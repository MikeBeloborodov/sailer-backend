from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.settings import settings
from database.models import Base
from database.database_logic import engine

SQLALCHEMY_TEST_DATABASE_URL = (f"postgresql://"
                            f"{settings.database_username}:"
                            f"{settings.database_password}@"
                            f"{settings.database_hostname}/"
                            f"{settings.database_name}_test")


engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)


TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)

# overridden db test session for sqlalchemy
def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()