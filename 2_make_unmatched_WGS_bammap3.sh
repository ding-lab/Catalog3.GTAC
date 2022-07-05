PYTHON="/diskmnt/Projects/Users/mwyczalk/miniconda3/bin/python"

JBM_BAM="/home/mwyczalk_test/Projects/Catalog3/GDAN.catalog/ATAC-seq/BamMap/ATACseq.WGS.BamMap.storage1.tsv"
UNMATCHED_FILENAMES="dat/ATAC-WGS.unmatched.filename.tsv"
mkdir -p ./dat

OUT_CAT="./dat/ATAC-WGS.unmatched.Catalog3.tsv"
OUT_BAM="./dat/ATAC-WGS.unmatched.BamMap3.tsv"

# usage: make_catalog3.JBM.py [-h] [-b BAMMAP] -o OUTPUT_CATALOG -O OUTPUT_BAMMAP [-P PROJECT] [-d] filenames
ARGS=" -b $JBM_BAM -o $OUT_CAT -O $OUT_BAM "
CMD="$PYTHON src/make_catalog3.JBM.py $@ $ARGS $UNMATCHED_FILENAMES"

>&2 echo Running: $CMD
eval $CMD
