#!/bin/bash

#fofn-checker

#IMPUTE_FILE=ALL_IMPUTED.csv
#IMPUTE_FILE=ALL_IMPUTED_default-RFC.csv
IMPUTE_FILE=$1

cut -f 1 -d ',' ${IMPUTE_FILE} > INDEX_ALL_IMPUTED.csv

cut -f 3 -d ',' ${IMPUTE_FILE} > DMG2300866_ALL_IMPUTED.csv
cut -f 4 -d ',' ${IMPUTE_FILE} > DMG2300867_ALL_IMPUTED.csv

grep "DMG2300866" 3-seqcap-NA_noref.tr.OHE_WO-NA.csv | cut -f 2- -d ',' | tr ',' '\n' > DMG2300866_ORIGINAL.csv
grep "DMG2300867" 3-seqcap-NA_noref.tr.OHE_WO-NA.csv | cut -f 2- -d ',' | tr ',' '\n' > DMG2300867_ORIGINAL.csv


echo "Evaluating DMG2300866:"

python evaluate.py DMG2300866_ALL_IMPUTED.csv DMG2300866_ORIGINAL.csv DMG2300866

echo "Evaluating DMG2300867:"

python evaluate.py DMG2300867_ALL_IMPUTED.csv DMG2300867_ORIGINAL.csv DMG2300867