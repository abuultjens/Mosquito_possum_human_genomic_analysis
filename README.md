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
3) remove all 'NA' and 'N' alleles, eg CP085200_16896_NA and keep CP085200_16896_C (EXCEL)
4) split off the 36 clinical isolates from the 3 seq cap:
36-VIC_noref.tr.OHE_WO-NA.csv
3-seqcap-NA_noref.tr.OHE_WO-NA.csv
5) code all alleles in seqcap SNP table as '0' if that pos was NA inn the mozzie (EXCEL)
3-seqcap-NA_noref.tr.OHE_WO-NA_SAME-NA-AS-MOZZIE.csv




snippy-clean_full_aln tmp.full.aln > tmp.full.clean.aln

sh snippy_full_to_subset_csv.sh tmp.full.clean.aln tmp_fofn.txt 117_POS.csv 36-VIC_4-seqcap-mincov-1_full_subset.csv

sh impute.sh

add "CHROMOSOME_POSITION_ALLELE" to col1 header and isolate names

python imputation_to_alignment.py




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



## R analysis:

library(phytools)
library(mapdata)
Mat <- read.csv("39_lat_long.csv", header = TRUE, row.names=1)
col <- read.csv("cols.csv", header = FALSE)
tree <- ape::read.tree(text='((SRR6346362:0.068926453,(SRR6346230:0.07156821699999993,((SRR6346279:0.0,SRR6346282:0.0,SRR6346299:0.0,SRR6346304:0.0,SRR6346330:0.0,SRR6346335:0.0,SRR6346339:0.0):5.000000080634948E-9,(((SRR6346235:0.0,SRR6346239:0.0,SRR6346241:0.0,SRR6346246:0.0):0.14446433300000006,(SRR6346297:0.142544754,((DMG2212098-DMG2301551_mincov-1_ONLY_mapped-reads:0.0,DMG2300866:0.0,DMG2300867:0.0,Reference:0.0,SRR6346234:0.0,SRR6346238:0.0,SRR6346240:0.0,SRR6346243:0.0,SRR6346247:0.0,SRR6346254:0.0,SRR6346296:0.0,SRR6346303:0.0,SRR6346328:0.0,SRR6346331:0.0,SRR6346333:0.0,SRR6346336:0.0,SRR6346358:0.0,SRR6346359:0.0,SRR6346364:0.0):5.000000080634948E-9,(SRR6346374:0.06409227099999992,SRR6346280:0.06409227299999998):5.000000080634948E-9):0.0666271249999999):5.000000080634948E-9):4.999999969612645E-9,(SRR6346276:0.1469257089999999,SRR6346351:0.06662712399999993):6.000000052353016E-9):4.999999969612645E-9):6.000000052353016E-9):4.999999969612645E-9):0.295935409,(SRR6346292:0.13066600699999997,(SRR6346206:0.137474208,SRR6346340:4.999999969612645E-9):4.999999969612645E-9):0.295935409);')
obj <- phylo.to.map(ftype="off", tree,Mat,ylim=c(-40,-37), xlim=c(142,149), plot=FALSE)
plot(obj,colors=cols,ftype="off",cex.points=c(0,1.5), pts=FALSE)



```
