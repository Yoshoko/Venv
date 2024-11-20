from fastapi import APIRouter,Request,HTTPException
from stage_class import Stage
from typing import List,Optional
router = APIRouter()

@router.get("/stages",response_model=List[Stage])
def get_allstages():
    results = Stage.get_all()
    return results

@router.get("/stages/{id}",response_model=Stage)
def get_one_stage(id:int):
    results = Stage.get_one(id=id)
    if results is None:
        raise HTTPException(status_code=404,detail="Not found")
    return results

@router.post("/stages",response_model=Stage)
async def create_stage(request:Request):
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400,detail="Data missing")

    poste = body.get("poste")
    entreprise = body.get("entreprise")
    expedition = body.get("expedition")
    url = body.get("url")

    if not poste or not entreprise :
        raise HTTPException(status_code=400,detail="Missing required fields")
    
    result = Stage.insert(
        poste=poste,
        entreprise=entreprise,
        expedition=expedition,
        url=url
    )
    return result

@router.delete("/stages/{id}",response_model=bool)
def delete_stage(id:int):
    success = Stage.delete(id)
    if not success:
        raise HTTPException(status_code=404,detail="Not Found")
    raise HTTPException(status_code=204,detail="No content")

@router.put("/stages/{id}",response_model=Stage)
async def update_project(id:int,request:Request):
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400,detail="Data missing")

    poste = body.get("poste")
    entreprise = body.get("entreprise")
    expedition = body.get("expedition")
    url = body.get("url")

    if not any([poste,entreprise,expedition]):
        raise HTTPException(status_code=400,detail="Data missing")
    
    result = Stage.update(
        id=id,
        poste=poste,
        entreprise=entreprise,
        expedition=expedition,
        url=url
    )
    if result is None:
        raise HTTPException(status_code=400,detail="Not Found")
    return result
        