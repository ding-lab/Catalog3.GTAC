Development of "BamMap.JBM" project.  This refers to creating BamMap v3 files from
BamMap files generated for the ATAC-Seq project (JBM) here:
    https://github.com/ding-lab/GDAN.catalog/blob/main/ATAC-seq/BamMap/ATACseq.BamMap.storage1.tsv

Only "data_path" and "system" of the JBM is retained.  The path is merged with
the catalog file "filename" (column 7) to provide UUID and dataset_name.

A Catalog file (Catalog v3 format) is required.  Here, using
../03-dev.GDAN/dat/Catalog.dat

JBM format:
$ examine_row ATACseq.BamMap.storage1.tsv 20
     1  sample_name TCGA-GK-A6C7-01A-11D-A705-36.wgs.T.hg38
     2  case    TCGA-GK-A6C7
     3  disease ATACseq
     4  experimental_strategy   WGS
     5  sample_type tumor
     6  data_path   /storage1/fs1/dinglab/Active/Projects/ATACseq/primary/AWS/WGS/3c906fb3-f7c1-4c2b-a57a-35a25727009e_wgs_gdc_realn.bam
     7  filesize    342557674888
     8  data_format BAM
     9  reference   hg38
    10  gdc_file_id 17c2b235-a075-468e-af31-4e88a3a64bb0
    11  system  storage1

From this, retain only the data_path, and extract "filename" and "system". Match by "filename" to Catalog, and retain uuid and dataset_name

BamMap v3 fields:
    dataset_name
    uuid
    data_path 
    system

# Preliminiary testing

* significant number of filenames in JBM do not match entries in Catalog file.  Example:
    filename: 42e9b8e0-94c1-4864-b8be-3e3f476df1d9_wgs_gdc_realn.bam

JBM: 
```
     1  sample_name TCGA-81-5910-10A-01D-A730-36.wgs.N.hg38
     2  case    TCGA-81-5910
     3  disease ATACseq
     4  experimental_strategy   WGS
     5  sample_type blood_normal
     6  data_path   /storage1/fs1/dinglab/Active/Projects/ATACseq/primary/AWS/WGS/42e9b8e0-94c1-4864-b8be-3e3f476df1d9_wgs_gdc_realn.bam
     7  filesize    243582184002
     8  data_format BAM
     9  reference   hg38
    10  gdc_file_id 0c834663-915b-45ec-a815-501dac3f092b
    11  system  storage1
```

Catalog:
```
     1  dataset_name    TCGA-81-5910.WGS.N
     2  case    TCGA-81-5910
     3  disease GBM
     4  experimental_strategy   WGS
     5  sample_type blood_normal
     6  specimen_name   TCGA-81-5910-10A-01D-A730-36
     7  filename    TCGA-81-5910-10A-01D-A730-36.bam
     8  filesize    79445397052
     9  data_format BAM
    10  data_variety    NA
    11  alignment   aligned
    12  project ATAC
    13  uuid    5b5edb44-fce3-4656-b03d-1720ca6abf2e
    14  md5 982a49821a7cb7180d4cb922e94be54f
    15  metadata    { 'aliquot_tag': 'ALQ_3c312520' }
```


