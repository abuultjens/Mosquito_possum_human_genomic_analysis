import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import sys

TRAIN = sys.argv[1]
TEST = sys.argv[2]

X_train = pd.read_csv(TRAIN, header=0, index_col=0)
X_test = pd.read_csv(TEST, header=0, index_col=0)

imp = IterativeImputer(max_iter=10, random_state=0)

# Fit the imputer and transform the test set
imp.fit(X_train)
IMPUTE = imp.transform(X_test)

# Round the imputed values to get binary output
IMPUTE_binary = np.round(IMPUTE).astype(int)

# Create a DataFrame from the imputed array, preserving column names and index
IMPUTE_df = pd.DataFrame(IMPUTE_binary, columns=X_test.columns, index=X_test.index)

# Save the DataFrame to a CSV file, including the header
IMPUTE_df.to_csv(sys.argv[3])
