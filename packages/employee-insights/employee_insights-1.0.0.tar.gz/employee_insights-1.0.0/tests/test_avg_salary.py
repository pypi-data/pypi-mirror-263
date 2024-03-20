import pytest
from src.employee_details import Employee


class TestAvgSalary:
    @pytest.fixture
    def Employee(self):
        return Employee()

    def test_avg_salary(self, Employee):
        self.mock_designation = "Scientist"
        result = Employee.avg_salary(self.mock_designation)
        assert result == 78118.24
