from pathlib import Path

import pytest

from jptax.insurance.deduction import round_by_law, calculate_caregiving, calculate_caregiving_employee, calculate_employment, calculate_employment_employee, calculate_kids_support, InsuranceDeduction
from jptax.insurance.dataframe import read_dataframes

ROOT = Path(__file__).resolve().parent.parent.parent


def test_round_by_law_50_point_0():
    assert round_by_law(50.0) == 50

def test_round_by_law_50_point_5():
    assert round_by_law(50.5) == 50

def test_round_by_law_50_point_6():
    assert round_by_law(50.6) == 51

def test_round_by_law_50_point_9():
    assert round_by_law(50.9) == 51

def test_calculate_caregiving_grade5_and_over39():
    assert abs(calculate_caregiving(9800, 11583.6, 40) - 1783.6) < 0.1

def test_calculate_caregiving_grade5_and_under40():
    assert calculate_caregiving(9800, 11583.6, 35) == 0.0

def test_calculate_caregiving_employee_grade5_and_over39():
    assert calculate_caregiving_employee(9800, 11583.6, 40) == 1784

def test_calculate_caregiving_employee_grade5_and_under40():
    assert calculate_caregiving_employee(9800, 11583.6, 35) == 0

def test_calculate_caregiving_raise_age_error():
    with pytest.raises(ValueError, match="age: should be greater than or equal to 0."):
        calculate_caregiving_employee(9800, 11583.6, -1)

def test_calculate_caregiving_raise_health_included_caregiving_error():
    with pytest.raises(ValueError, match="health_included_caregiving: must be greater than health."):
        calculate_caregiving_employee(9800, 9800, 45)

def test_calculate_employment_700000_code1():
    assert abs(calculate_employment(700000, False, "1") - 10850) < 0.1

def test_calculate_employment_900000_code2():
    assert abs(calculate_employment(900000, False, "2") - 15750) < 0.1

def test_calculate_employment_800000_code3():
    assert abs(calculate_employment(800000, False, "3") - 14800) < 0.1

def test_calculate_employment_board_member():
    assert calculate_employment(321800, True, "1") == 0.0

def test_calculate_employment_raise_salary_error():
    with pytest.raises(ValueError, match="salary: should be greater than or equal to 0 yen and less than or equal to 1,000,000,000,000 yen."):
        calculate_employment(-1000, False, "1")

def test_calculate_employment_employee_700000_code1():
    assert calculate_employment_employee(700000, False, "1") == 4200

def test_calculate_employment_employee_900000_code2():
    assert calculate_employment_employee(900000, False, "2") == 6300

def test_calculate_employment_employee_800000_code3():
    assert calculate_employment_employee(800000, False, "3") == 5600

def test_calculate_employment_employee_board_member():
    assert calculate_employment_employee(321800, True, "1") == 0

def test_calculate_employment_employee_raise_salary_error():
    with pytest.raises(ValueError, match="salary: should be greater than or equal to 0 yen and less than or equal to 1,000,000,000,000 yen."):
        calculate_employment_employee(-1000, False, "1")

def test_calculate_kids_support():
    assert abs(calculate_kids_support(240_000) - 864.0) < 0.1

def test_calculate_kids_support_smallest():
    assert abs(calculate_kids_support(68_000) - 316.8) < 0.1

def test_calculate_kids_support_largest():
    assert abs(calculate_kids_support(880_000) - 2340.0) < 0.1

def test_calculate_kids_support_raise_salary_error():
    with pytest.raises(ValueError, match="standard_remuneration: should be greater than or equal to 0 yen and less than or equal to 1,000,000,000,000 yen."):
        calculate_kids_support(-1000)


class TestInsuranceDeductionCase1:
    """一般事業、事業所所在地が東京都、30歳、従業員、支給額510,000円、標準報酬月額500,000円、2024年3月の給与
    """

    @pytest.fixture(scope='class')
    def fixt(self) -> InsuranceDeduction:
        df_map = read_dataframes(ROOT / 'src' / 'jptax' / 'insurance' / 'tables' / 'r5ippan3.xlsx')
        return InsuranceDeduction(
            510_000, 500_000, 30, False, "13", "1", df_map
        )

    def test_health(self, fixt: InsuranceDeduction):
        assert fixt.health == 50000.0

    def test_health_employee(self, fixt: InsuranceDeduction):
        assert fixt.health_employee == 25000.0

    def test_caregiving(self, fixt: InsuranceDeduction):
        assert fixt.caregiving == 0.0

    def test_caregiving_employee(self, fixt: InsuranceDeduction):
        assert fixt.caregiving_employee == 0

    def test_pension(self, fixt: InsuranceDeduction):
        assert fixt.pension == 91500

    def test_pension_employee(self, fixt: InsuranceDeduction):
        assert fixt.pension_employee == 45750

    def test_employment(self, fixt: InsuranceDeduction):
        assert fixt.employment == 7905.0

    def test_employment_employee(self, fixt: InsuranceDeduction):
        assert fixt.employment_employee == 3060

    def test_kids_support(self, fixt: InsuranceDeduction):
        assert fixt.kids_support == 1800.0
