"""Configuration and constants for the prediction API."""

# Define feature sets for each cohort
FEATURE_SETS = {
    1: ["IAA", "IEG", "IPS", "math", "portuguese"],
    2: [
        "IAA",
        "IEG",
        "IPS",
        "math",
        "portuguese",
        "IAA__minus_1",
        "IEG__minus_1",
        "IPS__minus_1",
        "math__minus_1",
        "portuguese__minus_1",
    ],
    3: [
        "IAA",
        "IEG",
        "IPS",
        "math",
        "portuguese",
        "IAA__minus_1",
        "IEG__minus_1",
        "IPS__minus_1",
        "math__minus_1",
        "portuguese__minus_1",
        "IAA__minus_2",
        "IEG__minus_2",
        "IPS__minus_2",
        "math__minus_2",
        "portuguese__minus_2",
    ],
}

SUPPORTED_COHORTS = [1, 2, 3]
