from typing import Callable, Generic, TypeVar
from .immutable_types import ImmutableVariable

T = TypeVar('T')

class LazyVariable(Generic[T]):
    def __init__(self, initializer: Callable[..., T], *args, **kwargs):
        object.__setattr__(self, '_initializer', initializer)
        object.__setattr__(self, '_args', args)
        object.__setattr__(self, '_kwargs', kwargs)
        object.__setattr__(self, '_immutable_value', None)
        object.__setattr__(self, '_initialized', False)

    def _initialize(self) -> None:
        if not self._initialized:
            value = self._initializer(*self._args, **self._kwargs)
            object.__setattr__(self, '_immutable_value', ImmutableVariable(value))
            object.__setattr__(self, '_initialized', True)

    def __getattr__(self, item: str):
        self._initialize()
        if hasattr(self._immutable_value, item):
            return getattr(self._immutable_value, item)
        raise AttributeError(f'{self.__class__.__name__} object has no attribute "{item}"')

    def __getitem__(self, key):
        self._initialize()
        if hasattr(self._immutable_value, '__getitem__'):
            return self._immutable_value[key]
        else:
            raise KeyError(f'{key} not found in {self._immutable_value}')

    def __call__(self, *args, **kwargs):
        self._initialize()
        if callable(self._immutable_value):
            return self._immutable_value(*args, **kwargs)
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not callable')

    def __setattr__(self, key, value):
        if '_initialized' in self.__dict__ and self.__dict__['_initialized'] and key not in ['_initializer', '_args', '_kwargs', '_immutable_value', '_initialized']:
            raise AttributeError('Cannot modify attributes of a lazy immutable variable')
        super().__setattr__(key, value)

    def __delattr__(self, item):
        if '_initialized' in self.__dict__ and self.__dict__['_initialized']:
            raise AttributeError('Cannot delete attributes of a lazy immutable variable')
        super().__delattr__(item)

    def __add__(self, other):
        self._initialize()
        return self._immutable_value + other

    def __sub__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__sub__'):
            return self._immutable_value - other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not subtractable')

    def __mul__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__mul__'):
            return self._immutable_value * other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not multipliable')

    def __truediv__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__truediv__'):
            return self._immutable_value / other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not divisible')

    def __floordiv__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__floordiv__'):
            return self._immutable_value // other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not floor-divisible')

    def __mod__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__mod__'):
            return self._immutable_value % other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not modifiable')

    def __pow__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__pow__'):
            return self._immutable_value ** other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not powerable')

    def __radd__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__radd__'):
            return other + self._immutable_value
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not addable')

    def __rsub__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__rsub__'):
            return other - self._immutable_value
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not subtractable')

    def __rmul__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__rmul__'):
            return other * self._immutable_value
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not multipliable')

    def __rtruediv__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__rtruediv__'):
            return other / self._immutable_value
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not divisible')

    def __rfloordiv__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__rfloordiv__'):
            return other // self._immutable_value
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not floor-divisible')

    def __rmod__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__rmod__'):
            return other % self._immutable_value
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not modifiable')

    def __rpow__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__rpow__'):
            return other ** self._immutable_value
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not powerable')

    def __pos__(self):
        self._initialize()
        if hasattr(self._immutable_value, '__pos__'):
            return +self._immutable_value
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support positive operator')

    def __neg__(self):
        self._initialize()
        if hasattr(self._immutable_value, '__neg__'):
            return -self._immutable_value
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support negative operator')

    def __invert__(self):
        self._initialize()
        if hasattr(self._immutable_value, '__invert__'):
            return ~self._immutable_value
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support bitwise not operator')

    def __and__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__and__'):
            return self._immutable_value & other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support bitwise and operator')

    def __or__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__or__'):
            return self._immutable_value | other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support bitwise or operator')

    def __xor__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__xor__'):
            return self._immutable_value ^ other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support bitwise xor operator')

    def __lshift__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__lshift__'):
            return self._immutable_value << other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support left shift operator')

    def __rshift__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__rshift__'):
            return self._immutable_value >> other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support right shift operator')

    def __eq__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__eq__'):
            return self._immutable_value == other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support equality operator')

    def __ne__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__ne__'):
            return self._immutable_value != other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support inequality operator')

    def __lt__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__lt__'):
            return self._immutable_value < other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support less than operator')

    def __le__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__le__'):
            return self._immutable_value <= other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support less than or equal to operator')

    def __gt__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__gt__'):
            return self._immutable_value > other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support greater than operator')

    def __ge__(self, other):
        self._initialize()
        if hasattr(self._immutable_value, '__ge__'):
            return self._immutable_value >= other
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support greater than or equal to operator')

    def __contains__(self, item):
        self._initialize()
        if hasattr(self._immutable_value, '__contains__'):
            return item in self._immutable_value
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support containment check')

    def __len__(self):
        self._initialize()
        if hasattr(self._immutable_value, '__len__'):
            return len(self._immutable_value)
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support length check')

    def __iter__(self):
        self._initialize()
        if hasattr(self._immutable_value, '__iter__'):
            return iter(self._immutable_value)
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not iterable')

    def __next__(self):
        self._initialize()
        if hasattr(self._immutable_value, '__next__'):
            return next(self._immutable_value)
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object is not an iterator')

    def __reversed__(self):
        self._initialize()
        if hasattr(self._immutable_value, '__reversed__'):
            return reversed(self._immutable_value)
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support reverse iteration')

    def __enter__(self):
        self._initialize()
        if hasattr(self._immutable_value, '__enter__'):
            return self._immutable_value.__enter__()
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support context management')

    def __exit__(self, exc_type, exc_value, traceback):
        self._initialize()
        if hasattr(self._immutable_value, '__exit__'):
            return self._immutable_value.__exit__(exc_type, exc_value, traceback)
        else:
            raise TypeError(f'{type(self._immutable_value).__name__} object does not support context management')