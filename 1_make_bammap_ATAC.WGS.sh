PYTHON="/diskmnt/Projects/Users/mwyczalk/miniconda3/bin/python"

JBM_BAM="/home/mwyczalk_test/Projects/Catalog3/GDAN.catalog/ATAC-seq/BamMap/ATACseq.WGS.BamMap.storage1.tsv"
CATALOG="/home/mwyczalk_test/Projects/Catalog3/GDAN.catalog/Catalog3/ATAC.Catalog3.tsv"
UNMATCHED_FILENAMES="dat/ATAC-WGS.unmatched.filename.tsv"
mkdir -p ./dat

# First, make catalog with matched data and spit out unmatched filenames
OUTFN_WGS="./dat/ATAC.BamMap3_WGS.GDC_matched.tsv"

SYSTEM="storage1"
KEY="data_path"

# make_bammap3-from_path.py [-h] [-k PATH_KEY] -C CATALOG -S SYSTEM -o OUTFN [-d] [-n] bampaths
ARGS="-k $KEY -C $CATALOG -S $SYSTEM -o $OUTFN_WGS -U $UNMATCHED_FILENAMES"
CMD="$PYTHON src/make_bammap3-from_path.py $@ $ARGS $JBM_BAM"

>&2 echo Running: $CMD
eval $CMD

exit

OUT_CAT="./dat/ATAC-WGS.unmatched.Catalog3.tsv"
OUT_BAM="./dat/ATAC-WGS.unmatched.BamMap3.tsv"

# usage: make_catalog3.JBM.py [-h] [-b BAMMAP] -o OUTPUT_CATALOG -O OUTPUT_BAMMAP [-P PROJECT] [-d] filenames
ARGS=" -b $JBM_BAM -o $OUT_CAT -O $OUT_BAM "
CMD="$PYTHON src/make_catalog3.JBM.py $@ $ARGS $UNMATCHED_FILENAMES"

>&2 echo Running: $CMD
eval $CMD
