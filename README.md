# Mozzie_possum_human_genomic_analysis
Genomic analysis of mosquito, possum and human derived *Mycobacterium. ulcerans* genomes


## Missing SNP imputation:

### Dependencies:
```
snippy v4.4.5
pandas v1.4.2
numpy v1.23.3
sklearn v1.1.2
```

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
```

## Phylogeographic figure generation (R v2021.09.2 Build 382):

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

