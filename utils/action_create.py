from tkinter import Canvas


class Action_Create:
    current_action_create = []
    cached_action_creates = []

    def __init__(self, canvas: Canvas, id: int, coords: tuple[int, int], pixel_size: float, color: str):
        Action_Create.current_action_create.append(self)
        self.canvas = canvas
        self.id = id
        self.coords = coords
        self.pixel_size = pixel_size
        self.color = color
        self.current_action_create = Action_Create.current_action_create

    def undo(self):
        self.canvas.delete(self.id)
        from utils.action_delete import Action_Delete
        Action_Delete(self.canvas, self.coords, self.pixel_size, self.color)

    @staticmethod
    def update_cache():
        if len(Action_Create.current_action_create) > 0:
            Action_Create.cached_action_creates.append(Action_Create.current_action_create.copy())
            Action_Create.current_action_create.clear()
