#!/bin/bash

#fofn-checker

#FOFN=36-clinical_fofn.txt
#OHE_FILE=36-VIC_5-seqcap_full_subset.OHE_v3.csv
#OUTFILE=36-clinical_36-VIC_5-seqcap_full_subset.OHE_v3.csv

FOFN=${1}
OHE_FILE=${2}
OUTFILE=${3}

head -1 ${OHE_FILE} > ${OUTFILE}

for TAXA in $(cat ${FOFN}); do

	grep ^"${TAXA}," ${OHE_FILE} >> ${OUTFILE}
	
done

		