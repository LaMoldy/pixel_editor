import tkinter as tk
from tkinter import ttk


class ComponentFactory:

    @staticmethod
    def create_window(title: str, dimensions: tuple[int, int], bg: str, resizable: bool) -> tk.Tk:
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
        window = tk.Tk()
        window.title(title)
        window.geometry(f"{dimensions[0]}x{dimensions[1]}")
        window.configure(bg=bg)
        window.resizable(resizable, resizable)
        return window

    @staticmethod
    def create_button(window: tk.Tk, text: str) -> ttk.Button:
        """
        Creates a new button

        Args:
            window (tk.Tk): The window
            text (str): The buttons text

        Returns:
            Button: A new Button
        """
        button = ttk.Button(
            window,
            text=text,
        )
        button.pack()
        return button
