import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

import sys

TRAIN = sys.argv[1]
TEST = sys.argv[2]
LABELS = sys.argv[3]
PREFIX = sys.argv[4]

y_train = pd.read_csv(LABELS, header=0, index_col=None)

X_test = pd.read_csv(TEST, header=0, index_col=0)
X_train = pd.read_csv(TRAIN, header=0, index_col=0)

########## upsampling

#from imblearn.over_sampling import RandomOverSampler
#ros = RandomOverSampler(sampling_strategy='auto', random_state=42)
#X_train_upsampled, y_train_upsampled = ros.fit_resample(X_train, y_train)

########## models

#from sklearn.linear_model import LogisticRegression
#clf = LogisticRegression(max_iter=1000)

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()

#from sklearn.svm import SVC
#clf = SVC()

#######################

clf.fit(X_train, y_train.values.ravel())
imputed_allele = clf.predict(X_test)

#imputed_allele.to_csv("%s_imputed_SNPs.csv" % PREFIX)
np.savetxt("%s_imputed_allele.csv" % PREFIX, imputed_allele, delimiter=",", fmt="%s")