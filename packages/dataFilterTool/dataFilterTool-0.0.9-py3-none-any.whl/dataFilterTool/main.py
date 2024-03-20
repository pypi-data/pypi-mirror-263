import os
import sys

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)

from dataFilterTool.join_date_filter import filter_by_date
from dataFilterTool.avg_sal_des import average_salary_by_designation


def main():
    while True:
        # Call the filter_by_date function
        date_join_str = input(
            "Enter the date (in the format YYYY-MM-DD) to filter employees: "
        )
        generated_excel_file = filter_by_date(date_join_str)
        if generated_excel_file:
            print(f"Excel file generated: {generated_excel_file}")
        else:
            print("Failed to generate Excel file.")

        # Ask if the user wants to continue entering dates
        continue_input = input("Do you want to enter designation? (yes/no): ")
        if continue_input.lower() != "yes":
            break

        # Call the average_salary_by_designation function
        designation = input("Enter the designation:")
        average_salary_by_designation(designation)

        # Ask if the user wants to continue entering designations
        continue_input = input("Do you want to enter another date? (yes/no): ")
        if continue_input.lower() != "yes":
            break


if __name__ == "__main__":
    # Create the output directory if it doesn't exist
    #output_dir = "/home/user1/Desktop/dataFilterTool/output"
    output_dir = "/home/user1/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    main()
