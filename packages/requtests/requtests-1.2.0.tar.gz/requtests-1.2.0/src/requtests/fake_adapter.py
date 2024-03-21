from itertools import cycle
from requests import Response
from requests.adapters import BaseAdapter
from .protocols import OptionalAssertions


class FakeAdapter(BaseAdapter):
    def __init__(self, *responses: Response, assertions: OptionalAssertions = None):
        super().__init__()
        self.closed = 0
        self.responses = _to_generator(responses)
        self.assertions = _to_generator(assertions) if assertions else None

    def close(self):
        self.closed += 1

    def send(self, request, **kwargs):
        if self.assertions:
            next(self.assertions)(request, **kwargs)
        response = next(self.responses)
        response.request = request
        return response


def _to_generator(element_or_collection):
    if _is_iterable(element_or_collection):
        return (x for x in element_or_collection)
    else:
        return cycle([element_or_collection])


def _is_iterable(obj):
    return hasattr(obj, "__iter__")
