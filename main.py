from utils.component import ComponentFactory

# Window Settings
window_title = "Pixel Editor"
window_dimensions = (1700, 900)
window_bg_colour = "grey"
window = ComponentFactory.create_window(window_title, window_dimensions, window_bg_colour)

# Place Components here


window.mainloop()
