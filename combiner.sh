#!/bin/bash

#fofn-checker

#FOFN=36-clinical_fofn.txt
#OHE_FILE=36-VIC_5-seqcap_full_subset.OHE_v3.csv
#OUTFILE=3-seqcap_36-clinical_36-VIC_5-seqcap_full_subset.OHE_v3.csv

OHE_FILE=${1}
IMPUTE_FILE=${2}
OUTFILE=${3}

# generate random prefix for all tmp files
RAND_1=`echo $((1 + RANDOM % 100))`
RAND_2=`echo $((100 + RANDOM % 200))`
RAND_3=`echo $((200 + RANDOM % 300))`
RAND=`echo "${RAND_1}${RAND_2}${RAND_3}"`

tail -n +2 ${OHE_FILE} > ${RAND}_${OUTFILE}

cat ${IMPUTE_FILE} > ${RAND}_TMP_${OUTFILE}
cat ${RAND}_${OUTFILE} >> ${RAND}_TMP_${OUTFILE}

# transpose matrix
tr ',' '\t' < ${RAND}_TMP_${OUTFILE} | datamash transpose -H | tr '\t' ',' > ${OUTFILE}

#rm ${RAND}_${OUTFILE}
#rm ${RAND}_TMP_${OUTFILE}


		