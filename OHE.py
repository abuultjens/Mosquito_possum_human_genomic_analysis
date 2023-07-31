
import pandas as pd

# Load the SNP table
df = pd.read_csv("36-VIC_W-3-seqcap-NA_noref.csv", index_col=0)

# Transpose the dataframe before one-hot encoding
df_transposed = df.transpose()

# Perform one-hot encoding
one_hot_df_transposed = pd.get_dummies(df_transposed, dummy_na=True)

# Save the one-hot encoded dataframe to a csv file
one_hot_df_transposed.to_csv('36-VIC_W-3-seqcap-NA_noref.tr.OHE.csv')
