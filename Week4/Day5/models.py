from dataclasses import dataclass

@dataclass
class Book:
    id: int
    title:str
    author: str
    status: str

@dataclass
class User:
    id: int
    name:str
