from tkinter import Canvas


class Action_Delete:
    current_action_delete = []
    cached_action_delete = []

    def __init__(self, canvas: Canvas, coords: tuple[int, int], pixel_size: float, color: str):
        Action_Delete.current_action_delete.append(self)
        self.canvas = canvas
        self.x = coords[0]
        self.y = coords[1]
        self.pixel_size = pixel_size
        self.color = color
        self.current_action_delete = Action_Delete.current_action_delete

    def undo(self):
        rect = self.canvas.create_rectangle(self.x * self.pixel_size, self.y * self.pixel_size,
                                            (self.x + 1) * self.pixel_size,
                                            (self.y + 1) * self.pixel_size,
                                            fill=self.color, outline=self.color)
        from utils.action_create import Action_Create
        Action_Create(self.canvas, rect, (self.x, self.y), self.pixel_size, self.color)

    @staticmethod
    def update_cache():
        if len(Action_Delete.current_action_delete) > 0:
            Action_Delete.cached_action_delete.append(Action_Delete.current_action_delete.copy())
            Action_Delete.current_action_delete.clear()
