import pandas as pd
from upgini.autofe.date import DateDiff, DateDiffFuture

from datetime import datetime
from pandas.testing import assert_series_equal


def test_date_diff():
    df = pd.DataFrame(
        [[datetime(1993, 12, 10), datetime(2022, 10, 10)], [datetime(2023, 10, 10), datetime(2022, 10, 10)]],
        columns=["date1", "date2"],
    )

    operand = DateDiff()
    expected_result = pd.Series([10531, None])
    assert_series_equal(operand.calculate_binary(df.date2, df.date1), expected_result)


def test_date_diff_future():
    df = pd.DataFrame(
        [[datetime(1993, 12, 10), datetime(2022, 10, 10)], [datetime(1993, 4, 10), datetime(2022, 10, 10)]],
        columns=["date1", "date2"],
    )

    operand = DateDiffFuture()
    expected_result = pd.Series([61.0, 182.0])
    assert_series_equal(operand.calculate_binary(df.date2, df.date1), expected_result)


def test_real():
    from upgini.autofe.feature import Feature

    df = pd.read_parquet("../ml-backend.worktrees/BACK-3250/test")
    feature = Feature.from_formula(
        "date_diff_future(date_0e8763,sber_spasibo_msisdn_ads_v2_1914333223_marketing_phone_birth_date)"
    )
    feature.op = feature.op.copy(update={"left_unit": "ms"})
    res = feature.calculate(df)
    pass
