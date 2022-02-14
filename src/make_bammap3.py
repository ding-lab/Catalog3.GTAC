import pandas as pd
import argparse, sys, os, uuid

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make a listing of all .fastq.gz files found in directory and assign UUID, writing a BamMap v3 file")
    parser.add_argument("datadir", help="Directory with downloaded MGI data")
    parser.add_argument("-o", "--output", dest="outfn", required=True, help="Output BamMap file name")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debugging information to stderr")
    parser.add_argument("-s", "--system", dest="system", default="storage1", help="Define system that path refers to")
    parser.add_argument("-n", "--no-header", action="store_true", help="Do not print header")

    args = parser.parse_args()

    bammap = [] 
    for f in os.listdir(args.datadir):
        if (not f.endswith(".fastq.gz")):
            continue
        rpath = args.datadir + '/' + f
        fpath = os.path.abspath(rpath)
        if (not os.path.isfile(fpath)):
            continue
        uid = str(uuid.uuid4())

        bammap.append([f, uid, fpath, args.system])

    header = [ "#dataset_name", "uuid", "data_path", "system"]
    bammap_df = pd.DataFrame(bammap, columns=header)
    print("Writing catalog to " + args.outfn)
    bammap_df.to_csv(args.outfn, sep="\t", index=False)


