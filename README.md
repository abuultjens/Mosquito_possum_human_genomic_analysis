# Mozzie_possum_human_genomic_analysis
```Genomic analysis of mosquito, possum and human derived M. ulcerans genomes

## Excluding DMG2212098-DMG2301551_mincov-1_ONLY_mapped-reads:
18 SNPs with only DMG2304587_mincov-1 and DMG2304588_mincov-1
32 SNPs with only DMG2304587_mincov-1
62 SNPs with only DMG2304588_mincov-1

## Including DMG2212098-DMG2301551_mincov-1_ONLY_mapped-reads:
6 SNPs with DMG2304587_mincov-1 and DMG2304588_mincov-1
8 SNPs with DMG2304587_mincov-1
17 SNPs with DMG2304588_mincov-1

## Including DMG2212098-DMG2301551_mincov-1_ONLY_mapped-reads:
5 SNPs with DMG2304587_mincov-1_ONLY_mapped-reads_mincov-1 and DMG2304588_mincov-1_ONLY_mapped-reads_mincov-1
8 SNPs with DMG2304587_mincov-1_ONLY_mapped-reads_mincov-1
16 SNPs with DMG2304588_mincov-1_ONLY_mapped-reads_mincov-1




This is the tree that was used (/home/buultjensa/2020_Mu/snippy_v4.4.5/JKD8049):
37-VIC_POSSUM-DMG2300866_mincov-1_MOZZIE-DMG2212098-DMG2301551_mincov-1_ONLY_mapped-reads_FastTree-ML.nwk_fofn.txt
37-VIC_POSSUM-DMG2300866_mincov-1_MOZZIE-DMG2212098-DMG2301551_mincov-1_ONLY_mapped-reads_fofn.txt
There are 22 core SNPs among these isolates.

This is just the 36 VIC, without the possum and the mozzie seqs:
36-VIC_fofn.txt
Then there are 117 core SNPs (36-VIC.tab).
95 core SNPs are lost through the inclusion of the seqcap datasets.

36-VIC_W-possum-DMG2300866
122 SNPs

36-VIC_W-possum-DMG2300867
108 SNPs

When including just the 36-VIC and the two possum seqcap:
37-VIC_POSSUM-DMG2300866-DMG2300867_fofn.txt
37-VIC_POSSUM-DMG2300866-DMG2300867.tab 
There are 98 SNPs.

When all three seqcap datasets are added there are 22 core SNPs:
22_SNPs_36-VIC_3-seqcap



## steps to make the SNP tables:
1) transpose
2) one hot encoding using OHE.py
3) remove all 'NA' alleles, eg CP085200_16896_NA and keep CP085200_16896_C (EXCEL)
4) split off the 36 clinical isolates from the 3 seq cap:
36-VIC_noref.tr.OHE_WO-NA.csv
3-seqcap-NA_noref.tr.OHE_WO-NA.csv
5) code all alleles in seqcap SNP table as '0' if that pos was NA inn the mozzie (EXCEL)
3-seqcap-NA_noref.tr.OHE_WO-NA_SAME-NA-AS-MOZZIE.csv


########### Impute
# run the missing allele classifier script
sh impute.sh

# requires:
117_POS.txt
ML.py
36-VIC_noref.tr.OHE_WO-NA.csv
3-seqcap-NA_noref.tr.OHE_WO-NA_SAME-NA-AS-MOZZIE.csv

########### Evaluate
# run the evaluation script
sh evaluate.sh [ALL_IMPUTATION.csv]

# requires:
3-seqcap-NA_noref.tr.OHE_WO-NA.csv
evaluate.py

###########

Allele imputation:

# this is for core SNP sites in the possum seqcap genomes where there were no missing data between the two datasets (88 sites)
# the test feature matrix had NaN for all sites where the mozzie data was missing.


default RFC:
Evaluating DMG2300866:
0.9431818181818182
[[111   7]
 [ 10 105]]
Evaluating DMG2300867:
0.9545454545454546
[[114   4]
 [ 30  85]]

```
