def test_create_medication_request_valid(
    client, test_patient, test_clinician, test_medication
):
    response = client.post(
        "/medication-requests/",
        json={
            "patient_id": test_patient.id,
            "clinician_id": test_clinician.id,
            "medication_id": test_medication.id,
            "reason_text": "Chronic condition",
            "prescribed_date": "2022-01-01",
            "start_date": "2022-01-02",
            "frequency": "Twice a day",
            "status": "active",
        },
    )

    data = response.json()
    assert response.status_code == 201
    assert data["frequency"] == "Twice a day"
    assert "id" in data


def test_create_medication_request_invalid_patient(
    client, test_clinician, test_medication
):
    response = client.post(
        "/medication-requests/",
        json={
            "patient_id": 58,
            "clinician_id": test_clinician.id,
            "medication_id": test_medication.id,
            "reason_text": "Invalid test",
            "prescribed_date": "2022-01-01",
            "start_date": "2022-01-02",
            "frequency": "Twice a day",
            "status": "active",
        },
    )

    assert response.status_code == 400


def test_create_medication_request_invalid_status(
    client, test_clinician, test_medication
):
    response = client.post(
        "/medication-requests/",
        json={
            "patient_id": 58,
            "clinician_id": test_clinician.id,
            "medication_id": test_medication.id,
            "reason_text": "Invalid test",
            "prescribed_date": "2022-01-01",
            "start_date": "2022-01-02",
            "frequency": "Twice a day",
            "status": "activee",
        },
    )

    assert response.status_code == 400


