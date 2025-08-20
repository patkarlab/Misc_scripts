# Scripts

### parse_gtf.py

This script takes input the gtf file and prints out the follwing columns into a new file.

1. gene_name
2. transcript_id
3. exon_number
4. chrom
5. start
6. end
7. strand

-----
### fastqc_plot.py

#### Usage:
`./fastqc_plot.py <input_fastq.gz> <output_png>`

This script plots the per base quality score.

----
### variant_parser.py

This script will take the *cancervar.csv as input and will write the variants.txt

----
### integrate.py 

This script will map the acmg output to cancervar file

----
### integrate_p2.py 

This script will integrate the output file from `integrate.py` to the final excel.

----
### json_file.py

This script converts the acmg json file to a tsv file printing only the required columns.

1. chrom
2. pos
3. ref
4. alt
5. acmg classification
6. acmg rules
7. classifications