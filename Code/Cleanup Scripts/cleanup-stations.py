import pandas as pd
import os

def filter_california_stations(file_path):
    # Load the file without headers. Specify dtype as str to ensure ID processing is accurate
    # Assuming the file is tab-separated; adjust 'sep' if necessary
    df = pd.read_csv(file_path, sep="\t", header=None, dtype=str)
    
    # Assuming the first column is ID and the fifth column is State (as indices 0 and 4, respectively)
    # Filter for stations in the USA (ID starts with 'US') and in California (5th column is 'CA')
    california_df = df[(df[0].str.startswith('US')) & (df[4] == 'CA')]
    
    return california_df

def process_file(file_path):
    california_stations = filter_california_stations(file_path)
    
    # Construct new filename with "_unclean" postfix
    base_name, extension = os.path.splitext(file_path)
    new_filename = f"{base_name}_unclean{extension}"
    
    # Save the filtered data. Since there were no headers, ensure headers are not written to the new file
    california_stations.to_csv(new_filename, sep="\t", index=False, header=False)
    print(f"Filtered data saved to {new_filename}")

# Example usage
file_path = '/Users/anthonyholmes/Github/com-sci-249-Winter24/Data/weather/weather-stations-worldwide-unclean.txt' 
process_file(file_path)
