import pandas as pd
import sys

# Load the CSV file
input_file = sys.argv[1]
df = pd.read_csv(input_file, index_col=0)

# Create a new DataFrame to store the result
result_df = pd.DataFrame(columns=df.columns)

# Iterate through the DataFrame to aggregate the alleles with the highest probability for each position
for position, group in df.groupby(df.index.str.rsplit('_', n=1).str[0]):
    max_prob_row = group.idxmax()
    alleles = [allele.split('_')[-1] for allele in max_prob_row]
    result_df.loc[position] = alleles

# Save the result DataFrame to a CSV file
output_file = sys.argv[2]
result_df.to_csv(output_file)
