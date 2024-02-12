from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from uvicorn import run
from app import crud, schemas
from sqlalchemy.exc import IntegrityError, DataError


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Health Check OK!"}


@app.post(
    "/medication-requests/",
    response_model=schemas.MedicationRequest,
    status_code=status.HTTP_201_CREATED,
)
def create_medication_request(
    request: schemas.MedicationRequestCreate, db: Session = Depends(get_db)
):
    try:
        return crud.create_medication_request(db=db, request=request)
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail="Bad request, please check your payload"
        )
    except DataError:
        raise HTTPException(status_code=400, detail="Invalid input value")


@app.get("/medication-requests/", response_model=list[schemas.MedicationRequest])
def list_medication_requests(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    try:
        return crud.get_medication_requests(db, skip=skip, limit=limit)
    except DataError:
        raise HTTPException(status_code=400, detail="Invalid input value")


if __name__ == "__main__":
    run("app.main:app", host="0.0.0.0", port=8000, reload=False)

