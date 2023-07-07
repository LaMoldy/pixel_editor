from tkinter import Canvas

from utils.action_delete import Action_Delete


class Action_Create:
    def __init__(self, canvas: Canvas, id: int, coords: tuple[int, int], pixel_size: float, color: str):
        self.canvas = canvas
        self.id = id
        self.coords = coords
        self.pixel_size = pixel_size
        self.color = color

    def undo(self):
        self.canvas.delete(self.id)
        new_action_delete = Action_Delete(self.canvas, self.coords, self.pixel_size, self.color)
        return new_action_delete
