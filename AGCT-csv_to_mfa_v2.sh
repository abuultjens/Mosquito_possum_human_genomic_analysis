#!/bin/bash

INFILE=${1}
OUTFILE=${2}

# generate random prefix for all tmp files
RAND_1=$(echo $((1 + RANDOM % 100)))
RAND_2=$(echo $((100 + RANDOM % 200)))
RAND_3=$(echo $((200 + RANDOM % 300)))
RAND=$(echo "${RAND_1}${RAND_2}${RAND_3}")

# check for and rm any preexisting files
if ls ${OUTFILE} 1> /dev/null 2>&1; then
        rm ${OUTFILE}
fi

# get n of columns (taxa)
N_TAXA=$(head -1 ${INFILE} | cut -f 2- -d ',' | tr ',' '\n' | wc -l)
ONE=1

# Debugging lines
echo "N_TAXA: $N_TAXA"
echo "ONE: $ONE"

N_TAXA_PLUS_ONE=$(( ONE + N_TAXA ))
seq 2 ${N_TAXA_PLUS_ONE} > ${RAND}_list.txt

for TAXA in $(cat ${RAND}_list.txt); do
        HEAD=$(cut -f ${TAXA} -d ',' ${INFILE} | head -1)
        echo ">${HEAD}" >> ${OUTFILE}
        TAIL=$(cut -f ${TAXA} -d ',' ${INFILE} | tail -n +2 | tr '\n' ',' | tr -d ',')
        echo "${TAIL}" >> ${OUTFILE}
done

rm ${RAND}_*
