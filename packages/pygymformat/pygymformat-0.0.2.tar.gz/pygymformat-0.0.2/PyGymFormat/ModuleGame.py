from typing import NoReturn, Any, List, Tuple
from abc import ABC, abstractmethod
import pygame


class GameBase(ABC):
    clock = pygame.time.Clock()
    running = True

    entities: List[Any] = []
    dt = 0

    @abstractmethod
    def init(self, window_size: Tuple[int, int], dt: int) -> NoReturn:
        self.dt = dt
        pygame.init()
        if window_size[0] < 0 or window_size[1] < 0:
            raise RuntimeError("Invalid Arguments")
        pygame.display.set_mode(window_size)

    @abstractmethod
    def render(self):
        for entity in self.entities:
            try:
                entity.render()
            except AttributeError:
                pass

    @abstractmethod
    def close(self):
        raise NotImplementedError

    @abstractmethod
    def step(self):
        for entity in self.entities:
            try:
                entity.frame(self.dt)
            except AttributeError:
                pass


class GameInstance:
    pass
