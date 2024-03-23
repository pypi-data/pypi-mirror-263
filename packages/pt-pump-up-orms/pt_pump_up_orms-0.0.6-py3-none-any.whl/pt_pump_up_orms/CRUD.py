from abc import ABC, abstractmethod


class CRUD(ABC):
    def __init__(self, route, **kwargs) -> None:
        super().__init__()

        if route is None:
            raise ValueError("route cannot be None")

        self.route = route.replace("/", "")
        self._id = None
        self._json = dict()

        self.bootstrap(kwargs)

        self._client = None

    def bootstrap(self, kwargs):
        for key, value in kwargs.items():
            if key == "id":
                self._id = value
            elif value is not None:
                self._json[key] = value

    @abstractmethod
    def index(self):
        pass

    @abstractmethod
    def store(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def destroy(self):
        pass

    # Getters and Setters
    @property
    def client(self):
        if self._client is None:
            raise ValueError("client cannot be None")
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    @property
    def id(self):
        return self._id

    # Avoid numpy 64-bit integer that are not JSON serializable
    @id.setter
    def id(self, value):
        if value is not None:
            self._id = int(value)
        else:
            self._id = None

    @property
    def json(self):

        if not self._json and self._id is not None:
            print(f"JSON is empty, fetching from server with id{self._id}")
            self.show()
        elif not self._json and self._id is None:
            raise ValueError(f"JSON is empty and id is None")

        return self._json
