import pygame
from vectormath import Vector2
from abc import ABC, abstractmethod
from ModuleVisibles import Hitbox
from typing import Any, List, Union


class PerspectivePlayerX(ABC):
    _hitbox: Hitbox
    _position_x: int
    _player: Any

    @abstractmethod
    def load(self, path: str) -> None:
        self._player = pygame.image.load(path)

    @property
    def hitbox(self) -> Hitbox:
        return self._hitbox

    @property
    def position_x(self) -> int:
        return self._position_x

    @hitbox.setter
    def hitbox(self, value: Hitbox):
        self._hitbox = value

    @position_x.setter
    def position_x(self, value: int):
        self._position_x = value

    @abstractmethod
    def step(self, step: int, delta_time: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def check(self, collisions: Union[List[Hitbox], List[pygame.Rect], Hitbox, pygame.Rect]) -> bool:
        if isinstance(collisions, Hitbox):
            return self._hitbox.check(collisions.box)
        elif isinstance(collisions, pygame.Rect):
            return self._hitbox.check(collisions)
        elif isinstance(collisions, list):
            for collision in collisions:
                if isinstance(collision, Hitbox):
                    if self._hitbox.check(collision.box):
                        return True
                elif isinstance(collision, pygame.Rect):
                    if self._hitbox.check(collision):
                        return True
        return False


class PerspectivePlayerXY(ABC):
    _hitbox: Hitbox
    _pos: Vector2

    @property
    def hitbox(self) -> Hitbox:
        return self._hitbox

    @property
    def position(self) -> Vector2:
        return self._pos

    @hitbox.setter
    def hitbox(self, value: Hitbox):
        self._hitbox = value

    @position.setter
    def position(self, value: Vector2):
        self._pos = value

    @abstractmethod
    def step(self, step: int, delta_time: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def reset(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def check(self, collisions: Union[List[Hitbox], List[pygame.Rect], Hitbox, pygame.Rect]) -> bool:
        if isinstance(collisions, Hitbox):
            return self._hitbox.check(collisions.box)
        elif isinstance(collisions, pygame.Rect):
            return self._hitbox.check(collisions)
        elif isinstance(collisions, list):
            for collision in collisions:
                if isinstance(collision, Hitbox):
                    if self._hitbox.check(collision.box):
                        return True
                elif isinstance(collision, pygame.Rect):
                    if self._hitbox.check(collision):
                        return True
        return False
