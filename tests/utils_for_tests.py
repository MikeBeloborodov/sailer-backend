from sqlalchemy.orm import Session
from tests.database_for_tests import engine 
from database.models import User


def delete_test_user(email: str = 'admin@mail.com'):
    with Session(engine) as session:
        session.query(User).filter(User.email == email).delete()
        session.commit()
