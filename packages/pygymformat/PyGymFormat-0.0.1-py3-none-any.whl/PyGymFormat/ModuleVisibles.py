from vectormath import Vector2
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Union, Any
import pygame
from ModuleInvisible import Hitbox


class StaticVisible(ABC):
    _BOX: Optional[pygame.Rect]
    _POS: Optional[Tuple[int, int]]

    @property
    def box(self):
        return self._BOX

    @box.setter
    def box(self, data: pygame.Rect):
        self._BOX = data

    @box.deleter
    def box(self):
        self._BOX = None

    @property
    def pos(self):
        return self._POS

    @pos.setter
    def pos(self, data):
        self._POS = data

    @pos.deleter
    def pos(self):
        self._POS = None

    def check(self, collisions: Union[List[Union[pygame.Rect, Hitbox]], Union[pygame.Rect, Hitbox]]):
        for obj in collisions:
            if self._BOX.colliderect(obj):
                return True
        return False

    @abstractmethod
    def reset(self):
        raise NotImplementedError

    @abstractmethod
    def render(self):
        raise NotImplementedError


class Visible(ABC):
    _obj: Any
    _pos: Optional[Tuple[int, int]]
    _hitbox: Optional[Hitbox]
    mov: Vector2 = Vector2(0, 0)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, data: Tuple[int, int]):
        self._pos = data

    @pos.deleter
    def pos(self):
        self._pos = None

    @property
    def obj(self):
        return self._obj

    @obj.setter
    def obj(self, data: Any):
        self._obj = data

    @obj.deleter
    def obj(self):
        self._obj = None

    @abstractmethod
    def render(self):
        raise NotImplementedError

    @abstractmethod
    def frame(self, dt):
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        raise NotImplementedError
