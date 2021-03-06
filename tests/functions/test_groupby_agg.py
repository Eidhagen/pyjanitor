import pandas as pd
import pytest


@pytest.mark.functions
def test_groupby_agg():

    df = pd.DataFrame(
        {
            "date": [
                "20190101",
                "20190101",
                "20190102",
                "20190102",
                "20190304",
                "20190304",
            ],
            "values": [1, 1, 2, 2, 3, 3],
        }
    )

    df_new = df.groupby_agg(
        by="date",
        new_column="date_average",
        agg_column="values",
        agg=pd.np.mean,
    )
    assert df.shape[0] == df_new.shape[0]
    assert "date_average" in df_new.columns
    assert df_new["date_average"].iloc[0] == 1
