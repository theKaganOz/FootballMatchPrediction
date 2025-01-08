import os
import pandas as pd

def merge_csv_files(input_directory, output_file):
    # List to store DataFrames
    dataframes = []

    # Iterate through all files in the directory
    for filename in os.listdir(input_directory):
        # Check if the file is a CSV
        if filename.endswith(".csv"):
            file_path = os.path.join(input_directory, filename)
            # Read the CSV into a DataFrame
            df = pd.read_csv(file_path)
            # Append the DataFrame to the list
            dataframes.append(df)
            print(f"Merged: {filename}")

    # Concatenate all DataFrames
    if dataframes:
        merged_df = pd.concat(dataframes, ignore_index=True)
        # Save the merged DataFrame to the output file
        merged_df.to_csv(output_file, index=False)
        print(f"All CSV files merged into: {output_file}")
    else:
        print("No CSV files found in the directory.")

# Define the input directory and output file
input_dir = r"C:\Users\kagan\SpyderScripts\FootballMatchPrediction\Datasets\football-datasets-main\football-datasets-main\datasets\merged_datasets"  # Replace with your directory path
output_file = r"C:\Users\kagan\SpyderScripts\FootballMatchPrediction\Datasets\football-datasets-main\football-datasets-main\datasets\football_match_dataset.csv"        # Replace with your desired output file name

# Call the function
merge_csv_files(input_dir, output_file)
