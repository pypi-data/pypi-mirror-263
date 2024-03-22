from typing import Any, Callable, TypeVar, Generic, Union

T = TypeVar('T')


class ImmutableVariable(Generic[T]):
    def __init__(self, value: T):
        object.__setattr__(self, '_value', value)

    def __repr__(self):
        return f'ImmutableVariable({type(self._value).__name__})'

    def __str__(self):
        return self.__repr__()

    def _check_method(self, operand_name: str, *args):
        if not hasattr(self._value, operand_name):
            types = '", "'.join(type(arg).__name__ for arg in args)
            raise TypeError(
                f'Unsupported operand type(s) for {operand_name}: "{type(self._value).__name__}" and "{types}"')
        return getattr(self._value, operand_name)

    def _binary_proxy(self, operand_name: str, other: Any) -> Any:
        method = self._check_method(operand_name, other)
        result = method(other)
        return result

    def _unary_proxy(self, operand_name: str) -> Any:
        method = self._check_method(operand_name)
        return method()

    def __getattr__(self, name: str) -> Any:
        if hasattr(self._value, name):
            return getattr(self._value, name)
        else:
            raise AttributeError(f"{type(self._value).__name__} object has no attribute '{name}'")

    def __setattr__(self, key: str, value: Any) -> None:
        raise AttributeError("Cannot modify immutable variable")

    def __delattr__(self, item: str) -> None:
        raise AttributeError("Cannot delete immutable variable attributes")

    def __call__(self, *args, **kwargs) -> Any:
        if callable(self._value):
            return self._value(*args, **kwargs)
        else:
            raise TypeError(f"{type(self._value).__name__} object is not callable")

    def __getitem__(self, key: Any) -> Any:
        if hasattr(self._value, '__getitem__'):
            return self._value[key]
        else:
            raise TypeError(f"'{type(self._value).__name__}' object is not subscriptable")

    def __add__(self, other: Any) -> Any:
        return self._binary_proxy('__add__', other)

    def __sub__(self, other: Any) -> Any:
        return self._binary_proxy('__sub__', other)

    def __mul__(self, other: Any) -> Any:
        return self._binary_proxy('__mul__', other)

    def __truediv__(self, other: Any) -> Any:
        return self._binary_proxy('__truediv__', other)

    def __floordiv__(self, other: Any) -> Any:
        return self._binary_proxy('__floordiv__', other)

    def __mod__(self, other: Any) -> Any:
        return self._binary_proxy('__mod__', other)

    def __pow__(self, other: Any) -> Any:
        return self._binary_proxy('__pow__', other)

    def __radd__(self, other: Any) -> Any:
        return other + self._value

    def __rsub__(self, other: Any) -> Any:
        return other - self._value

    def __rmul__(self, other: Any) -> Any:
        return other * self._value

    def __rtruediv__(self, other: Any) -> Any:
        return other / self._value

    def __rfloordiv__(self, other: Any) -> Any:
        return other // self._value

    def __rmod__(self, other: Any) -> Any:
        return other % self._value

    def __rpow__(self, other: Any) -> Any:
        return other ** self._value

    def __pos__(self) -> Any:
        return self._unary_proxy('__pos__')

    def __neg__(self) -> Any:
        return self._unary_proxy('__neg__')

    def __invert__(self) -> Any:
        return self._unary_proxy('__invert__')

    def __and__(self, other: Any) -> Any:
        return self._binary_proxy('__and__', other)

    def __or__(self, other: Any) -> Any:
        return self._binary_proxy('__or__', other)

    def __xor__(self, other: Any) -> Any:
        return self._binary_proxy('__xor__', other)

    def __lshift__(self, other: Any) -> Any:
        return self._binary_proxy('__lshift__', other)

    def __rshift__(self, other: Any) -> Any:
        return self._binary_proxy('__rshift__', other)

    def __eq__(self, other: Any) -> bool:
        return self._binary_proxy('__eq__', other)

    def __ne__(self, other: Any) -> bool:
        return self._binary_proxy('__ne__', other)

    def __lt__(self, other: Any) -> bool:
        return self._binary_proxy('__lt__', other)

    def __le__(self, other: Any) -> bool:
        return self._binary_proxy('__le__', other)

    def __gt__(self, other: Any) -> bool:
        return self._binary_proxy('__gt__', other)

    def __ge__(self, other: Any) -> bool:
        return self._binary_proxy('__ge__', other)

    def __contains__(self, item: Any) -> bool:
        return self._binary_proxy('__contains__', item)

    def __len__(self) -> int:
        return self._unary_proxy('__len__')

    def __iter__(self):
        if hasattr(self._value, '__iter__'):
            return iter(self._value)
        else:
            raise TypeError(f"'{type(self._value).__name__}' object is not iterable")

    def __next__(self):
        if hasattr(self._value, '__next__'):
            return next(self._value)
        else:
            raise TypeError(f"'{type(self._value).__name__}' object is not an iterator")

    def __reversed__(self):
        if hasattr(self._value, '__reversed__'):
            return reversed(self._value)
        else:
            raise TypeError(f"'{type(self._value).__name__}' object is not reversible")

    def __enter__(self):
        return self._unary_proxy('__enter__')

    def __exit__(self, exc_type, exc_value, traceback):
        if hasattr(self._value, '__exit__'):
            return self._value.__exit__(exc_type, exc_value, traceback)
        else:
            raise TypeError(f"'{type(self._value).__name__}' object is not a context manager")

