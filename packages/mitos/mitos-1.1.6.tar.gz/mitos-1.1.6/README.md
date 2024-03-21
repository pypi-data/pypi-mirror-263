These are the mitogenome related sources including MITOS and other (more or less) helpful tools. Note that some of the tools are unfinished and not in a production state.

Usage on Galaxy
===============

MITOS should primarily be used via Galaxy. It is available for instance on usegalaxy.eu

- [MITOS2](https://usegalaxy.eu/?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Fmitos2%2Fmitos2%2F2.1.7%2Bgalaxy1&version=latest)
- [MITOS](https://usegalaxy.eu/?tool_id=toolshed.g2.bx.psu.edu%2Frepos%2Fiuc%2Fmitos%2Fmitos%2F1.1.5%2Bgalaxy0&version=latest)



Installation
============

There are three ways to install. Preferred is the installation via conda since this also takes care of non-python requirements of the main mitos script.

1. via conda: `conda install mitos --strict-channel-priority -c conda-forge -c bioconda -n mitos`
   - this will install MITOS2. For MITOS use `conda install "mitos<2" --strict-channel-priority -c conda-forge -c bioconda -n mitos`
   - in case of problems with resolving environments try to use use `--solver libmamba` or replace `conda` by `mamba`.
2. via pip: `pip install mitos`
3. manual: pip -r requirements.txt

For the non-python requirements see README.MITOS.

MITOS
=====

* runmitos.py: standalone CLI MITOS

From runmitos.py help:

```
mandatory options:
  -c CODE, --code CODE  the genetic code
  -o OUTDIR, --outdir OUTDIR
                        the directory where the output is written
  --linear              treat sequence as linear
  -r REFDIR, --refdir REFDIR
                        the directory where the reference data is found

```

Please note that the reference data for the `-r` flag needs to be downloaded from Zenodo ([MITOS](https://zenodo.org/record/2683856), [MITOS2](https://zenodo.org/record/4284483)).

see also `mitos.py --help` README.MITOS

genbank file handling
=====================

* refseqsplit:
    - splits a file consisting of concatenated gb files into single genbank files
    - its possible to apply filters (taxonomy, prefix)

skewness related programs
=========================

* skew:
	compute skewness values for a gene of given genbank files
* skewcum:
	compute cumulative skewness for given genbank files
* skewsvm:
	do svm classification of skewness values .. and try to relate misclassifications to rearrangements

MISC
====

* gcpp
	- pretty print and compare genetic code
