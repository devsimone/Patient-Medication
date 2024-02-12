from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from config import settings
from app.database import get_db
from app.models import Base, Patient, Clinician, Medication, MedicationRequest
from datetime import date

SQLALCHEMY_DATABASE_URL = (f"{settings.driver_name}://{settings.database_username}:{settings.database_password}@"
                           f"{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test")
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture()
def test_patient(session):
    patient = Patient(
        first_name="john",
        last_name="Patient",
        date_of_birth=date(1993, 0o6, 13),
        sex="male",
    )
    session.add(patient)
    session.commit()
    return patient


@pytest.fixture()
def test_clinician(session):
    clinician = Clinician(
        first_name="Laura", last_name="Clinician", registration_id="047383"
    )
    session.add(clinician)
    session.commit()
    return clinician


@pytest.fixture()
def test_medication(session):
    medication = Medication(
        code="123456",
        code_name="TestMed",
        code_system="SNOMED",
        strength_value=5,
        strength_unit="mg",
        form="tablet",
    )
    session.add(medication)
    session.commit()
    return medication


@pytest.fixture()
def medication_request(session, test_patient, test_clinician, test_medication):
    med_request = MedicationRequest(
        patient_id=test_patient.id,
        clinician_id=test_clinician.id,
        medication_id=test_medication.id,
        reason_text="Example reason",
        prescribed_date=date(2019, 12, 4),
        start_date=date(2019, 12, 4),
        end_date=date.today(),
        frequency="Three times a day",
        status="active",
    )
    session.add(med_request)
    session.commit()
    return med_request
