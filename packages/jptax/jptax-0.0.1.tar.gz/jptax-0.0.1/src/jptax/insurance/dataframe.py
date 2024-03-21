from pathlib import Path
import warnings

import numpy as np
import pandas as pd

from jptax.insurance.definitions import pref_code, cols, dtype


def read_dataframes(source_path: Path) -> dict[str, pd.DataFrame]:
    warnings.simplefilter("ignore")
    df_dict = pd.read_excel(
        source_path,
        sheet_name=None,
        skiprows=10,
        nrows=50,
    )
    warnings.simplefilter("default")

    ret = {}
    for k, df in df_dict.items():
        df.columns = pd.Index(cols)

        df['円以上'] = df['円以上'].fillna(0)

        index = df['厚生年金保険料 全額'].index > 35
        df.loc[index, '厚生年金保険料 全額'] = np.nan

        # 報酬の上限値を1,000,000,000,000に設定
        df['円未満'] = df['円未満'].fillna(1_000_000_000_000)

        df['厚生年金保険料 全額'] = df['厚生年金保険料 全額'].astype(np.float64)
        df['厚生年金保険料 折半額'] = df['厚生年金保険料 折半額'].astype(np.float64)

        df['厚生年金保険料 全額'] = df['厚生年金保険料 全額'].bfill()
        df['厚生年金保険料 折半額'] = df['厚生年金保険料 折半額'].bfill()
        df['厚生年金保険料 全額'] = df['厚生年金保険料 全額'].ffill()
        df['厚生年金保険料 折半額'] = df['厚生年金保険料 折半額'].ffill()

        # 従業員負担分は50銭以下のときは切り捨て、50銭1厘以上のときは切上
        df['健康保険料 折半額'] = (df['健康保険料 折半額'] + 0.49).apply(np.floor)
        df['第２号被保険者 健康保険料 折半額'] = (df['第２号被保険者 健康保険料 折半額'] + 0.49).apply(
            np.floor)

        df = df.astype(dtype)
        df = df.drop(['_'], axis=1)

        code = pref_code[k]
        ret[code] = df
    return ret
