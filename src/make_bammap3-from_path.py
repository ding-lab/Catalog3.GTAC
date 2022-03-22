import pandas as pd
import argparse, sys, os, uuid

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create BamMap3 file based on paths of downloaded data")
    parser.add_argument("bampaths", help="Path to file listing full dataset paths.  Assume headers present")
    parser.add_argument("-k", "--path_key", default="data_path", help="column name listing data path")

    parser.add_argument("-C", "--catalog", required=True, help="Path to corresponding Catalog3 file")
    parser.add_argument("-S", "--system", required=True, help="System name")
    parser.add_argument("-o", "--output", dest="outfn", required=True, help="Output BamMap file name")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debugging information to stderr")
    parser.add_argument("-n", "--no-header", action="store_true", help="Do not print header")

    args = parser.parse_args()

    bampaths = pd.read_csv(args.bampaths, sep="\t")
    catalog = pd.read_csv(args.catalog, sep="\t")

    paths = bampaths[args.path_key]
    filename=paths.apply(lambda x: os.path.basename(x))
    bams = pd.concat([paths, filename], axis="columns")
    bams.columns = ['data_path', 'filename']
    bams["system"] = args.system

    bams = bams.merge(catalog[['filename', 'uuid', 'dataset_name']], on="filename", how="outer", indicator=True)
    # Evaluatee whether merged completely, what was not merged
    vc = bams['_merge'].value_counts()
    if ( vc["left_only"] > 0): 
        m = bams['_merge'] == "left_only" 
        print("WARNING: " + str(vc["left_only"]) + " unknown filenames:")
        print(bams.loc[m, "filename"])
        print("These will be ignored")

    print(str(vc["both"]) + " filenames successfully matched to catalog")
    m = bams['_merge'] == "both" 

    bams = bams.loc[m]

    print("Writing catalog to " + args.outfn)
    columns=['dataset_name', 'uuid', 'system', 'data_path']
    bams.to_csv(args.outfn, sep="\t", index=False, columns=columns, na_rep="Unmatched")
