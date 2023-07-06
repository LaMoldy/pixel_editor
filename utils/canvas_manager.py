from tkinter import filedialog, colorchooser
from tkinter import *

from PIL import ImageGrab, Image, ImageTk


class Canvas_Manager:

    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.selected_colour = "black"
        self.pixel_size = 14.0625
        self.resolution = (900, 900)
        self.cached_actions = []
        self.current_action = []
        self.action_length = []
        canvas.bind("<B1-Motion>", self.draw_pixel)
        canvas.master.bind("<ButtonRelease-1>", self.on_draw_finish)
        canvas.master.bind("<ButtonRelease-3>", self.on_draw_finish)
        canvas.bind("<B3-Motion>", self.erase_pixel)
        canvas.master.bind("<Control-z>", self.undo)

    def draw_pixel(self, event):
        """
        Draws a pixel on the canvas.
        Is run when Mouse 1 is held and moved.

        Args:
            event: the event object

        """

        x = event.x // self.pixel_size
        y = event.y // self.pixel_size
        rect = self.canvas.create_rectangle(x * self.pixel_size, y * self.pixel_size, (x + 1) * self.pixel_size,
                                            (y + 1) * self.pixel_size,
                                            fill=self.selected_colour, outline=self.selected_colour)
        self.current_action.append((rect, (x, y)))

    def erase_pixel(self, event):
        """Checks if a pixel exists where the mouse is and deletes it."""

        x = event.x // self.pixel_size
        y = event.y // self.pixel_size

        for action in self.cached_actions:
            coords = action[1]
            if coords[0] == x and coords[1] == y:
                self.canvas.delete(action[0])

    def on_draw_finish(self, _):
        """Called when drawing finishes. Adds the actions to cached_actions list."""
        self.cached_actions.extend(self.current_action)
        self.action_length.append(len(self.current_action))
        self.current_action.clear()

    def undo(self, _):
        """Undoes the last action the user did."""
        try:
            last_action_length = self.action_length[-1]
            action_start = len(self.cached_actions) - last_action_length
            action_end = len(self.cached_actions)
            for action in self.cached_actions[action_start:action_end]:
                print(action)
                self.canvas.delete(action[0])
                self.cached_actions.remove(action)
            self.action_length.remove(last_action_length)
        except IndexError:
            print("No more actions to revert.")

    def save_image(self):
        """Saves the image on the canvas via ImageGrab"""
        # Get the dimensions of the canvas
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Capture a screenshot of the canvas
        screenshot = ImageGrab.grab((x, y, x + width, y + height))

        # Ask user for the save location and filename
        filename = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG Image", "*.png"), ("All Files", "*.*")])
        if filename:
            # Save the screenshot as an image file
            screenshot.save(filename)
            print("Image saved successfully.")

    def open_image(self):
        """Prompts the user to open a file via file explorer."""

        # Asks to open file
        file = filedialog.askopenfile(defaultextension=".png", filetypes=[("PNG Image", "*.png")])

        # Checks if the user picked a file or not
        if file:
            # Opens and resizes image to canvas resolution
            image = (Image.open(file.name))
            resized_image = image.resize(self.resolution, Image.LANCZOS)
            new_image = ImageTk.PhotoImage(resized_image)

            # Adds the image to the object for memory
            self.image = new_image

            # Clears the canvas
            self.clear()

            # Creates an image on the canvas with the image the user opened
            self.canvas.create_image((450, 450), image=self.image)

    def clear(self):
        """Clears the canvas"""
        self.canvas.delete("all")

    def change_colour(self):
        """Sets the primary color to the choice of the user."""
        color = colorchooser.askcolor()
        self.selected_colour = color[1]
