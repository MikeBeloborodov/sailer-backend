from pydantic import BaseSettings

# this is for production on heroku
class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str

    class Config:
        env_file = ('.env')


settings = Settings()