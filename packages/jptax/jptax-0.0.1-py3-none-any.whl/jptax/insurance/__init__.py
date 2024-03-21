from pathlib import Path
from datetime import date

from jptax.insurance.dataframe import read_dataframes
from jptax.insurance.deduction import InsuranceDeduction


R5_START = date(2023, 3, 1)
R6_START = date(2024, 3, 1)
DIR_OF_PATH = Path(__file__).resolve().parent


class Insurance:
    def __init__(self, dt: date = date.today()):
        """
        Args:
            dt (date, optional): 支給日 Defaults to date.today().
        """
        if dt >= R6_START:
            self._df_map = read_dataframes(DIR_OF_PATH / 'tables' / 'r6ippan3.xlsx')
        elif dt >= R5_START:
            self._df_map = read_dataframes(DIR_OF_PATH / 'tables' / 'r5ippan3.xlsx')
        else:
            raise ValueError('dt: must be a date newer than 02/28/2023.')

    def calculate(self, salary: int, standard_remuneration: int, age: int, is_board: bool, pref: str, business: str) -> InsuranceDeduction:
        """各種社会保険料控除を計算する

        Args:
            salary (int): 支給額
            standard_remuneration (int): 標準報酬月額
            age (int): 年齢
            is_board (bool): 役員である
            pref (str): 事業所所在地の都道府県
            business (str): 事業

        Returns:
            InsuranceDeduction: 各種社会保険料控除
        """
        ret = InsuranceDeduction(salary, standard_remuneration, age, is_board, pref, business, self._df_map)
        return ret
