from abc import ABC, abstractmethod
from typing import List, Union, Any, Callable


class Physics(ABC):
    _rules: List[Union[Callable, Any]]

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, rules: List[Union[Callable, Any]]):
        self._rules = rules

    @rules.deleter
    def rules(self):
        self._rules = []

    def append(self, rule: List[Union[Callable, Any]]):
        self._rules.append(rule)

    def modify(self, index: int, new_rule: Union[Callable, Any]):
        self._rules[index] = new_rule

    def extend(self, rules: List[Union[Callable, Any]]):
        self._rules.extend(rules)

    @abstractmethod
    def step(self, dt):
        raise NotImplementedError
