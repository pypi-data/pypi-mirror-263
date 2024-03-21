import math
from functools import cached_property

import pandas as pd

from jptax.insurance.definitions import pref_code


def round_by_law(v: float) -> int:
    """50銭以下のときは切り捨て、50銭1厘以上のときは切上

    Args:
        v (float): 端数を含む数

    Returns:
        int: 端数を含まない数
    """
    return math.floor(v + 0.49)


def calculate_caregiving(health: float, health_included_caregiving: float, age: int) -> float:
    """介護保険料を算出する

    Args:
        health (float): 健康保険料
        health_included_caregiving (float): 第２号被保険者 健康保険料
        age (int): 年齢

    Returns:
        float: 介護保険料
    """
    if age < 0:
        raise ValueError("age: should be greater than or equal to 0.")
    if health_included_caregiving <= health:
        raise ValueError("health_included_caregiving: must be greater than health.")
    if age < 40:
        return 0.0
    else:
        return health_included_caregiving - health


def calculate_caregiving_employee(health: float, health_included_caregiving: float, age: int) -> int:
    """介護保険料（従業員負担分）を算出する

    Args:
        health (float): 健康保険料
        health_included_caregiving (float): 第２号被保険者 健康保険料
        age (int): 年齢

    Returns:
        int: 介護保険料
    """
    return round_by_law(calculate_caregiving(health, health_included_caregiving, age))


def calculate_employment(salary: int, is_board: bool, business: str) -> float:
    """雇用保険料を算出する

    Args:
        salary (int): 給与
        is_board (bool): 役員である
        business (str): 事業

    Returns:
        float: 雇用保険料
    """
    if salary < 0 or salary > 1_000_000_000_000:
        raise ValueError("salary: should be greater than or equal to 0 yen and less than or equal to 1,000,000,000,000 yen.")

    if is_board:
        return 0.0

    match business:
        case "1": # 一般の事業
            return (salary * (15.5 / 1_000))
        case "2": # 農林水産・清酒製造の事業
            return (salary * (17.5 / 1_000))
        case "3": # 建設の事業
            return (salary * (18.5 / 1_000))
        case _:
            raise IndexError("business: must be a value between 1 and 3.")


def calculate_employment_employee(salary: int, is_board: bool, business: str) -> int:
    """雇用保険料（従業員負担分）を算出する

    Args:
        salary (int): 給与
        is_board (bool): 役員である
        business (str): 事業

    Returns:
        int: 雇用保険料
    """
    if salary < 0 or salary > 1_000_000_000_000:
        raise ValueError("salary: should be greater than or equal to 0 yen and less than or equal to 1,000,000,000,000 yen.")

    if is_board:
        return 0

    # 50銭以下のときは切り捨て、50銭1厘以上のときは切上
    match business:
        case "1": # 一般の事業
            return round_by_law(salary * (6 / 1_000))
        case "2": # 農林水産・清酒製造の事業
            return round_by_law(salary * (7 / 1_000))
        case "3": # 建設の事業
            return round_by_law(salary * (7 / 1_000))
        case _:
            raise IndexError("business: must be a value between 1 and 3.")


def calculate_kids_support(standard_remuneration: int) -> float:
    """子ども・子育て拠出金を算出する

    Args:
        standard_remuneration (int): 標準報酬月額

    Returns:
        float: 子ども・子育て拠出金
    """
    if standard_remuneration < 0 or standard_remuneration > 1_000_000_000_000:
        raise ValueError("standard_remuneration: should be greater than or equal to 0 yen and less than or equal to 1,000,000,000,000 yen.")

    if standard_remuneration <= 93_000:
        return 88_000 * (3.6 / 1000)
    elif standard_remuneration >= 635_000:
        return 650_000 * (3.6 / 1000)
    else:
        return standard_remuneration * (3.6 / 1000)


class InsuranceDeduction:
    def __init__(self, salary: int, standard_remuneration: int, age: int, is_board: bool, pref: str, business: str, df_map: dict[str, pd.DataFrame]):
        self._salary = salary
        self._standard_remuneration = standard_remuneration
        self._age = age
        self._is_board = is_board
        self._pref = pref
        self._business = business
        self._df_map = df_map

    @cached_property
    def row(self) -> pd.Series:
        if self._standard_remuneration < 58_000 or self._standard_remuneration > 1_390_000:
            raise ValueError("standard_remuneration: should be greater than or equal to 58,000 yen and less than or equal to 1,390,000 yen.")
        if not self._pref in list(pref_code.values()):
            raise IndexError("pref: must be a value between 1 and 47.")

        # 対象のレコードを取得
        df = self._df_map[self._pref]
        b_index = (self._standard_remuneration >= df['円以上']) & (self._standard_remuneration < df['円未満'])
        return df.loc[b_index].iloc[0]

    @cached_property
    def health(self) -> float:
        """
        Returns:
            float: 健康保険料 全額
        """
        return float(self.row['健康保険料 全額'])

    @cached_property
    def health_employee(self) -> int:
        """
        Returns:
            int: 健康保険料 従業員負担分
        """
        return int(self.row['健康保険料 折半額'])

    @cached_property
    def caregiving(self) -> float:
        """
        Returns:
            float: 介護保険料 全額
        """
        health = float(self.row['健康保険料 全額'])
        health_included_caregiving = float(self.row['第２号被保険者 健康保険料 全額'])
        return calculate_caregiving(health, health_included_caregiving, self._age)

    @cached_property
    def caregiving_employee(self) -> int:
        """
        Returns:
            int: 介護保険料 従業員負担分
        """
        health = float(self.row['健康保険料 折半額'])
        health_included_caregiving = float(self.row['第２号被保険者 健康保険料 折半額'])
        return calculate_caregiving_employee(health, health_included_caregiving, self._age)

    @cached_property
    def pension(self) -> int:
        """
        Returns:
            int: 厚生年金保険料 全額
        """
        return int(self.row['厚生年金保険料 全額'])

    @cached_property
    def pension_employee(self) -> int:
        """
        Returns:
            int: 厚生年金保険料 従業員負担分
        """
        return int(self.row['厚生年金保険料 折半額'])

    @cached_property
    def employment(self) -> float:
        """
        Returns:
            float: 雇用保険料 全額
        """
        return calculate_employment(self._salary, self._is_board, self._business)

    @cached_property
    def employment_employee(self) -> int:
        """
        Returns:
            int: 雇用保険料 従業員負担分
        """
        return calculate_employment_employee(self._salary, self._is_board, self._business)

    @cached_property
    def kids_support(self) -> float:
        """
        Returns:
            float: 子ども・子育て拠出金
        """
        return calculate_kids_support(self._standard_remuneration)
