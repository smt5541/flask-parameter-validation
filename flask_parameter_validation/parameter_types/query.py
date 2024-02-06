"""
    Query Parameters
    - i.e. sent in GET requests, /?username=myname
"""
import json

from .parameter import Parameter


class Query(Parameter):
    name = "query"

    def __init__(self, default=None, **kwargs):
        super().__init__(default, **kwargs)

    def convert(self, value, allowed_types):
        """Convert query parameters to corresponding types."""
        print(f"Query#convert received {type(value)}")
        if type(value) is str:
            # int conversion
            if int in allowed_types:
                try:
                    value = int(value)
                except ValueError:
                    pass
            # float conversion
            if float in allowed_types:
                try:
                    value = float(value)
                except ValueError:
                    pass
            # bool conversion
            if bool in allowed_types:
                if value.lower() == "true":
                    value = True
                elif value.lower() == "false":
                    value = False
            # dict conversion
            if dict in allowed_types:
                try:
                    value = json.loads(value)
                except ValueError:
                    raise ValueError(f"invalid JSON")
        print(f"Query#convert returned {type(value)}")
        return super().convert(value, allowed_types)
