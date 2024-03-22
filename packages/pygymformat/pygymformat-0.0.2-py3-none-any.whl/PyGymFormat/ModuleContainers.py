import pygame
from vectormath import Vector2
from typing import List, Union, Any
from ModuleInvisible import Hitbox


class PerspectiveContainer:
    def __init__(self, widgets: List[Any]):
        self.widgets = widgets
        self.mov: Vector2 = Vector2(0, 0)

    @property
    def widgets(self):
        return self._widgets

    @widgets.setter
    def widgets(self, data: List[Any]):
        self._widgets = data

    @widgets.deleter
    def widgets(self):
        self._widgets = None

    def check(self, collisions: Union[List[Union[pygame.Rect, Hitbox]], Union[pygame.Rect, Hitbox]]):
        for widget in self.widgets:
            if widget.check(collisions):
                return widget

    def render(self):
        for widget in self.widgets:
            widget.render()

    def reset(self):
        for widget in self.widgets:
            widget.reset()

    def add_widget(self, widget: Any):
        self.widgets.append(widget)

    def remove_widget(self, widget: Any):
        self.widgets.remove(widget)

    def clear(self):
        self.widgets.clear()

    def step(self, dt: int):
        for widget in self.widgets:
            widget.step(dt)
