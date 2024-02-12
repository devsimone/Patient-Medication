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


if __name__ == "__main__":
    run("app.main:app", host="0.0.0.0", port=8000, reload=False)

