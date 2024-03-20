# Employee Data Processing Package

## Introduction

This Python package allows users to process employee data stored in an Excel file or a database table. It provides functionalities to filter employees based on their joining date and calculate the average salary for employees with a given designation. The package also offers logging capabilities and the ability to configure the location of log files using a config file.

## Features

- Input: Takes input from the user for the date of joining.
- Filtering: Filters employees who have joined after the given date.
- Output: Saves the filtered list of employees in a new file.
- Average Salary: Computes and prints the average salary for employees with a given designation.
- Timestamp: Appends timestamp to output and log files.
- Logging: Logs all operations, errors.
- Configurability: Allows users to configure the location of log files using a config file.

### Folder Structure

- input: Contains the main employee_details file which functions in it.
- database_connection: Stores all the sql scripts to create the database table for this project.
- tests: Contains the test script classes written for the functions created in input directory.

## Setup and Installation

### Clone the Repository

1. Clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/SaxenaSim/employee_insights.git

2. Navigate to the repository directory:
   ```bash
   cd your-repository

3. Install the required packages from the requirements.txt file:
   ```bash
   pip install -r requirements.txt


## Usage

Upon finishing the cloning of the repository, start by executing all scripts located in the db_scripts folder to configure your database in accordance with this code.

Once the package is installed, you can use the package as follows:

1. **Run the utility:**

   a. Importing the packages:
   ```bash
   import src
   from src.employee_details import Employee
   ```
   b. Creating objects:
   ```bash
   obj = Employee()
   ```
   c. Call methods or access attributes of object:
   ```bash
   result = obj.filter_employee("Enter a date in YYYY-MM-DD format")
   print(result)
   ```

## Testing

The repository includes some test cases to demonstrate the utility's functionality. You can run the test suite using pytest:

```bash
 pytest
 ```

## Code Hygiene and Pre-commit Hooks

The repository employs tools such as Black which is a code scanning tools to enforce code hygiene standards. These checks are executed automatically before each commit, typically through pre-commit hooks.

## Building the package locally

To build the package as a wheel file locally for distribution and installation, you can use the following command:

```bash
 python setup.py sdist bdist_wheel
 ```
## Releasing to PyPI

To release the package to the Python Package Index (PyPI) repository publicly for broader usage, follow these steps:

1. Sign up for an account on PyPI ([https://pypi.org/](https://pypi.org/)).
2. Install twine if not already installed:

    ```bash
    pip install twine
    ```

3. Upload your package to PyPI using twine:

    ```bash
    twine upload dist/*
    ```
