from pydantic import BaseModel, model_validator


class EnvNames(BaseModel):
    current_env: str
    other_envs: list[str]

    @model_validator(mode='after')
    def remove_current_from_other_envs(self):
        try:
            self.other_envs.remove(self.current_env)
        finally:
            return self
