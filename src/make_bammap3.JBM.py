import pandas as pd
import argparse, sys, os, uuid

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create BamMap3 file based on JBM and Catalog3 file")
    parser.add_argument("jbm_fn", help="Path to JBM file")
    parser.add_argument("catalog_fn", help="Path to corresponding Catalog3 file")
    parser.add_argument("-o", "--output", dest="outfn", required=True, help="Output BamMap file name")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debugging information to stderr")
    parser.add_argument("-n", "--no-header", action="store_true", help="Do not print header")

    args = parser.parse_args()

    jbm = pd.read_csv(args.jbm_fn, sep="\t", comment='#')
    catalog = pd.read_csv(args.catalog_fn, sep="\t")

    bm = jbm[['data_path', 'system']]
    filename=bm['data_path'].apply(lambda x: os.path.basename(x))
    bm = bm.assign(filename = filename.values)

    bm = bm.merge(catalog[['filename', 'uuid', 'dataset_name']], on="filename", how="left")
    bm = bm.drop(columns=['filename'])

    print("Writing catalog to " + args.outfn)
    columns=['dataset_name', 'uuid', 'data_path', 'system']
    bm.to_csv(args.outfn, sep="\t", index=False, columns=columns, na_rep="Unmatched")
