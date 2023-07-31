import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle
from sklearn import metrics

from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import classification_report, confusion_matrix

from sklearn.ensemble import RandomForestClassifier

import sys

IMPUTED = sys.argv[1]
ORIGINAL = sys.argv[2]
#LABELS = sys.argv[3]
PREFIX = sys.argv[3]

INDEX_df = pd.read_csv("INDEX_ALL_IMPUTED.csv", header=0, index_col=None)
IMPUTED_df = pd.read_csv(IMPUTED, header=0, index_col=None)
ORIGINAL_df = pd.read_csv(ORIGINAL, header=0, index_col=None)

# List of strings to exclude
exclude_list = [
    'CP085200_16896_C',
    'CP085200_16896_T',
    'CP085200_413419_A',
    'CP085200_413419_G',
    'CP085200_593567_C',
    'CP085200_593567_T',
    'CP085200_720080_C',
    'CP085200_720080_G',
    'CP085200_801361_C',
    'CP085200_801361_T',
    'CP085200_869371_C',
    'CP085200_869371_G',
    'CP085200_916542_C',
    'CP085200_916542_T',
    'CP085200_918743_A',
    'CP085200_918743_T',
    'CP085200_1181588_C',
    'CP085200_1181588_T',
    'CP085200_1223972_C',
    'CP085200_1223972_T',
    'CP085200_1249660_A',
    'CP085200_1249660_G',
    'CP085200_1461583_C',
    'CP085200_1461583_G',
    'CP085200_1501558_C',
    'CP085200_1501558_T',
    'CP085200_1600648_A',
    'CP085200_1600648_G',
    'CP085200_2099679_C',
    'CP085200_2099679_G',
    'CP085200_2471485_C',
    'CP085200_2471485_G',
    'CP085200_2849882_A',
    'CP085200_2849882_G',
    'CP085200_3151421_A',
    'CP085200_3151421_G',
    'CP085200_3189720_C',
    'CP085200_3189720_T',
    'CP085200_3299889_A',
    'CP085200_3299889_G',
    'CP085200_3728996_A',
    'CP085200_3728996_G',
    'CP085200_3852669_G',
    'CP085200_3852669_T',
    'CP085200_4101860_C',
    'CP085200_4101860_T',
    'CP085200_4585132_C',
    'CP085200_4585132_T',
    'CP085200_5132023_A',
    'CP085200_5132023_G',
    'CP085200_5412286_C',
    'CP085200_5412286_G',
    'CP085200_5442563_C',
    'CP085200_5442563_T',
    'CP085200_5515487_A',
    'CP085200_5515487_G',
    'CP085200_5523110_C',
    'CP085200_5523110_G',
    'CP085200_508429_G',
    'CP085200_586474_C',
    'CP085200_586815_C',
    'CP085200_607871_C',
    'CP085200_1258987_A',
    'CP085200_1307238_A',
    'CP085200_1326356_A',
    'CP085200_1443791_C',
    'CP085200_1517690_C',
    'CP085200_1644645_C',
    'CP085200_1913146_C',
    'CP085200_1919491_G',
    'CP085200_2290727_T',
    'CP085200_3171526_C',
    'CP085200_3287521_A',
    'CP085200_3602545_T',
    'CP085200_4063873_G',
    'CP085200_4420786_G',
    'CP085200_4486687_G',
    'CP085200_4927490_C',
    'CP085200_5081778_G',
    'CP085200_5289654_T',
]

df = pd.concat([INDEX_df, IMPUTED_df, ORIGINAL_df], axis=1)
df.set_index(df.columns[0], inplace=True)

df = df[~df.index.str.startswith(tuple(exclude_list))]

#ACCURACY = accuracy_score(IMPUTED_df, ORIGINAL_df)
ACCURACY = accuracy_score(df.iloc[:, 0] , df.iloc[:, 1])
print(ACCURACY)
#ACCURACY.to_csv("%s_accuracy.csv" % PREFIX, ACCURACY, delimiter=",", fmt="%s")

CM = confusion_matrix(IMPUTED_df, ORIGINAL_df)
print(CM)
np.savetxt("%s_confusion_matrix.csv" % PREFIX, CM, delimiter=",", fmt="%s")