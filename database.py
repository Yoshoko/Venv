from sqlmodel import SQLModel,create_engine, Session


file_name = "database.sqlite"

engine = create_engine(f"sqlite:///{file_name}")

SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)