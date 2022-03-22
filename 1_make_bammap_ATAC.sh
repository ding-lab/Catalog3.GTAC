PYTHON="/diskmnt/Projects/Users/mwyczalk/miniconda3/bin/python"

DAT="/home/mwyczalk_test/Projects/Catalog3/GDAN.catalog/ATAC-seq/BamMap/ATACseq.WGS.BamMap.storage1.tsv"
CATALOG="/home/mwyczalk_test/Projects/Catalog3/GDAN.catalog/Catalog3/ATAC.Catalog3.tsv"
SYSTEM="storage1"

KEY="data_path"

mkdir -p ./dat
OUTFN="./dat/ATAC.BamMap3.dat"

# make_bammap3-from_path.py [-h] [-k PATH_KEY] -C CATALOG -S SYSTEM -o OUTFN [-d] [-n] bampaths
ARGS="-k $KEY -C $CATALOG -S $SYSTEM -o $OUTFN"
CMD="$PYTHON src/make_bammap3-from_path.py $@ $ARGS $DAT"

>&2 echo Running: $CMD
eval $CMD
