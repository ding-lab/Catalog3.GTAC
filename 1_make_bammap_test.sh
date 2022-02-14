PYTHON="/Users/mwyczalk/miniconda3/bin/python"

DATD="../data"

OUT="./dat/bammap3.dat"
SYSTEM="shiso"

CMD="$PYTHON src/make_bammap3.py -s $SYSTEM -o $OUT $DATD"

>&2 echo Running: $CMD
eval $CMD
