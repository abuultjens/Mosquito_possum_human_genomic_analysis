#!/bin/bash

FOFN=${1}
OHE_FILE=${2}
OUTFILE=${3}

head -1 ${OHE_FILE} > ${OUTFILE}

for TAXA in $(cat ${FOFN}); do

	grep ^"${TAXA}," ${OHE_FILE} >> ${OUTFILE}
	
done

		
