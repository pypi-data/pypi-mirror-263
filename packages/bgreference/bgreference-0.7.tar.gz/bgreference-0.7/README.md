# BgReference #

bgreference is a library to fast retrive Genome Reference partial sequences.

## Install using CONDA
```
conda install -c conda-forge -c bbglab bgreference
```

## or install using PIP
```
pip install bgreference
```

## Usage example

```
#!python
from bgreference import hg19, hg38

# Get 10 bases from chromosome one build hg19
tenbases_hg19 = hg19('1', 12345, size=10)

# Get 10 bases from chromosome one builg hg38
tenbases_hg38 = hg38('1', 12345, size=10)

# Use synonymous sequence names

hg19(2, 23456)
hg19('2', 23456)
hg19('chr2', 23456)

hg19('MT', 234, size=3)
hg19('chrM', 234, size=3)
hg19('chrMT', 234, size=3)
hg19('M', 234, size=3)

```

## Using your own reference genome

- Create a folder (e.g. ``/my/genome/folder``) to contain the files.
- Create one file per chromosome. Each file shoud be named as ``<chromosme>.txt`` (e.g. ``chr1.txt``), and must contain 1 single line with all the nucleotides (without header).
- Create a file (e.g. ``/my/bgdata.custom``) to indicate the *bgdata* package where to find the new files, as explain in the [bgdata docs](https://bgdata.readthedocs.io/en/latest/advanced.html#fixing-your-builds):
   
```
[paths]  
datasets/genomereference/mygenome = /my/genome/folder
```

> Substitute ``mygenome`` for the name of your genome
   
- Export the above file using the ``BGDATA_BUILDS`` environment variable:
   
```
#!bash
export BGDATA_BUILDS=/my/bgdata.custom
```
   
- Request bgreference the new genome using the ``refseq`` function:
   
```
#!python
import bgreference
bgreference.refseq('mygenome', 'chr1', 1000)
```
   