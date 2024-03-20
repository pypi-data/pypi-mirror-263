from .base_controller import BaseController


class Page:
    def __init__(self, name: str, controller: BaseController, icon: str = None):
        self.name = name
        self.controller = controller
        self.icon = icon
        self.rendered = False

    def render(self):
        if not self.rendered:
            self.rendered = True
            self.controller.render()

    def get_content(self):
        self.render()
        return self.controller.view
