from tkinter import filedialog, colorchooser
from tkinter import *

from utils.component import ComponentFactory
from PIL import ImageGrab, Image, ImageTk


class App:

    def __init__(self, title: str, bg_color: str, resizable: bool = True):
        """
        The Application

        :param title: str: Set the title of the window
        :param bg_color: str: Set the background color of the window
        :param resizable: bool: Set the window to be resizable or not
        :return: Nothing
        :doc-author: Trelent
        """
        self.window = ComponentFactory.create_window(title, bg_color, resizable)
        self.selected_colour = "black"
        self.load_components()
        self.window.mainloop()

    def load_components(self):
        """
        Loads the main components of the app.
        """
        resolution = (900, 900)
        pixel_size = 14.0625

        canvas = ComponentFactory.create_canvas(self.window, resolution)
        canvas.pack()

        def draw_pixel(event):
            x = event.x // pixel_size
            y = event.y // pixel_size
            canvas.create_rectangle(x * pixel_size, y * pixel_size, (x + 1) * pixel_size, (y + 1) * pixel_size,
                                    fill=self.selected_colour, outline=self.selected_colour)

        def erase_pixel(event):
            x = event.x // pixel_size
            y = event.y // pixel_size
            rect = canvas.create_rectangle(x * pixel_size, y * pixel_size, (x + 1) * pixel_size, (y + 1) * pixel_size,
                                           outline="white", fill="white")

        canvas.bind("<B1-Motion>", draw_pixel)
        canvas.bind("<B3-Motion>", erase_pixel)

        def clear_canvas():
            canvas.delete("all")

        clear_button = ComponentFactory.create_button(self.window, "Clear", command=clear_canvas)
        clear_button.pack()

        def change_colour():
            color = colorchooser.askcolor()
            self.selected_colour = color[1]

        change_color_button = ComponentFactory.create_button(self.window, "Change Colour", command=change_colour)
        change_color_button.pack()

        def save_image():
            # Get the dimensions of the canvas
            x = canvas.winfo_rootx()
            y = canvas.winfo_rooty()
            width = canvas.winfo_width()
            height = canvas.winfo_height()

            # Capture a screenshot of the canvas
            screenshot = ImageGrab.grab((x, y, x + width, y + height))

            # Ask user for the save location and filename
            filename = filedialog.asksaveasfilename(defaultextension=".png",
                                                    filetypes=[("PNG Image", "*.png"), ("All Files", "*.*")])
            if filename:
                # Save the screenshot as an image file
                screenshot.save(filename)
                print("Image saved successfully.")

        save_button = ComponentFactory.create_button(self.window, text="Save Image", command=save_image)
        save_button.pack()

        def open_image():
            file = filedialog.askopenfile(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
            if file:
                image = (Image.open(file.name))
                resized_image = image.resize(resolution, Image.LANCZOS)
                new_image = ImageTk.PhotoImage(resized_image)
                self.image = new_image
                clear_canvas()
                canvas.create_image((450, 450), image=self.image)

        open_image_button = ComponentFactory.create_button(self.window, text="Open Image", command=open_image)
        open_image_button.pack()


App("Pixel Editor", "grey")
