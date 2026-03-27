from src.app import activities


def test_get_activities_returns_all_activities_with_no_store_header(client):
    # Arrange
    expected_activity_names = set(activities.keys())

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.headers["cache-control"] == "no-store"
    assert set(response.json().keys()) == expected_activity_names


def test_get_activities_returns_activity_details_and_participants(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert payload[activity_name] == {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
    }