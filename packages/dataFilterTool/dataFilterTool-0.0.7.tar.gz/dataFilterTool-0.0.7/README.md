<!-- # DataFilterTool Package

The **DataFilterTool** package is a Python utility that provides functions to filter employee data based on joining date and calculate the average salary for a given designation. This package can be downloaded from PyPi and integrated into your projects.

## Installation

You can install the **DataFilterTool** package using pip:

```bash
pip install dataFilterTool
```

## Features

- **Filter Employees by Joining Date**: Take input from the user for the date of joining and filter all employees who joined after the specified date. The filtered list is saved in a new file.

- **Calculate Average Salary by Designation**: Take the designation as input and calculate the average salary for employees with that designation. The result is printed in an output file with a timestamp.

- **File Organization**: The package includes separate folders for input, output, and logs. Every time a new file is created in the output and logs folders, it is appended with a timestamp.

- **Configuration Support**: Utilizes a config file to define the location of log files, allowing for easy customization and management.

## Project Structure

The **DataFilterTool** package has the following structure:

- **dataFilterTool**: Package directory containing the core functionality.
  - **filter_by_date.py**: Module to filter employees by joining date.
  - **avg_sal_by_des.py**: Module to calculate average salary by designation.
  - **config.py**: Configuration file to define the location of log files.
  - **version.py**: File to store the package version information.
- **input**: Directory to store input files.
- **output**: Directory to store output files.
- **logs**: Directory to store log files.
- **tests**: Directory containing unit tests for the package.
- **scripts**: Directory containing additional scripts for data generation.
- **setup.py**: Script for package installation.
- **MANIFEST.py**: Manifest file for package distribution.

## Usage

Here's a basic example of how to use the package:

```python
from dataFilterTool.filter_by_date import filter_by_date
from dataFilterTool.avg_sal_by_des import average_salary_by_designation

# Filter employees by joining date
date_input = input("Enter the date of joining (YYYY-MM-DD): ")
filter_by_date(date_input)

# Calculate average salary by designation
designation = input("Enter the designation: ")
average_salary_by_designation(designation)
```

## Contribution and Support

Contributions to the **DataFilterTool** package are welcome. Feel free to submit bug reports, feature requests, or pull requests on the [GitHub repository](https://github.com/Lavanay-nrg/dataFilterTool).

For support or inquiries, please contact us at support@datafiltertool.com.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Lavanya-nrg/dataFilterTool/blob/main/LICENSE) file for details.

---

Thank you for using the **DataFilterTool** package! We hope it helps simplify your data filtering and analysis tasks. -->

## DataFilterTool

DataFilterTool is a Python package designed to facilitate filtering and analyzing employee data. It offers functionality to filter employees based on their date of joining and to calculate the average salary for a given designation. This package is suitable for use in various data analysis and human resources applications.

## Features

- Filter employees based on the date of joining.
- Calculate the average salary for a given designation.
- Organize input, output, and log files in separate directories.
- Append timestamps to output and log files for tracking.
- Utilize a configuration file to define the location of log files.

## Installation

You can install DataFilterTool from PyPI using pip:

```bash
pip install DataFilterTool
```

## Usage

### Filtering Employees

To filter employees based on their date of joining, use the `filter_by_date` function. This function takes the date of joining as input and saves the filtered list of employees in a new file in the output directory.

```python
from DataFilterTool.filter_by_date import filter_by_date

# Example usage
date_of_joining = "2022-01-01"
filter_by_date(date_of_joining)
```

### Calculating Average Salary

To calculate the average salary for a given designation, use the `average_salary_by_designation` function. This function takes the designation as input and prints the average salary for that designation in an output file with a timestamp.

```python
from DataFilterTool.avg_sal_by_des import average_salary_by_designation

# Example usage
designation = "Manager"
average_salary_by_designation(designation)
```

### Configuration

You can customize the location of log files by modifying the configuration file (`config.py`). This allows you to specify the path to the log directory relative to the root user.

## File Structure

```
dataFilterTool/
|-- init.py
|-- dataenv/
|-- DataFilterTool/
|   |-- __init__.py
|   |-- filter_by_date.py
|   |-- avg_sal_by_des.py
|   |-- config.py
|   |-- version.py
|-- .github/
|   |-- workflows/
|-- dataFilter_config/
|-- |-- init.py
|-- |-- config.ini
|-- input/
|   |-- employee_data.xlsx 
|-- output/
|   |-- average_salary_output.txt
|   |-- filtered_output_{timestamp}.xlsx
|-- logs/
|   |-- filtered_logs_{timestamp}.txt
|-- tests/
|   |-- test_filter_functions.py
|   |-- test_average_salary_functions.py
|-- scripts/
|   |-- data_generation.py
|-- setup.py
|-- MANIFEST.py
|-- README.md
|-- requirements.txt
```

## Contributing

Contributions to DataFilterTool are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.