from pydantic import BaseModel
from typing import Optional
from datetime import date


class MedicationRequestBase(BaseModel):
    patient_id: int
    clinician_id: int
    medication_id: int
    reason_text: str
    prescribed_date: date
    start_date: date
    frequency: str
    status: str


class MedicationRequestCreate(MedicationRequestBase):
    pass


class MedicationRequestUpdate(BaseModel):
    end_date: Optional[date] = None
    frequency: Optional[str] = None
    status: Optional[str] = None


class MedicationRequest(MedicationRequestBase):
    id: int
    end_date: Optional[date] = None

    class Config:
        from_attributes = True
