from utils.canvas_manager import Canvas_Manager
from utils.component import ComponentFactory


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
        self.cached_actions = []
        self.load_components()
        self.window.mainloop()

    def load_components(self):
        """
        Loads the main components of the app.
        """
        resolution = (900, 900)
        canvas = ComponentFactory.create_canvas(self.window, resolution)
        canvas.pack()
        canvas_object = Canvas_Manager(canvas)

        clear_button = ComponentFactory.create_button(self.window, "Clear", command=canvas_object.clear)
        clear_button.pack()

        change_color_button = ComponentFactory.create_button(self.window, "Change Colour",
                                                             command=canvas_object.change_colour)
        change_color_button.pack()

        open_image_button = ComponentFactory.create_button(self.window, text="Open Image",
                                                           command=canvas_object.open_image)
        open_image_button.pack()


App("Pixel Editor", "grey")
