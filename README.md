Design for general purpose BamMap maker for GDC data which has been downloaded 
by a non-CPTAC3-style process.  Matching of downloaded data to metadata is done
by filename match to catalog.  

In general, it is preferred to avoid filename matching.  Better ways of generating
data is to have UUID known and match on that to Catalog file metadata.

* Only a list of paths of BAM files is passed as a filename argument
* System is specified as per-run
* It is assumed that the filename of downloaded data is not modified

Examples are TCGA files Jay downloaded
