import pytest
from src.employee_details import Employee
import os


class TestSaveData:
    @pytest.fixture
    def Employee(self):
        return Employee()

    def test_save_data_file(self, Employee):
        mock_data = "This is my sample data"
        file = Employee.save_data_to_file(mock_data)
        assert os.path.exists(file)
