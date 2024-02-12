from sqlalchemy.orm import Session
from app import models, schemas


def create_medication_request(db: Session, request: schemas.MedicationRequestCreate):
    db_request = models.MedicationRequest(**request.dict())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)

    return db_request


def get_medication_requests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MedicationRequest).offset(skip).limit(limit).all()


def update_medication_request(
    db: Session, request_id: int, request: schemas.MedicationRequestUpdate
):
    db_request = (
        db.query(models.MedicationRequest)
        .filter(models.MedicationRequest.id == request_id)
        .first()
    )

    if db_request:
        update_data = request.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_request, key, value)
        db.commit()
        db.refresh(db_request)

    return db_request
