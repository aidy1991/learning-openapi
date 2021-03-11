from dataclasses import dataclass


@dataclass
class Pet:
    id: int
    name: str
    tag: str


def get():
    return [Pet(id=0, name='hoge', tag="hoge0"),
            Pet(id=1, name="foo", tag="foo1")], 200, {"x-next": "next"}
