"""
Example usage of the School Lag Prediction API
"""

import requests
import json

BASE_URL = "http://localhost:8000"


def example_cohort_1():
    """Example: Prediction for cohort 1 (current year only) - Student WITHOUT lag"""
    print("=" * 50)
    print("Cohort 1 Example (Current year only)")
    print("Student performing well - Expected: NO LAG")
    print("=" * 50)

    data = {
        "years": 1,
        "IAA": 9.0,
        "IEG": 8.8,
        "IPS": 8.5,
        "math": 8.9,
        "portuguese": 9.2,
    }

    print(f"Request: {json.dumps(data, indent=2)}")
    response = requests.post(f"{BASE_URL}/predict", json=data)
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def example_cohort_2():
    """Example: Prediction for cohort 2 (current year + 1-year lag) - Student WITH lag"""
    print("=" * 50)
    print("Cohort 2 Example (Current year + 1-year lag)")
    print("Student with declining performance - Expected: LAG")
    print("=" * 50)

    data = {
        "years": 2,
        "IAA": 5.2,
        "IEG": 4.8,
        "IPS": 5.5,
        "math": 4.5,
        "portuguese": 5.1,
        "IAA__minus_1": 7.5,
        "IEG__minus_1": 7.8,
        "IPS__minus_1": 7.6,
        "math__minus_1": 7.2,
        "portuguese__minus_1": 7.9,
    }

    print(f"Request: {json.dumps(data, indent=2)}")
    response = requests.post(f"{BASE_URL}/predict", json=data)
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def example_cohort_3():
    """Example: Prediction for cohort 3 (current year + 1-year lag + 2-year lag) - Student WITHOUT lag"""
    print("=" * 50)
    print("Cohort 3 Example (Current + 1-year lag + 2-year lag)")
    print("Student with consistent strong performance - Expected: NO LAG")
    print("=" * 50)

    data = {
        "years": 3,
        "IAA": 8.7,
        "IEG": 8.9,
        "IPS": 8.4,
        "math": 8.6,
        "portuguese": 8.8,
        "IAA__minus_1": 8.5,
        "IEG__minus_1": 8.7,
        "IPS__minus_1": 8.2,
        "math__minus_1": 8.4,
        "portuguese__minus_1": 8.6,
        "IAA__minus_2": 8.3,
        "IEG__minus_2": 8.5,
        "IPS__minus_2": 8.0,
        "math__minus_2": 8.2,
        "portuguese__minus_2": 8.4,
    }

    print(f"Request: {json.dumps(data, indent=2)}")
    response = requests.post(f"{BASE_URL}/predict", json=data)
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def get_health():
    """Check API health"""
    print("=" * 50)
    print("Health Check")
    print("=" * 50)
    response = requests.get(f"{BASE_URL}/health")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


def get_features(cohort):
    """Get features for specific cohort"""
    print("=" * 50)
    print(f"Features for Cohort {cohort}")
    print("=" * 50)
    response = requests.get(f"{BASE_URL}/features/{cohort}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")


if __name__ == "__main__":
    print("\nStarting API examples...\n")

    # Check health first
    try:
        get_health()
        get_features(1)
        get_features(2)
        get_features(3)

        # Examples from each cohort
        example_cohort_1()
        example_cohort_2()
        example_cohort_3()

        print("All examples completed successfully!")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Make sure the server is running.")
        print("Run: python main.py")
