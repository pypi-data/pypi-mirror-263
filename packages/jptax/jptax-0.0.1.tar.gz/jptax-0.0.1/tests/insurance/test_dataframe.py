from pathlib import Path

from jptax.insurance.dataframe import read_dataframes

ROOT = Path(__file__).resolve().parent.parent.parent


def test_read_dataframes_r5ippan3():
    df_map = read_dataframes(ROOT / 'src' / 'jptax' / 'insurance' / 'tables' / 'r5ippan3.xlsx')
    assert len(df_map) == 47
    assert "1" in df_map
    assert "47" in df_map
    assert "48" not in df_map
    df = df_map["13"]
    assert df.loc[0, "健康保険料 全額"] == 5800.0

def test_read_dataframes_r6ippan3():
    df_map = read_dataframes(ROOT / 'src' / 'jptax' / 'insurance' / 'tables' / 'r6ippan3.xlsx')
    assert len(df_map) == 47
    assert "1" in df_map
    assert "47" in df_map
    assert "48" not in df_map
    df = df_map["13"]
    assert df.loc[0, "健康保険料 全額"] == 5788.4
