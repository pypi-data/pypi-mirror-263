import pytest
from src.employee_details import Employee
import os


class TestSaveAvg:
    @pytest.fixture
    def Employee(self):
        return Employee()

    def test_save_avg_file(self, Employee):
        mock_designation = "designation"
        mock_salary = "salary"
        file = Employee.save_avg_to_file(mock_designation, mock_salary)
        assert os.path.exists(file)
