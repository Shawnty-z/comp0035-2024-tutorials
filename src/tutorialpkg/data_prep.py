import pandas as pd
from pathlib import Path

def describe_dataframe(df: pd.DataFrame):
    """
    Prints information that describes the data in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): The pandas DataFrame containing data.
    
    Returns:
    None
    """
    print("Dataframe Information:")
    print(df.info())
    print("\nDataframe Description:")
    print(df.describe())

if __name__ == '__main__':
    # Define the file paths for the CSV and Excel files
    csv_file_path = Path(__file__).parent.joinpath('data', 'paralympics_events_raw.csv')
    excel_file_path = Path(__file__).parent.joinpath('data', 'paralympics_all_raw.xlsx')

    # Read the CSV file into a DataFrame
    try:
        paralympics_csv_df = pd.read_csv(csv_file_path)
        print(f"CSV data loaded successfully from {csv_file_path}")
        describe_dataframe(paralympics_csv_df)
    except FileNotFoundError:
        print(f"File not found: {csv_file_path}")
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")

    # Read the first worksheet of the Excel file into a DataFrame
    try:
        paralympics_excel_df = pd.read_excel(excel_file_path)
        print(f"Excel data (first sheet) loaded successfully from {excel_file_path}")
        describe_dataframe(paralympics_excel_df)
    except FileNotFoundError:
        print(f"File not found: {excel_file_path}")
    except Exception as e:
        print(f"An error occurred while reading the Excel file: {e}")

    # Read the second worksheet of the Excel file (medal standings) into a DataFrame
    try:
        medal_standings_df = pd.read_excel(excel_file_path, sheet_name="medal_standings")
        print("Medal standings data loaded successfully from the second sheet.")
        describe_dataframe(medal_standings_df)
    except FileNotFoundError:
        print(f"File not found: {excel_file_path}")
    except Exception as e:
        print(f"An error occurred while reading the Excel sheet: {e}")
