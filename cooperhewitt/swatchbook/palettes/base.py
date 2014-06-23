import json

class base:

    def __init__(self):

        self.source = None
        self.colours = None

    def __str__(self):
        return self.as_json(indent=2)

    def source(self):
        return self.__source__

    def colours(self):
        return self.__colours__

    def colors(self):
        return self.colours()

    def as_dict(self):

        return {
            'source': self.source(),
            'colours': self.colours()
        }

    def as_json(self, **kwargs):

        return json.dumps(self.as_dict(), **kwargs)

    def name(self, hex):

        hex = hex.lower()

        details = self.__colours__.get(hex, None)

        if not details:
            raise Exception, "Invalid hex colour"

        return details['name']

    def hex(self, name):

        name = name.lower()

        for hex, details in self.__colours__.items():
            
            if details.get('name', None) == name:
                return hex

        raise Exception, "Invalid colour name"
