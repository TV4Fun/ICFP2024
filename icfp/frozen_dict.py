from typing import Optional, TypeVar, Hashable

K = TypeVar('K', bound=Hashable)
V = TypeVar('V', bound=Hashable)


class FrozenDict(dict[K, V]):
    def __init__(self, copy_from: Optional[dict[K, V]] = None, add: Optional[tuple[K, V]] = None) -> None:
        if copy_from is None:
            super().__init__()
        else:
            super().__init__(copy_from)
        if add:
            key, value = add
            super().__setitem__(key, value)
        _hash = 0
        for i, (k, v) in enumerate(sorted(self.items())):
            _hash ^= hash(k) ^ (hash(v) << (i + 1))
        self._hash = _hash

    def __add__(self, other: tuple[K, V]) -> 'FrozenDict[K, V]':
        return FrozenDict(self, other)

    def __setitem__(self, key: K, value: V) -> None:
        raise TypeError("Attempt to set item on FrozenDict")

    def __hash__(self) -> int:
        return self._hash
