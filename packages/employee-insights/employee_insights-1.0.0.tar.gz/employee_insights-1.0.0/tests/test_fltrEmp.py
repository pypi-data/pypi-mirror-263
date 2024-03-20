import pytest, pandas as pd
from src.employee_details import Employee


class TestFltrEmp:
    @pytest.fixture
    def Employee(self):
        return Employee()

    def test_fltrEmp_len(self, Employee):
        mock_date = "1990-07-21"
        mock_df = pd.DataFrame()
        mock_df = Employee.filter_employee(mock_date)
        assert len(mock_df) > 0

    def test_fltrEmp_data(self, Employee):
        mock_date = "1990-07-21"
        mock_df = pd.DataFrame()
        mock_df = Employee.filter_employee(mock_date)
        assert "EMP007" in mock_df["emp_code"].values
