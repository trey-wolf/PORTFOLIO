import kagglehub
import pandas as pd
import numpy as np
import os

# Download latest version
path = kagglehub.dataset_download("bhanupratapbiswas/superstore-sales")
print("path to dataset files:", path)

# Load the CSV file into a pandas DataFrame
csv_file = os.path.join(path, "superstore_final_dataset (1).csv")
# Try different encodings to handle potential encoding issues
try:
    df = pd.read_csv(csv_file, encoding='utf-8')
except UnicodeDecodeError:
    try:
        df = pd.read_csv(csv_file, encoding='latin1')
    except UnicodeDecodeError:
        df = pd.read_csv(csv_file, encoding='cp1252')

numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

print(f"\nDataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

print("\nData successfully loaded into arrays for processing!")

# === DATA CLEANING ANALYSIS ===
print("\n=== DATA CLEANING ANALYSIS ===")
# Remove negative values in numeric columns
def remove_negative_values(dataframe, numeric_columns):
    print("\nChecking for negative values in numeric columns...")
    for col in numeric_columns:
        if (dataframe[col] < 0).any():
            negative_count = (dataframe[col] < 0).sum()
            print(f"Column '{col}' has {negative_count} negative values. Removing these rows...")
            dataframe = dataframe[dataframe[col] >= 0]
            print(f"Negative values removed from column '{col}'. New dataset shape: {dataframe.shape}")
    print("\nNegative value check complete.")
    return dataframe
df = remove_negative_values(df, numeric_cols)

# Check and Update data types
def detect_and_fix_date_format(date_str):
    """
    Detect if a date is DD/MM/YYYY or MM/DD/YYYY and convert to MM/DD/YYYY
    """
    if pd.isna(date_str) or date_str == '':
        return pd.NaT
    
    date_str = str(date_str).strip()
    
    if '/' in date_str:
        parts = date_str.split('/')
        if len(parts) == 3:
            first, second, third = parts
            try:
                first_int = int(first)
                second_int = int(second)
                year = int(third)
                
                # Logic to determine format
                if first_int > 12:
                    # Must be DD/MM/YYYY, convert to MM/DD/YYYY
                    return pd.to_datetime(f"{second}/{first}/{year}", format='%m/%d/%Y')
                elif second_int > 12:
                    # Must be MM/DD/YYYY, keep as is
                    return pd.to_datetime(f"{first}/{second}/{year}", format='%m/%d/%Y')
                else:
                    # Ambiguous - assume MM/DD/YYYY
                    return pd.to_datetime(f"{first}/{second}/{year}", format='%m/%d/%Y')
            except:
                return pd.NaT
    
    # Try other formats
    try:
        return pd.to_datetime(date_str)
    except:
        return pd.NaT

# Apply to your date columns
def apply_date_standardization(dataframe):
    date_columns = ['Order_Date', 'Ship_Date']
    
    for col in date_columns:
        if col in dataframe.columns:
            print(f"Standardizing {col}...")
            dataframe[col] = dataframe[col].apply(detect_and_fix_date_format)
    
    return dataframe
df = apply_date_standardization(df)

def update_data_types(dataframe):
    print("\nUpdating data types...")
    print("Before update:")
    print(dataframe.dtypes)
    
    print("Data types updated.")
    # Convert 'Order_Date' to datetime
    if 'Order_Date' in dataframe.columns:
        dataframe['Order_Date'] = pd.to_datetime(dataframe['Order_Date'], errors='coerce')
    print("\nConverted Order_Date to datetime type.")
    
    # Convert 'Postal_Code' to string if not already
    if 'Postal_Code' in dataframe.columns:
        dataframe['Postal_Code'] = dataframe['Postal_Code'].astype(str)

    print("\nConverted Postal_Code to string type.")
    
    # Convert 'Ship_Date' to datetime
    if 'Ship_Date' in dataframe.columns:
        dataframe['Ship_Date'] = pd.to_datetime(dataframe['Ship_Date'], errors='coerce')
    
    print("\nConverted Ship_Date to datetime type.")
    
    # Show updated data types
    print("\nAfter update:")
    print(dataframe.dtypes)
    
    return dataframe

df = update_data_types(df)

# Check and update duplicate rows
def update_duplicate_rows(dataframe):
    duplicate_rows = dataframe.duplicated().sum()
    print(f"\nNumber of duplicate rows: {duplicate_rows}")

    if duplicate_rows > 0:
        print("\nRemoving duplicate rows...")
        dataframe.drop_duplicates(inplace=True)
        print(f"Duplicate rows removed. New dataset shape: {dataframe.shape}")
    return dataframe
df = update_duplicate_rows(df)

# Check and update missing values
def update_missing_values(dataframe):
    # Check for missing values
    missing_values = dataframe.isnull().sum()
    print(f"\nMissing values in each column:\n{missing_values[missing_values > 0]}")
    if missing_values.sum() == 0:
        print("No missing values detected.")
        return dataframe

    print("\nHandling missing values...")
    print(dataframe["Order_Date"])    
df = update_missing_values(df)

# Outlier detection and handling
def detect_and_handle_outliers(dataframe):
    numeric_columns = dataframe.select_dtypes(include=[np.number]).columns.tolist()
    print("\nDetecting outliers in numeric columns...")
    for col in numeric_columns:
        mean_val = dataframe[col].mean()
        std_val = dataframe[col].std()
        outliers = dataframe[(dataframe[col] < mean_val - 3 * std_val) | (dataframe[col] > mean_val + 3 * std_val)]
        if len(outliers) > 0:
            print(f"Outliers detected in column '{col}': {len(outliers)} rows")
            # Optionally, remove outliers
            print(f"Removing outliers from column '{col}'...")
            dataframe = dataframe[(dataframe[col] >= mean_val - 3 * std_val) & (dataframe[col] <= mean_val + 3 * std_val)]
            print(f"Outliers removed from column '{col}'. New dataset shape: {dataframe.shape}")
        else:
            print(f"No outliers detected in column '{col}'")
    print("\nOutlier detection complete.")
    return dataframe

df = detect_and_handle_outliers(df)

# === SAVE CLEANED DATASET ===
print("\n" + "="*50)
print("SAVING CLEANED DATASET")
print("="*50)

# Define output file path
output_file = os.path.join(os.path.dirname(csv_file), "superstore_dataset_cleaned.csv")

try:
    # Save the cleaned dataframe to CSV
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"✅ Cleaned dataset saved successfully!")
    print(f"📁 File location: {output_file}")
    print(f"📊 Final dataset shape: {df.shape}")
    
    # Display summary of cleaning operations
    print(f"\n📋 DATA CLEANING SUMMARY:")
    print(f"   • Negative values removed from numeric columns")
    print(f"   • Date formats standardized to MM/DD/YYYY")
    print(f"   • Data types optimized (dates, postal codes)")
    print(f"   • Duplicate rows removed")
    print(f"   • Missing values handled")
    print(f"   • Outliers detected and removed")
    
    # Final data quality check
    final_missing = df.isnull().sum().sum()
    final_duplicates = df.duplicated().sum()
    
    print(f"\n🔍 FINAL QUALITY CHECK:")
    print(f"   • Total missing values: {final_missing}")
    print(f"   • Duplicate rows: {final_duplicates}")
    print(f"   • Dataset ready for analysis: {'✅ YES' if final_missing == 0 and final_duplicates == 0 else '⚠️ REVIEW NEEDED'}")
    
except Exception as e:
    print(f"❌ Error saving cleaned dataset: {e}")
    print("Attempting to save with different encoding...")
    try:
        df.to_csv(output_file, index=False, encoding='latin1')
        print(f"✅ Cleaned dataset saved with latin1 encoding!")
        print(f"📁 File location: {output_file}")
    except Exception as e2:
        print(f"❌ Failed to save dataset: {e2}")

print(f"\n🎉 Data cleaning process completed!")
print(f"Your cleaned dataset is ready for analysis and visualization.")