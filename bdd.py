'''
    CREATE TABLE IF NOT EXISTS stage(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        poste TEXT NOT NULL,
        entreprise TEXT NOT NULL,
        expedition TEXT NOT NULL,
        url TEXT         
    )               
'''
from stage_class import Stage, fake_stage
from projects_model import Project
from database import get_session
from typing import Optional
from sqlmodel import select

# INSERT
with get_session() as session:
    for j in range(0):
        new_stage = fake_stage()
        session.add(new_stage) #insert
        session.commit() #commit
        session.refresh(new_stage) #recup id
        print(new_stage)
        print(new_stage.id)

# SELECT
with get_session() as session:
    statement = select(Stage) # lien vers la classe
    results = session.exec(statement).all() # éxecuter + all
    for stage in results:
        print(stage)

# SELECT avec option
with get_session() as session:
    # statement = select(Stage).where(Stage.entreprise == 'Richnou Corp') # lien vers la classe
    statement = select(Stage)\
        .where(Stage.entreprise.like("%ch%"))\
        .order_by(Stage.expedition.desc())\
        .limit(10)
    print(str(statement))
    results = session.exec(statement).all() # éxecuter + all
    for stage in results:
        print(stage)
       
with get_session() as session:
    session.add(Project(
        rubrique="vue.js",
        nom="Douglas",
        image="img/douglas.jpg",
        rendu="2024-11-15"

    ))

    session.add(Project(
        rubrique="python",
        nom="bdd",
        image="img/bdd.jpg",
        rendu="2024-12-16"

    ))
    session.commit()