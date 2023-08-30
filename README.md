# Mozzie_possum_human_genomic_analysis
Genomic analysis of mosquito, possum and human derived *Mycobacterium. ulcerans* genomes


## Missing SNP imputation:

```

# clean the snippy.full.aln
snippy-clean_full_aln tmp.full.aln > tmp.full.clean.aln

# make subset of snippy.full.clean.aln
sh snippy_full_to_subset_csv.sh tmp.full.clean.aln 36-VIC_5-seqcap_fofn.txt 117_POS.csv 36-VIC_5-seqcap_full_subset.csv

# one hot encode
python OHE_v3.py 36-VIC_5-seqcap_full_subset.csv 36-VIC_5-seqcap_full_subset.OHE_v3.csv

# split off the seqcap datasets
sh splitter.sh 5-seqcap_fofn.txt 36-VIC_5-seqcap_full_subset.OHE_v3.csv 5-seqcap_36-VIC_5-seqcap_full_subset.OHE_v3.csv

# split off the clinical isolates
sh splitter.sh 36-clinical_fofn.txt 36-VIC_5-seqcap_full_subset.OHE_v3.csv 36-clinical_36-VIC_5-seqcap_full_subset.OHE_v3.csv

# impute missing SNP alleles
python IterativeImputer.py 36-clinical_36-VIC_5-seqcap_full_subset.OHE_v3.csv 5-seqcap_36-VIC_5-seqcap_full_subset.OHE_v3.csv IMPUTE_SNPs.csv

# combine imputed alleles with the clinical isolates
sh combiner.sh 36-clinical_36-VIC_5-seqcap_full_subset.OHE_v3.csv IMPUTE_SNPs.csv 5-seqcap_36-clinical_36-VIC_5-seqcap_full_subset.OHE_v3.csv

# convert from allele by site to by site
python imputation_to_alignment.py 5-seqcap_36-clinical_36-VIC_5-seqcap_full_subset.OHE_v3.csv 5-seqcap_36-clinical_36-VIC_5-seqcap_full_subset.OHE_v3.SITES.csv

# convert from csv to multifasta alignment
sh AGCT-csv_to_mfa_v2.sh 5-seqcap_36-clinical_36-VIC_5-seqcap_full_subset.OHE_v3.SITES.csv 5-seqcap_36-clinical_36-VIC_5-seqcap_full_subset.OHE_v3.SITES.aln

# build tree
FastTree -nt -gtr 5-seqcap_36-clinical_36-VIC_5-seqcap_full_subset.OHE_v3.SITES.aln > 5-seqcap_36-clinical_36-VIC_5-seqcap_full_subset.OHE_v3.SITES.FastTree-ML.nwk

```

## R tree analysis:

```

library(phytools)
library(mapdata)
Mat <- read.csv("41_lat_long.csv", header = TRUE, row.names=1)
Mat <- as.matrix(Mat)
obj <- phylo.to.map(ftype="off", tree,Mat,ylim=c(-40,-37), xlim=c(142,149), plot=FALSE)
fofn <- read.csv("fofn.txt", header = FALSE)
fofn_mat <- as.character(as.matrix(fofn))
col <- read.csv("41_cols.csv", header = FALSE)
col_mat <- as.matrix(col)
col_mat <- as.character(col_mat)
cols<-setNames(col_mat, fofn_mat)
tree <- ape::read.tree(text='((((SRR6346297:0.06964841600000005,(SRR6346276:0.07005604999999998,(((SRR6346235:0.0,SRR6346239:0.0):4.999999969612645E-9,(SRR6346241:0.009329159000000031,SRR6346246:5.000000025123796E-9):0.009365866999999972):0.068679781,SRR6346351:0.038144220000000006):5.999999996841865E-9):0.018974668000000028):5.999999996841865E-9,(SRR6346339:0.039648983000000027,SRR6346230:0.029027137000000036):0.019029522999999993):4.999999969612645E-9,((SRR6346304:0.01891179799999998,SRR6346362:0.019063290999999982):5.000000025123796E-9,(((SRR6346282:0.0,SRR6346299:0.0,SRR6346335:0.0):5.000000025123796E-9,(SRR6346279:0.01943108199999999,SRR6346330:0.009405866999999957):0.009537969000000035):0.028604507999999973,(DMG2304588_mincov-1:0.018963604000000023,((SRR6346374:0.009401145,SRR6346336:0.009403959000000017):4.999999969612645E-9,(((SRR6346296:0.009408784000000003,((DMG2300867:0.0,SRR6346247:0.0):4.999999969612645E-9,SRR6346303:0.028528482999999993):0.009392021000000028):4.999999969612645E-9,(SRR6346331:0.009403959000000017,(SRR6346358:0.009557739999999981,(DMG2300866:5.000000025123796E-9,SRR6346280:0.009384127999999992):0.009389804999999973):0.009450777000000021):4.999999969612645E-9):5.000000025123796E-9,((DMG2212098-DMG2301551_mincov-1:0.0,DMG2304587_mincov-1:0.0,SRR6346234:0.0,SRR6346243:0.0,SRR6346328:0.0,SRR6346333:0.0):4.999999969612645E-9,((SRR6346364:0.019052344,(SRR6346254:4.999999969612645E-9,SRR6346359:0.00939487499999997):0.00940395799999999):5.000000025123796E-9,(SRR6346238:0.028934134999999972,SRR6346240:0.009408784000000003):5.000000025123796E-9):4.999999969612645E-9):5.000000025123796E-9):5.000000025123796E-9):4.999999969612645E-9):0.009408848000000025):4.999999969612645E-9):0.018946993000000023):0.1506598795,(SRR6346292:0.09909331700000001,(SRR6346206:0.05062636399999998,SRR6346340:0.061546725999999996):5.000000025123796E-9):0.1506598795);')
plot(obj,colors=cols,ftype="off",cex.points=c(0,1.5), pts=FALSE)

```

## SNP chromosome position plot

```

python SNP_position_plot.py [list_of_sites] [outfile.png]


```














```

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


######################################################################################

# clean full.aln
snippy-clean_full_aln tmp.full.aln > tmp.full.clean.aln

# make subset of full.aln
sh snippy_full_to_subset_csv.sh tmp.full.clean.aln tmp_fofn.txt 117_POS.csv 36-VIC_4-seqcap-mincov-1_full_subset.csv

# OHE
python OHE.py

# extract the seqcap columns to new file and removal all 'nan' rows
Excel

# replace the 'N' alleles with 'nan' for specific individuals at specific sites
python replace_N-allele_with_nan.py

# remove all rows with 'N'
Excel

# impute
python IterativeImputer.py

# combine the train and test tables
Excel

# transpose matrix
tr ',' '\t' < IMPUTE_36-VIC_full_subset.OHE_WO-nan-N.csv | datamash transpose -H | tr '\t' ',' > IMPUTE_36-VIC_full_subset.OHE_WO-nan-N.tr.csv

# convert allele by site to AGCT by site
python imputation_to_alignment.py

# convert csv to mfa
sh AGCT-csv_to_mfa.sh IMPUTE_36-VIC_full_subset.OHE_WO-nan-N.tr.SITES.csv IMPUTE_36-VIC_full_subset.OHE_WO-nan-N.tr.SITES.aln

# make tree
nice FastTree -nt -gtr IMPUTE_36-VIC_full_subset.OHE_WO-nan-N.tr.SITES.aln > IMPUTE_36-VIC_full_subset.OHE_WO-nan-N.tr.SITES.FastTree-ML.nwk

######################################################################################




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


```
