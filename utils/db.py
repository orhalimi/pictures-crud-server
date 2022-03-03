from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = create_engine(
    "mysql+pymysql://root:ka*dj#D23Aff2@localhost:3307/prod", echo=True)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()

