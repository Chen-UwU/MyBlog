from typing import Union,List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    id: Union[int, None] = None

ls:List[Item] = []

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    global ls
    item = None
    for i in ls:
        if i.id == item_id:
            item = i
    if not item:
        return{'?':"你查了一个什么东西？"}
    return {"item_id": item_id, "q": q, 'item': item.model_dump()}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    global ls
    ls.append(item)
    return {"item_name": item.name, "item_id": item_id}