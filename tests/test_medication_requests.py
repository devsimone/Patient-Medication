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


def test_list_medication_requests_empty(client):
    response = client.get("/medication-requests/")
    assert response.json() == []
    assert response.status_code == 200


def test_list_medication_requests_non_empty(client, medication_request):
    response = client.get("/medication-requests/")
    requests = response.json()

    assert response.status_code == 200
    assert len(requests) > 0


def test_update_medication_request_valid(client, medication_request):
    response = client.patch(
        f"/medication-requests/{1}",
        json={
            "end_date": "2022-02-01",
            "frequency": "Once a day",
            "status": "completed",
        },
    )

    data = response.json()
    assert response.status_code == 200
    assert data["frequency"] == "Once a day"
    assert data["status"] == "completed"


def test_update_medication_request_invalid(client, medication_request):
    invalid_request_id = 1
    response = client.patch(
        f"/medication-requests/{invalid_request_id}",
        json={"reason_text": "No longer needed"},
    )

    data = response.json()
    assert response.status_code == 200
    assert data["frequency"] != "No longer needed"


def test_update_medication_request_invalid_id(client):
    invalid_request_id = 21
    response = client.patch(
        f"/medication-requests/{invalid_request_id}",
        json={
            "end_date": "2020-02-01",
            "frequency": "Three times a day",
            "status": "completed",
        },
    )
    assert response.status_code == 404
