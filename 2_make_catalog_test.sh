PYTHON="/Users/mwyczalk/miniconda3/bin/python"

DATD="../data/Samplemap.csv"

OUT="./dat/catalog3.dat"
BM="./dat/bammap3.dat"

CMD="$PYTHON src/make_catalog3.MGI.py -b $BM -o $OUT $DATD"

>&2 echo Running: $CMD
eval $CMD
