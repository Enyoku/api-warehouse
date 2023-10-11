from pydantic import BaseModel


class CategoryCreate(BaseModel):
    category_id: int
    category_name: str


class CategoryCreateJson(BaseModel):
    id: int
    name: str


class CategoryRead(BaseModel):
    category_id: int
    category_name: str

    class Config:
        orm_mode = True
