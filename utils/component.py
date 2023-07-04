import tkinter as tk

class ComponentFactory():

    @staticmethod
    def create_window(title: str, dimensions: tuple[int, int], bg: str) -> tk.Tk:
        """
        Creates a new window

        Args:
            title (str): Window title
            dimension (tuple): Dimensions of the window
            bg (str): Window background colour

        Returns:
            Tk: A new window
        """
        window = tk.Tk()
        window.title(title)
        window.geometry(f"{dimensions[0]}x{dimensions[1]}")
        window.configure(bg=bg)
        return window
