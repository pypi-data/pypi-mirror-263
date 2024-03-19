# SNF2JSON

This tool is a simple file converter that takes a Sniffles (SNF) file and converts it into a JSON like object (SNFJ).
The purpose of this converter is to make it easier to work with the Sniffles file format in other tools such as
[Spectre](https://github.com/fritzsedlazeck/Spectre), which is a long read copy number variation (CNV) caller.

Functionality:
To preserve the original data structure of the SNF file, the pickled objects withing the file are converted into a JSON 
like object structure, which can easily be loaded into a Python dictionary.

Installation:
```bash
pip install snf2json
```
Usage:

For compression use the .gz extension in the output filename. 
```bash
snf2json <sample.snf> <new_sample.snfj.gz>
```
or
```bash
snf2json <sample.snf> <new_sample.snfj>
```
