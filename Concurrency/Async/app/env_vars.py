from pydantic import BaseSettings, ValidationError


class EnvVar(BaseSettings):
    your_email: str
    email_to: str
    password: str
    subject: str
    text: str
    textType: str
    port: int

    class Config:
        env_file=".env"

try:
    env=EnvVar()  
except ValidationError as e:
    print(e.json())

