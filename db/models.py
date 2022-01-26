from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from sqlalchemy import VARCHAR, Boolean, Column, Integer, null
from sqlalchemy.orm import relationship

from . import Base

from proto3.models import proto3_pb2 as model_proto


@dataclass
class Item(Base):
    __tablename__ = "items"
    __proto_enums__ = ["category"]

    category: int = Column(Integer)
    tradable: bool = Column(Boolean)
    type: str = Column(VARCHAR(128))
    uniqueName: str = Column(VARCHAR(128), unique=True, nullable=False)

    def _load_proto_from_json_dict(self, d) -> None:
        # TO IMPLEMENT IN SUBCLASS
        category: str = d["category"]
        self.category = model_proto.ItemCategory.Value(category.replace("-", ""))
