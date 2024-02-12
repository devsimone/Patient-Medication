from sqlalchemy.orm import Session
from app import models, schemas


def create_medication_request(db: Session, request: schemas.MedicationRequestCreate):
    db_request = models.MedicationRequest(**request.dict())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)

    return db_request

