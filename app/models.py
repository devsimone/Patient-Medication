from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Float

Base = declarative_base()


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    sex = Column("sex", Enum("male", "female", name="sex"))


class Clinician(Base):
    __tablename__ = "clinicians"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    registration_id = Column(String)


class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String)
    code_name = Column(String)
    code_system = Column(String)
    strength_value = Column(Float)
    strength_unit = Column(String)
    form = Column("form", Enum("powder", "tablet", "capsule", "syrup", name="form"))


class MedicationRequest(Base):
    __tablename__ = "medication_requests"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    clinician_id = Column(Integer, ForeignKey("clinicians.id"))
    medication_id = Column(Integer, ForeignKey("medications.id"))
    reason_text = Column(String)
    prescribed_date = Column(Date)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    frequency = Column(String)
    status = Column(
        "status", Enum("active", "on-hold", "cancelled", "completed", name="status")
    )

    patient = relationship("Patient")
    clinician = relationship("Clinician")
    medication = relationship("Medication")