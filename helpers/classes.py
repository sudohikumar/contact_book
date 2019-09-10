from dataclasses import dataclass, field

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class config:
    MONGO_HOST: str
    USERNAME: str
    PASSWORD: str
    DATABASE: str
    COLLECTION: str


@dataclass_json
@dataclass
class contacts_data:
    email: str
    name: str
    phone: str
