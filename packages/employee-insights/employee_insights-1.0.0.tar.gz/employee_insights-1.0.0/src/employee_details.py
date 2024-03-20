import yaml, mysql.connector, logging, logging.config
from datetime import datetime
import pandas as pd
import os


class Employee:
    def __init__(self):

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root_dir = os.path.dirname(current_dir)
        config_dir = os.path.join(project_root_dir, 'configuration')
        config_file_path = os.path.join(config_dir,'config.yaml')
        config_logging_path = os.path.join(config_dir,"logging_config.yaml")
        
        # Load database configuration from YAML file and establish connection
        with open(config_file_path, "r") as config_file:
            # Read database configuration parameters from YAML file
            self.db_config = yaml.safe_load(config_file)
        # Establish a connection to the MySQL database using the retrieved configuration
        self.conn = mysql.connector.MySQLConnection(
            user=self.db_config["database"]["user"],
            password=self.db_config["database"]["password"],
            host=self.db_config["database"]["host"],
            port=self.db_config["database"]["port"],
            database=self.db_config["database"]["database"],
        )
        
        # Load logging configuration from YAML file and configure logging
        with open(config_logging_path, "r") as f:
            # Read logging configuration parameters from YAML file
            self.logging_config = yaml.safe_load(f)
        # Configure logging using the retrieved configuration
        logging.config.dictConfig(self.logging_config)
        
        # Initialize logger and employee DataFrame
        self.logger = logging.getLogger("file_size_logger")
        self.employee_df = pd.DataFrame()
        # Create DataFrame containing employee data
        self.create_dataframe()
        
    """
    Creates a Pandas DataFrame containing employee data from the database.

    This method executes a SQL query to retrieve all columns and records from the 'employee' table
    in the database connected through 'conn'. The retrieved data is then loaded into a Pandas DataFrame,
    which is stored in the 'employee_df' attribute of the class instance.

    """

    def create_dataframe(self):
        self.employee_df = pd.read_sql_query("SELECT * FROM employee", self.conn)

    """
    Filters the employee DataFrame based on the date of joining, returning a DataFrame 
    containing only the employees who joined after the specified input_date. 
    If successful, logs the filtered DataFrame; otherwise, logs any encountered exceptions.
    
    Args:
        input_date (str or pandas.Timestamp): The filter date in string format or as a pandas Timestamp.
    
    Returns:
        pandas.DataFrame or None: A DataFrame containing filtered employee data if successful, otherwise None.
    """

    def filter_employee(self, input_date):
        try:
            self.logger.info("::Entering into filter_employee method::")
            self.employee_df["date_of_joining"] = pd.to_datetime(
                self.employee_df["date_of_joining"]
            )
            filtered_df = self.employee_df[
                self.employee_df["date_of_joining"] > input_date
            ]
            self.logger.info("::Filtered dataframe::")
            self.logger.debug(filtered_df)
            return filtered_df
        except Exception as e:
            self.logger.info("::Entering into Filter exception::")
            self.logger.error(e)
            return None
        
    """
    Saves the employee data to a text file.

    This method takes a DataFrame of employee data as input and writes it to a text file in the 'output' directory.
    The filename is constructed with a timestamp to ensure uniqueness. If successful, the filename of the saved file is returned.

    Args:
        employees (pandas.DataFrame): DataFrame containing employee data.

    Returns:
        str or False: If successful, returns the filename of the saved file. Otherwise, returns False.
    """

    def save_data_to_file(self, employees):
        try:
            self.logger.info("::Entering into save_data_to_file method::")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            filename = f"output/filtered_employees_{timestamp}.txt"
            self.logger.debug(filename)
            self.logger.debug(timestamp)
            with open(filename, "w") as f:
                f.write(employees.to_string(index=False))
            return filename
        except Exception as e:
            self.logger.info("::Entering into save_data_to_file exception::")
            self.logger.error(e)
            return False
        
    """
    Calculates the average salary for employees with the given designation.

    This method filters the employee DataFrame based on the specified designation,
    calculates the average salary of the filtered employees, and returns the result.
    If successful, logs the filtered DataFrame and the calculated average salary.

    Args:
        designation (str): The designation for which the average salary is to be calculated.

    Returns:
        float or None: The average salary of employees with the given designation, or None if an error occurs.
    """

    def avg_salary(self, designation):
        try:
            self.logger.info(":: ENtering into avg_salary method::")
            designation_lower=designation.lower()
            filtered_df = self.employee_df[
                self.employee_df["designation"].str.lower() == designation_lower
            ]
            self.logger.info("::Filtered df::")
            self.logger.debug(filtered_df)
            average_salary = filtered_df["salary"].mean()
            self.logger.info("::average salary::")
            self.logger.debug(average_salary)
            return average_salary
        except Exception as e:
            self.logger.info("::Entering into average_salary exception")
            self.logger.error(e)
            return None
        
    """
    Saves the average salary for a given position to a text file.

    This method takes the position and its corresponding average salary as input,
    and appends this information along with a timestamp to a text file in the 'output' directory.
    If successful, returns the filename of the saved file.

    Args:
        position (str): The position for which the average salary is calculated.
        salary (float): The average salary for the specified position.

    Returns:
        str or False: If successful, returns the filename of the saved file. Otherwise, returns False.
    """

    def save_avg_to_file(self, position, salary):
        try:
            self.logger.info("::Entering into save_avg_to_file method::")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            filename = f"output/avg_salary.txt"
            self.logger.debug(filename)
            self.logger.debug(timestamp)
            with open(filename, "a") as f:
                f.write(
                    f"{timestamp}: Average Salary for the {position} is {salary:.2f}\n"
                )
            return filename
        except Exception as e:
            self.logger.info("::Entering into save_avg_to_file exception::")
            self.logger.error(e)
            return False




if __name__ == "__main__":

    input_date = input("Enter date of joining in YYYY-MM-DD format")

    obj = Employee()

    employees = obj.filter_employee(input_date)
    obj.save_data_to_file(employees)
    
    print("Want average for a particular designation(Y/N) :")
    x=input()
    if x=="Y":
        designation = input("Enter designation : ")

        salary = obj.avg_salary(designation)
        obj.save_avg_to_file(designation, salary)
    else:
        pass
