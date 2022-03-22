PYTHON="/diskmnt/Projects/Users/mwyczalk/miniconda3/bin/python"

JBM="/home/mwyczalk_test/Projects/Catalog3/discovery/03-dev.GDAN/dev.untracked/GDAN.catalog/ATAC-seq/BamMap/ATACseq.BamMap.storage1.tsv"
CATALOG="/home/mwyczalk_test/Projects/Catalog3/discovery/03-dev.GDAN/dat/Catalog.dat"

mkdir -p ./dat
OUT="./dat/bammap3.dat"

CMD="$PYTHON src/make_bammap3.JBM.py -o $OUT $JBM $CATALOG"

>&2 echo Running: $CMD
eval $CMD
