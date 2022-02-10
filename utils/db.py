from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mysql+pymysql://root:ka*dj#D23Aff2@localhost:3307/prod", echo=True)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def create_session():
    return Session()


def insert(model_instance):
    session = create_session()
    try:
        session.add(model_instance)
        session.commit()
    finally:
        session.close()

