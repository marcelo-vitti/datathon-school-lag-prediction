def get_features_for_cohort(df, cohort):
    """
    Select valid features based on cohort year.
    """
    base_features = ["IAA", "IEG", "IPS", "math", "portuguese"]

    lag_1_features = [
        "IAA__minus_1",
        "IEG__minus_1",
        "IPS__minus_1",
        "math__minus_1",
        "portuguese__minus_1",
    ]

    lag_2_features = [
        "IAA__minus_2",
        "IEG__minus_2",
        "IPS__minus_2",
        "math__minus_2",
        "portuguese__minus_2",
    ]

    if cohort == 1:
        return base_features

    if cohort == 2:
        return base_features + lag_1_features

    if cohort == 3:
        return base_features + lag_1_features + lag_2_features

    raise ValueError("Invalid cohort")
