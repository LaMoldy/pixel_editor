from tkinter import *


class ComponentFactory:

    @staticmethod
    def create_window(title: str, dimensions: tuple[int, int], bg: str, resizable: bool) -> Tk:
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
        window.geometry(f"{dimensions[0]}x{dimensions[1]}")
        window.configure(bg=bg)
        window.resizable(resizable, resizable)
        return window

    @staticmethod
    def create_button(window: Tk, text: str) -> Button:
        """
        Creates a new button

        Args:
            window (tk.Tk): The window
            text (str): The buttons text

        Returns:
            Button: A new Button
        """
        button = Button(
            window,
            text=text,
        )
        button.pack()
        return button
