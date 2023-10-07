from dataclasses import dataclass

@dataclass
class Provider:
    instances = []
    name: str
    url: str

    def __post_init__(self):
        self.instances.append(self)

@dataclass
class Service:
    instances = []
    name: str
    provider: str
    url: str

    def __post_init__(self):
        self.instances.append(self)
