Design for general purpose BamMap maker for GDC data which has been downloaded 
by a non-CPTAC3-style process.  Matching of downloaded data to metadata is done
by filename match to catalog.  

In general, it is preferred to avoid filename matching.  Better ways of generating
data is to have UUID known and match on that to Catalog file metadata.

* Only a list of paths of BAM files is passed as a filename argument
* System is specified as per-run
* It is assumed that the filename of downloaded data is not modified

Examples are TCGA files Jay downloaded

# For DLBCL
WARNING: 17 unknown filenames:
0     CTSP-ACY0-NB1-A-1-0-D-A889-36.WholeGenome.RP-1...
1     CTSP-ACY0-TTP1-A-1-1-D-A889-36.WholeGenome.RP-...
2     CTSP-ACY1-NB1-A-1-0-D-A889-36.WholeGenome.RP-1...

Will redo discovery.  Does not change

## Investigating

Here is example specific file which did not match
/storage1/fs1/dinglab/Active/Projects/CTSP-DLBCL/primary/AWG/WGS/CTSP-ACY0-NB1-A-1-0-D-A889-36.WholeGenome.RP-1329.bam

### Case list

DLBCL case list is generated from unique cases in this file:
    /home/mwyczalk_test/Projects/Catalog3/discovery/04-dev.DLBCL/dat/CTSP-DLBCL1_WGS-Alignment_s3Manifest.tsv

Turns out, there is an updated version of this here:
    /home/mwyczalk_test/Projects/Catalog3/GDAN.catalog/DLBCL/DLBCL1.BamMap.storage1.tsv
Catalog regenerated here:
    /home/mwyczalk_test/Projects/Catalog3/discovery/08.DLBCL_202
This catalog then copied to 
    /home/mwyczalk_test/Projects/Catalog3/GDAN.catalog/DLBCL/Catalog3

# Run 2

347 filenames successfully matched to catalog

-> success!

/home/mwyczalk_test/Projects/Catalog3/bammap/02_ATAC_JBM/dat/DLBCL.BamMap3.dat

# for ATAC

WARNING: 241 unknown filenames:
1      04a96939-24b7-4764-81da-5284029b3ca5_wgs_gdc_realn.bam
3      237e3757-c320-4103-8468-93e6f20f4c3a_wgs_gdc_realn.bam
5      44847057-7892-4a64-93da-1d767e8c3e04_wgs_gdc_realn.bam
7      39cf12f2-db46-404b-baa0-f1b240a5f064_wgs_gdc_realn.bam
22     dc5d4a05-ce89-423b-a31c-c068b788756b_wgs_gdc_realn.bam
                                ...
919    3e919f38-a312-4d69-befd-27c62a5d0704_wgs_gdc_realn.bam
921    a23632be-a8c3-4c41-b24b-7b03ec8311a5_wgs_gdc_realn.bam
924    7eae49f4-eead-4243-836b-9710e0120a64_wgs_gdc_realn.bam
926    37d827d8-360c-4738-8920-1adfa42d5dcc_wgs_gdc_realn.bam
928    2f2239f1-c612-46a2-923b-dd134e071294_wgs_gdc_realn.bam
Name: filename, Length: 241, dtype: object
These will be ignored
688 filenames successfully matched to catalog

Written to /home/mwyczalk_test/Projects/Catalog3/bammap/02_ATAC_JBM/dat/ATAC.BamMap3.dat
