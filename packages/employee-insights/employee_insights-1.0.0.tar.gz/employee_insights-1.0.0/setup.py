from setuptools import setup, find_packages

setup(
    name="employee_insights",
    version="1.0.0",
    author="Simran",
    author_email="simran.saxena@dataverze.ai",
    description="This package is used to get the employee details like employees whose date_of_joining is greater than input date_of_joining and average salary of empolyees of a particular designation.",
    packages=find_packages(),
    install_requires=[
        "black==24.3.0",
        "pytest==8.0.2",
        "setuptools==69.1.1",
        "wheel==0.42.0",
        "twine==5.0.0",
        "pre-commit==3.6.2",
        "mysql-connector-python==8.3.0",
        "pandas==2.2.1",
        "pandasql==0.7.3",
    ],
    #package_data={'employee_insights': ['configuration/*']},
    #package_data={'employee_insights': ["output/*", "logs/*", "configuration/*"]},
    #package_data={'employee_insights':[config]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
