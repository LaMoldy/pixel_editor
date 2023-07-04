import io
from tkinter import filedialog

from utils.component import ComponentFactory
from PIL import Image, ImageDraw, ImageTk, ImageGrab

# Window Settings
window_title = "Pixel Editor"
window_dimensions = (1700, 900)
window_bg_colour = "grey"
window_resizable = True
window = ComponentFactory.create_window(window_title, window_dimensions, window_bg_colour, window_resizable)

# Place Components here
resolution = (900, 900)
pixel_size = 20
zoom_factor = 1

canvas = ComponentFactory.create_canvas(window, resolution)
canvas.pack(side="bottom")


def draw_pixel(event):
    x = event.x // pixel_size
    y = event.y // pixel_size
    canvas.create_rectangle(x * pixel_size, y * pixel_size, (x + 1) * pixel_size, (y + 1) * pixel_size,
                            fill="black")


canvas.bind("<B1-Motion>", draw_pixel)


def clear_canvas():
    canvas.delete("all")


clear_button = ComponentFactory.create_button(window, "Clear", command=clear_canvas)
clear_button.pack(side="top")


def zoom_in():
    global zoom_factor
    zoom_factor *= 2
    redraw_canvas()


def zoom_out():
    global zoom_factor
    if zoom_factor > 1:
        zoom_factor //= 2
        redraw_canvas()


def redraw_canvas():
    canvas.delete("all")
    for x in range(resolution[0] // pixel_size):
        for y in range(resolution[0] // pixel_size):
            canvas.create_rectangle(x * pixel_size, y * pixel_size,
                                    (x + 1) * pixel_size, (y + 1) * pixel_size,
                                    fill="black")


zoom_in_button = ComponentFactory.create_button(window, text="Zoom In", command=zoom_in)
zoom_in_button.pack()

zoom_out_button = ComponentFactory.create_button(window, text="Zoom Out", command=zoom_out)
zoom_out_button.pack()


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




save_button = ComponentFactory.create_button(window, text="Save Image", command=save_image)
save_button.pack()

window.mainloop()
