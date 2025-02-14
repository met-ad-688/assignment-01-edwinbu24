import pandas as pd

# List of CSV files to process
files = ["../question_tags.csv", "../questions.csv"]  # Update paths if necessary

# Initialize a counter for lines containing "GitHub"
total_count = 0

# Iterate through each file
for file in files:
    try:
        print(f"Processing file: {file}")
        
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file)
        
        # Use vectorized operations to check for "GitHub" in all columns
        count = df.astype(str).apply(lambda col: col.str.contains("GitHub", case=False, na=False)).any(axis=1).sum()
        
        # Add to the total count
        total_count += count
        
        print(f"File: {file}, Lines containing 'GitHub': {count}")
    except Exception as e:
        print(f"Error processing file {file}: {e}")

# Print the final result
print(f"Total lines containing 'GitHub': {total_count}")