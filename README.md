# Mozzie_possum_human_genomic_analysis
```Genomic analysis of mosquito, possum and human derived M. ulcerans genomes

This is the tree that was used:
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

# run the missing allele classifier script
sh fofn-checker.sh

# run the evaluation script
sh evaluate.sh [ALL_IMPUTATION.csv]


Allele imputation:

default RFC:
Evaluating DMG2300866:
0.927038626609442
[[111   7]
 [ 10 105]]
Evaluating DMG2300867:
0.8540772532188842
[[114   4]
 [ 30  85]]

default RFC with random upsampling:
Evaluating DMG2300866:
0.9227467811158798
[[110   7]
 [ 11 105]]
Evaluating DMG2300867:
0.8497854077253219
[[113   4]
 [ 31  85]]

default SVC:
Evaluating DMG2300866:
0.9356223175965666
[[111   5]
 [ 10 107]]
Evaluating DMG2300867:
0.8454935622317596
[[112   4]
 [ 32  85]]

default LGR:
Evaluating DMG2300866:
0.9356223175965666
[[111   5]
 [ 10 107]]
Evaluating DMG2300867:
0.8454935622317596
[[112   4]
 [ 32  85]]





```
