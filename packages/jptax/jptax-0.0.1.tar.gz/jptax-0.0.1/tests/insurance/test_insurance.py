from datetime import date

import pytest

from jptax.insurance import Insurance


class TestInsurance:
    def test_calculate_case1(self):
        """一般事業、事業所所在地が東京都、30歳、従業員、支給額510,000円、標準報酬月額500,000円、2024年2月の給与
        """
        dt = date(2024, 2, 29)
        insurance = Insurance(dt)
        deduction = insurance.calculate(510_000, 500_000, 30, False, "13", "1")
        assert deduction.health == 50000.0
        assert deduction.health_employee == 25000

    def test_calculate_case2(self):
        """一般事業、事業所所在地が東京都、30歳、従業員、支給額510,000円、標準報酬月額500,000円、2024年3月の給与
        """
        dt = date(2024, 3, 31)
        insurance = Insurance(dt)
        deduction = insurance.calculate(510_000, 500_000, 30, False, "13", "1")
        assert deduction.health == 49900.0
        assert deduction.health_employee == 24950

    def test_calculate_case3(self):
        """2023年2月の給与
        """
        dt = date(2023, 2, 28)
        with pytest.raises(ValueError, match="dt: must be a date newer than 02/28/2023."):
            Insurance(dt)
