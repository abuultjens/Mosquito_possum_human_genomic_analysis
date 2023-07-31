#!/bin/bash

#fofn-checker

OUTFILE=ALL_IMPUTED_default-RFC_RAND-UPSAMPLE.csv




# generate random prefix for all tmp files
RAND_1=`echo $((1 + RANDOM % 100))`
RAND_2=`echo $((100 + RANDOM % 200))`
RAND_3=`echo $((200 + RANDOM % 300))`
RAND=`echo "${RAND_1}${RAND_2}${RAND_3}"`

for NA_POS in $(cat 117_POS.txt); do

	echo "${NA_POS}"

	# for each NA make a fofn
	tr ',' '\t' < 36-VIC_noref.tr.OHE_WO-NA.csv | datamash transpose -H | grep "${NA_POS}" | cut -f 1 > ${NA_POS}_fofn_${RAND}.txt

	for POS_ALLELE in $(cat ${NA_POS}_fofn_${RAND}.txt); do

		# make labels file for that pos
		tr ',' '\t' < 36-VIC_noref.tr.OHE_WO-NA.csv | datamash transpose -H | grep "${POS_ALLELE}" | datamash transpose -H > ${POS_ALLELE}_labels_${RAND}.csv

		python ML.py 36-VIC_noref.tr.OHE_WO-NA.csv 3-seqcap-NA_noref.tr.OHE_WO-NA_SAME-NA-AS-MOZZIE.csv ${POS_ALLELE}_labels_${RAND}.csv ${POS_ALLELE}_${RAND}
		
		datamash transpose -H < ${POS_ALLELE}_${RAND}_imputed_allele.csv > ${POS_ALLELE}_${RAND}_imputed_allele.tr.csv
		
		LINE=`cat ${POS_ALLELE}_${RAND}_imputed_allele.tr.csv | tr '\t' ','`
		
		echo "${POS_ALLELE},${LINE}" >> ${OUTFILE}

		rm ${POS_ALLELE}_${RAND}_imputed_allele.csv
		rm ${POS_ALLELE}_${RAND}_imputed_allele.tr.csv
		rm ${POS_ALLELE}_labels_${RAND}.csv
		
	done

	rm ${NA_POS}_fofn_${RAND}.txt

done

		