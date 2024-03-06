import gzip
import pandas as pd
import os

def process_and_filter_csv(input_directory):
    # Loop through all files in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file is a gzipped file
        if filename.endswith('.gz'):
            # Construct the full file path
            file_path = os.path.join(input_directory, filename)
            
            # Open the gzipped CSV, read it into a pandas DataFrame
            with gzip.open(file_path, 'rt') as f:
                df = pd.read_csv(f, 
                                 header=None, 
                                 names=['ID', 'YEAR/MONTH/DAY', 'ELEMENT', 'DATA VALUE', 
                                        'M-FLAG', 'Q-FLAG', 'S-FLAG', 'OBS-TIME'])
                
                # Filter the DataFrame for rows where the ID starts with 'US1CA'
                filtered_df = df[df['ID'].str.startswith('US1CA')]
                
                # Create a new filename with '_clean' appended before the file extension
                clean_filename = os.path.splitext(filename)[0] + '_clean.csv'
                
                # Save the filtered DataFrame to a new CSV file
                filtered_df.to_csv(os.path.join(input_directory, clean_filename), index=False)
                
                print(f'Processed and saved: {clean_filename}')

# Example usage:
input_directory = '/Users/anthonyholmes/Github/com-sci-249-Winter24/Data/weather/'  # Update this path to where your .gz files are located
process_and_filter_csv(input_directory)
