from pydantic import BaseModel


class CringeEnvironment(BaseModel):
    description: str
    aliases: list[str] = []
