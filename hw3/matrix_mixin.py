import numpy as np

import numbers

from numpy.lib.mixins import NDArrayOperatorsMixin


class RepresentationMixin:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = np.asarray(value)

    def __str__(self):
        res = ""
        for s in self.value:
            res += str(s) + '\n'
        return '[' + res[:-1] + ']'

    def write_to_file(self, file):
        with open(file, 'w') as f:
            f.write(self.__str__())

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.value)


class MatrixExt(NDArrayOperatorsMixin, RepresentationMixin):

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (MatrixExt,)):
                return NotImplemented

        inputs = tuple(x.value if isinstance(x, MatrixExt) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.value if isinstance(x, MatrixExt) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)
