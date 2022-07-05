PYTHON="/diskmnt/Projects/Users/mwyczalk/miniconda3/bin/python"

JBM_BAM="/home/mwyczalk_test/Projects/Catalog3/GDAN.catalog/ATAC-seq/BamMap/ATACseq.WXS.wgs_cases.only_pairs.BamMap.tsv"
UNMATCHED_FILENAMES="dat/ATAC-WXS.unmatched.filename.tsv"
mkdir -p ./dat

OUT_CAT="./dat/ATAC-WXS.unmatched.Catalog3.tsv"
OUT_BAM="./dat/ATAC-WXS.unmatched.BamMap3.tsv"

# usage: make_catalog3.JBM.py [-h] [-b BAMMAP] -o OUTPUT_CATALOG -O OUTPUT_BAMMAP [-P PROJECT] [-d] filenames
ARGS=" -b $JBM_BAM -o $OUT_CAT -O $OUT_BAM "
CMD="$PYTHON src/make_catalog3.JBM.py $@ $ARGS $UNMATCHED_FILENAMES"

>&2 echo Running: $CMD
eval $CMD
