import pandas as pd
import numpy as np
import sys

# load the dataset
df = pd.read_csv(sys.argv[1], index_col=0)

# Transpose the dataframe before one-hot encoding
df_transposed = df.transpose()

# Create an empty DataFrame to store the one-hot encoded data
one_hot_df_transposed = pd.DataFrame(index=df_transposed.index)

# Iterate through the columns of the transposed DataFrame to perform custom one-hot encoding
for col in df_transposed.columns:
    unique_values = df_transposed[col].unique()
    # Skip encoding for 'N' alleles
    unique_values = [val for val in unique_values if val != 'N']
    for unique_value in unique_values:
        new_col_name = f"{col}_{unique_value}"
        one_hot_df_transposed[new_col_name] = (df_transposed[col] == unique_value).astype(int)
    # Set to 'nan' where 'N' allele is present
    if 'N' in df_transposed[col].unique():
        n_indices = df_transposed[df_transposed[col] == 'N'].index
        for unique_value in unique_values:
            new_col_name = f"{col}_{unique_value}"
            one_hot_df_transposed.loc[n_indices, new_col_name] = np.nan

# Replace empty cells with 'nan'
one_hot_df_transposed.replace(np.nan, 'nan', inplace=True)

# Save the modified DataFrame to a CSV file
one_hot_df_transposed.to_csv(sys.argv[2])
