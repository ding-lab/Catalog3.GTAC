import pandas as pd
import argparse, sys, json

# Write Catalog3 file for every line of reads file 
# Essentially a merge of reads and aliquots, with some normalization of data, and output to data format as defined here:
#   https://docs.google.com/document/d/1uSgle8jiIx9EnDFf_XHV3fWYKFElszNLkmGlht_CQGE/edit#
# Implemented in pandas (i.e., column-wise operations)

def read_samplemap(sm_fn):
    samplemap = pd.read_csv(sm_fn)
    return(samplemap)

def read_bammap(bm_fn):
    bammap = pd.read_csv(bm_fn, sep="\t", escapechar='#')
    return(bammap)

def write_catalog(outfn, catalog):
    header = [ 'dataset_name', 'case', 'disease', 'experimental_strategy', 'sample_type', 'specimen_name', 'filename',
        'filesize', 'data_format', 'data_variety', 'alignment', 'project', 'uuid', 'md5', 'metadata']

    write_data = catalog[header]

    # close, but need to comment out leading line
    print("Writing catalog to " + outfn)
    write_data.to_csv(outfn, sep="\t", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processes MGI Samplemap.csv file")
    parser.add_argument("samplemap_fn", help="MGI Samplemap file")
    parser.add_argument("-b", "--bammap", dest="bammap_fn", required=True, help="BamMap of data files")
    parser.add_argument("-o", "--output", dest="outfn", required=True, help="Output file name")
    parser.add_argument("-D", "--disease", dest="disease", default="DISEASE", help="Disease code")
    parser.add_argument("-P", "--project", dest="project", default="PROJECT", help="Project name")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debugging information to stderr")
    parser.add_argument("-n", "--no-header", action="store_true", help="Do not print header")
    parser.add_argument("-L", "--download_id", dest="download_id", help="Download ID, starting with DT-")
    parser.add_argument("-B", "--batch_name", dest="batch_name", help="Download batch name, taken from subject line of email")

    args = parser.parse_args()

    samplemap = read_samplemap(args.samplemap_fn)
    bammap = read_bammap(args.bammap_fn)

    # Confirm that file names as listed by Samplemap match those listed in BamMap
    sm_name = samplemap['File Name'].sort_values().reset_index(drop=True)
    bm_name = bammap['dataset_name'].sort_values().reset_index(drop=True)

    if (not sm_name.equals(bm_name)): 
        print("ERROR: File names in BamMap do not match those in Samplemap")
        print("SampleMap: " + sm_name)
        print("BamMap: " + bm_name)
        sys.exit(1)

    # Merge samplemap with BamMap to get UUID column
    samplemap = samplemap.merge(bammap[['dataset_name', 'uuid']], left_on="File Name", right_on="dataset_name")

#    header = [ 'dataset_name', 'case', 'disease', 'experimental_strategy', 'sample_type', 'specimen_name', 'filename',
#        'filesize', 'data_format', 'data_variety', 'alignment', 'project', 'uuid', 'md5', 'metadata']

    catalog = samplemap[['File Name', 'Sample Name']]
    catalog = catalog.rename(columns={'File Name': 'dataset_name', 'Sample Name': 'case'})
    catalog['specimen_name'] = samplemap['Sample Name']
    catalog['filename'] = samplemap['File Name']
    catalog['disease'] = args.disease
    catalog['project'] = args.project
    catalog['experimental_strategy'] = "NA"
    catalog['sample_type'] = "NA"
    catalog['filesize'] = "NA"
    catalog['data_format'] = "FASTQ"
    catalog['data_variety'] = "NA"
    catalog['alignment'] = "NA"
    catalog['uuid'] = samplemap['uuid']
    catalog['md5'] = "NA"

    #metadata = "'lane': '" + str(samplemap['Lane Number']) + "'"   # e.g., 'aliquot_tag': 'ALQ_e412b5f2'
    metadata = "'lane': '" + samplemap['Lane Number'].apply(str)  + "'"
    metadata += ", 'read': '" + samplemap['Read Number'].apply(str) + "'"   
    metadata += ", 'library_type': '" + samplemap['Library Type'].apply(str) + "'"   
    metadata += ", 'protocol': '" + samplemap['Protocol'].apply(str) + "'"      # this often will have single quotes embedded - problem
    if (args.download_id):
        metadata += ", 'download_id': '" + args.download_id + "'"   
    if (args.batch_name):
        metadata += ", 'batch_name': '" + args.batch_name + "'"   

    catalog['metadata'] = "{ " + metadata + " }"

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


    write_catalog(args.outfn, catalog)
    
