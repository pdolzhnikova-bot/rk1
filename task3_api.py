from typing import Annotated

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    price: Annotated[float, Field(gt=0)]
    tags: list[str] = Field(default_factory=list)


class ItemWithId(Item):
    id: int


_items: list[ItemWithId] = []
_next_id: int = 1


@app.post("/items", response_model=ItemWithId)
def create_item(item: Item) -> ItemWithId:
    global _next_id
    new_item = ItemWithId(id=_next_id, **item.model_dump())
    _next_id += 1
    _items.append(new_item)
    return new_item
