from tkinter import *
from tkinter import ttk


class ComponentFactory:

    @staticmethod
    def create_window(title: str, bg: str, resizable: bool, dimensions: tuple[int, int] = None) -> Tk:
        """
        Creates a new window

        Args:
            title (str): Window title
            dimensions (tuple): Dimensions of the window
            bg (str): Window background colour
            resizable (bool): Window resizing ability

        Returns:
            Tk: A new window
        """
        window = Tk()
        window.title(title)
        if dimensions is not None:
            window.geometry(f"{dimensions[0]}x{dimensions[1]}")
        window.configure(bg=bg)
        window.resizable(resizable, resizable)
        return window

    @staticmethod
    def create_button(window: Tk, text: str = None, command: any = None) -> ttk.Button:
        """
        Creates a new button

        Args:
            window (tk.Tk): The window
            text (str): The buttons text
            command (any): The command

        Returns:
            Button: A new Button

        """
        button = ttk.Button(
            window,
            text=text,
            command=command
        )
        return button

    @staticmethod
    def create_canvas(window: Tk, res: tuple[int, int]):
        """
                Creates a Canvas object

                Args:
                    res (tuple): the resolution


                Returns:
                    Canvas: A new Canvas


                """
        canvas = Canvas(window,
                        bg="#FFFFFF",
                        height=res[0],
                        width=res[1])

        return canvas
