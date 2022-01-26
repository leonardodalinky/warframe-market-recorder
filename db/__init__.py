from dataclasses import dataclass, fields
import os
from dotenv import load_dotenv

from sqlalchemy.orm.decl_api import registry
from sqlalchemy.orm.decl_api import declared_attr
from sqlalchemy import create_engine, Column, Integer


load_dotenv()

@dataclass
class _Base:
    __proto_enums__ = []
    id: int = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def load_json_dict(self, d) -> None:
        field_names = [field.name for field in fields(self.__class__)]
        field_names = list(filter(lambda x: x not in self.__proto_enums__ and x != "id", field_names))
        for field_name in field_names:
            setattr(self, field_name, d[field_name])
        self._load_proto_from_json_dict(d)

    def _load_proto_from_json_dict(self, d) -> None:
        # TO IMPLEMENT IN SUBCLASS
        pass

Base = registry().generate_base(cls=_Base)

engine = create_engine(os.getenv("DB_URL"))

# constants
REPO_VERSION = 1
MIGRATE_REPO = "migrate_repo"
