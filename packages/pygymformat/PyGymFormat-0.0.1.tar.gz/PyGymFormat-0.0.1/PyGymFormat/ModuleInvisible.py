from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Union, Any, Callable
import pygame
from pygame.math import Vector2
from ModuleVisibles import Visible


class StaticInvisible(ABC):
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


class Hitbox(ABC):
    _base: Union[Visible, Any]
    _box: Optional[pygame.Rect]
    _pos: Optional[Tuple[int, int]]
    mov: Vector2 = Vector2(0, 0)

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, data: Union[Visible, Any]):
        self._base = data

    @base.deleter
    def base(self):
        self._base = None

    @property
    def box(self):
        return self._box

    @box.setter
    def box(self, data: pygame.Rect):
        self._box = data

    @box.deleter
    def box(self):
        self._box = None

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, data):
        self._pos = data

    @pos.deleter
    def pos(self):
        self._pos = None

    def check(self, collisions: Union[List[Union[pygame.Rect, Hitbox]], Union[pygame.Rect, Hitbox]]):
        for obj in collisions:
            if self._box.colliderect(obj):
                return True
        return False

    @abstractmethod
    def step(self, dt: int):
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        raise NotImplementedError


