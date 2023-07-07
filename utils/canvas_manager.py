from tkinter import filedialog, colorchooser
from tkinter import *

from PIL import ImageGrab, Image, ImageTk

from utils.action_create import Action_Create
from utils.action_delete import Action_Delete


class Canvas_Manager:

    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.selected_colour = "black"
        self.pixel_size = 14.0625
        self.resolution = (900, 900)
        canvas.bind("<B1-Motion>", self.draw_pixel)
        canvas.master.bind("<ButtonRelease-1>", self.on_draw_finish)
        canvas.master.bind("<ButtonRelease-3>", self.on_erase_finish)
        canvas.bind("<B3-Motion>", self.erase_pixel)
        canvas.master.bind("<Control-z>", self.undo)
        canvas.master.bind("<Alt-z>", self.redo)

    def draw_pixel(self, event):
        """
        Draws a pixel on the canvas.
        Is run when Mouse 1 is held and moved.

        Args:
            event: the event object

        """

        x = event.x // self.pixel_size
        y = event.y // self.pixel_size
        coords = (x, y)
        rect = self.canvas.create_rectangle(x * self.pixel_size, y * self.pixel_size, (x + 1) * self.pixel_size,
                                            (y + 1) * self.pixel_size,
                                            fill=self.selected_colour, outline=self.selected_colour)
        Action_Create(self.canvas, rect, coords, self.pixel_size, self.selected_colour)

    @staticmethod
    def on_draw_finish(_):
        """Called when drawing finishes. Adds the actions to cached_actions list."""
        Action_Create.update_cache()

    def erase_pixel(self, event):
        """Checks if a pixel exists where the mouse is and deletes it."""

        x = event.x // self.pixel_size
        y = event.y // self.pixel_size

        for action_create in Action_Create.cached_action_creates:
            for action in action_create:
                coords = action.coords
                if coords[0] == x and coords[1] == y:
                    action.undo()

    @staticmethod
    def on_erase_finish(_):
        Action_Delete.update_cache()

    @staticmethod
    def undo(_):
        """Undoes the last action the user did."""
        try:
            for action in Action_Create.cached_action_creates[-1]:
                action.undo()
            Action_Delete.update_cache()
            Action_Create.cached_action_creates.remove(Action_Create.cached_action_creates[-1])
        except IndexError:
            print("No more actions to revert.")

    @staticmethod
    def redo(_):
        """Redoes the last action the user did."""
        try:
            for action in Action_Delete.cached_action_delete[-1]:
                action.undo()
            Action_Create.update_cache()
            Action_Delete.cached_action_delete.remove(Action_Delete.cached_action_delete[-1])
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
