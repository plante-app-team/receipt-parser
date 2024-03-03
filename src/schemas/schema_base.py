from dataclasses import dataclass, asdict
from datetime import datetime
from uuid import UUID


@dataclass
class SchemaBase:
    id: UUID | int | str  # make sure every object has id

    def to_dict(self) -> dict:
        obj = asdict(self)
        for key, val in obj.items():
            if isinstance(val, UUID):
                obj[key] = str(val)
            elif isinstance(val, datetime):
                obj[key] = val.isoformat()

        obj["id"] = str(self.id)
        return obj
