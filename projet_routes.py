from fastapi import APIRouter,Request,HTTPException
from projects_model import Projet
from typing import List,Optional
router = APIRouter()

@router.get("/projets",response_model=List[Projet])
def get_allprojets():
    results = Projet.get_all()
    return results

@router.get("/projets/{id}",response_model=Projet)
def get_one_projet(id:int):
    results = Projet.get_one(id=id)
    if results is None:
        raise HTTPException(status_code=404,detail="Not found")
    return results

@router.post("/projets",response_model=Projet)
async def create_projet(request:Request):
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400,detail="Data missing")

    rubrique = body.get("rubrique")
    nom = body.get("nom")
    image = body.get("image","default.jpg")
    rendu = body.get("rendu")

    if not rubrique or not nom or not rendu:
        raise HTTPException(status_code=400,detail="Missing required fields")
    
    result = Projet.insert(
        rubrique=rubrique,
        nom=nom,
        image=image,
        rendu=rendu
    )
    return result

@router.delete("/projets/{id}",response_model=bool)
def delete_projet(id:int):
    success = Projet.delete(id)
    if not success:
        raise HTTPException(status_code=404,detail="Not Found")
    raise HTTPException(status_code=204,detail="No content")

@router.put("/projets/{id}",response_model=Projet)
async def update_project(id:int,request:Request):
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400,detail="Data missing")

    rubrique = body.get("rubrique")
    nom = body.get("nom")
    image = body.get("image")
    rendu = body.get("rendu")

    if not any([rubrique,nom,image,rendu]):
        raise HTTPException(status_code=400,detail="Data missing")
    
    result = Projet.update(
        id=id,
        rubrique=rubrique,
        nom=nom,
        image=image,
        rendu=rendu
    )
    if result is None:
        raise HTTPException(status_code=400,detail="Not Found")
    return result
        