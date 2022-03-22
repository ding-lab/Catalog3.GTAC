Details of mapping from MGI-style SampleMap to Catalog3 columns

# SampleMap columns
     1	File Name	TWFU-CPT0002270014-Y1N1Z1_1Bn1_1_S2_L002_R1_001.fastq.gz
     2	Flow Cell ID	H7JNJDSX3
     3	Index Sequence	GCGGGTAAGT+TAGCACTAAG
     4	Lane Number	2
     5	Read Number	1
     6	Sample Name	TWFU-CPT0002270014-Y1N1Z1_1Bn1_1
     7	Species	Human
     8	Tissue Type
     9	Library Type	cdna library
    10	Library Name	TWFU-CPT0002270014-Y1N1Z1_1Bn1_1
    11	Completion Date	2022-01-27
    12	Total Bases Kb	"9755585.0"
    13	% PF Clusters	74.07
    14	Avg QScore	35.96
    15	% > Q30	93.8
    16	% Phix Error Rate
    17	Protocol	10x_SC_3'_GEX_V3.1

# Catalog V3 columns
```
    header = [ 'dataset_name', 'case', 'disease', 'experimental_strategy', 'sample_type', 'specimen_name', 'filename',
        'filesize', 'data_format', 'data_variety', 'alignment', 'project', 'uuid', 'md5', 'metadata']
```

'dataset_name' = sm[1] = sm['File Name']
'case' = sm[6] = sm['Sample Name']
'disease' = as passed by argument
'experimental_strategy' = NA
'sample_type' = NA
'specimen_name' = sm[6] = sm['Sample Name']
'filename' = sm[1] = sm['File Name']
'filesize' = NA
'data_format' = FASTQ
'data_variety' = NA
'alignment' = NA
'project' = as passed by argument
'uuid' = matched from BamMap
'md5' = NA
'metadata' = 
    lane = sm['Lane Number'], 
    read = sm['Read Number'], 
    library type = sm['Library Type'], 
    protocol = sm['Protocol'],
    download_id  = passed
    batch_name = passed

