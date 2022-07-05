import pandas as pd
import argparse, sys, json, os

# Write Catalog3 file for every line in a JBM-style BamMap file
# Example entry of a JBM-style BamMap:
# 1 sample_name   TCGA-2G-AAFM-01A-11D-A729-36.wgs.T.hg38
# 2 case    TCGA-2G-AAFM
# 3 disease TCGA-TGCT
# 4 experimental_strategy   WGS
# 5 sample_type tumor
# 6 data_path   /storage1/fs1/dinglab/Active/Projects/ATACseq/primary/AWS/WGS/a96db2c5-c516-4b72-a982-46b80b187116_wgs_gdc_realn.bam
# 7 filesize    347538575394
# 8 data_format BAM
# 9 reference   hg38
# 10 gdc_file_id 88885dfa-ea8c-44d3-8c28-b61a6d0bd2b2
# 11 system  storage1

def read_bammap(bm_fn):
    bammap = pd.read_csv(bm_fn, sep="\t", escapechar='#')
    return(bammap)

def write_catalog3(outfn, catalog):
    header = [ 'dataset_name', 'case', 'disease', 'experimental_strategy', 'sample_type', 'specimen_name', 'filename',
        'filesize', 'data_format', 'data_variety', 'alignment', 'project', 'uuid', 'md5', 'metadata']

    write_data = catalog[header]

    # close, but need to comment out leading line
    print("Writing catalog3 to " + outfn)
    write_data.to_csv(outfn, sep="\t", index=False)

def write_bammap3(outfn, catalog):
    header = [ 'dataset_name', 'uuid', 'system', 'path']

    write_data = catalog[header]

    # close, but need to comment out leading line
    print("Writing bammap3 to " + outfn)
    write_data.to_csv(outfn, sep="\t", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processes JBM file to create a Catalog3 and BamMap3")
    parser.add_argument("filenames", help="File listing paths of interest")
    parser.add_argument("-b", "--bammap", help="JBM (ad hoc BamMap) file")
    parser.add_argument("-o", "--output_catalog", required=True, help="Catalog3 output file name")
    parser.add_argument("-O", "--output_bammap", required=True, help="BamMap3 output file name")
    parser.add_argument("-P", "--project", dest="project", default="PROJECT", help="Project name")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debugging information to stderr")

    args = parser.parse_args()

    bammap = read_bammap(args.bammap)
    # Index([' sample_name', 'case', 'disease', 'experimental_strategy', 'sample_type', 'data_path', 'filesize', 'data_format', 'reference', 'gdc_file_id', 'system'],

    filenames = pd.read_csv(args.filenames)

    bam_filename = bammap["data_path"].apply(lambda x: os.path.basename(x))
    bam_filename = bam_filename.rename("filename")
    bammap = pd.concat([bammap, bam_filename], axis="columns")

    # now catalog has just the bammap entries which match to passed filenames
    catalog = bammap.merge(filenames, on="filename")

    catalog = catalog.rename(columns={' sample_name': 'dataset_name', 'sample_name': 'dataset_name', 'gdc_file_id': 'uuid', 'data_path': 'path'})

    catalog['project'] = args.project
    catalog['data_variety'] = "NA"
    catalog['alignment'] = "NA"
    catalog['md5'] = "NA"
    catalog['specimen_name'] = "NA"
    catalog['metadata'] = "{ 'source': 'JBM' }"

#    #metadata = "'lane': '" + str(samplemap['Lane Number']) + "'"   # e.g., 'aliquot_tag': 'ALQ_e412b5f2'
#    metadata = "'lane': '" + samplemap['Lane Number'].apply(str)  + "'"
#    metadata += ", 'read': '" + samplemap['Read Number'].apply(str) + "'"   
#    metadata += ", 'library_type': '" + samplemap['Library Type'].apply(str) + "'"   
#    metadata += ", 'protocol': '" + samplemap['Protocol'].apply(str) + "'"      # this often will have single quotes embedded - problem
#    if (args.download_id):
#        metadata += ", 'download_id': '" + args.download_id + "'"   
#    if (args.batch_name):
#        metadata += ", 'batch_name': '" + args.batch_name + "'"   
#
#    catalog['metadata'] = "{ " + metadata + " }"

#'dataset_name' = sm[1] = sm['File Name']
#'case' = sm[6] = sm['Sample Name']
#'disease' = as passed by argument
#'experimental_strategy' = NA
#'sample_type' = NA
#'specimen_name' = sm[6] = sm['Sample Name']
#'filename' = sm[1] = sm['File Name']
#'filesize' = NA
#'data_format' = FASTQ
#'data_variety' = NA
#'alignment' = NA
#'project' = as passed by argument
#'uuid' = matched from BamMap
#'md5' = NA
#'metadata' = 
#    lane = sm['Lane Number'], 
#    read = sm['Read Number'], 
#    library_type = sm['Library Type'], 
#    protocol = sm['Protocol'],
#    download_id  = passed
#    batch_name = passed

    write_catalog3(args.output_catalog, catalog)
    write_bammap3(args.output_bammap, catalog)
    
