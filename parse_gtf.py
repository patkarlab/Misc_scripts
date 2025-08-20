#!/usr/bin/env python3

import pandas as pd

gtf_file = "/home/ref_annotation/gencode.v19.annotation.gtf"
data = []

with open(gtf_file) as f:
    for line in f:
        if line.startswith("#"):
            continue
        fields = line.strip().split("\t")
        if fields[2] == "exon":
            chrom = fields[0]
            start = int(fields[3])
            end = int(fields[4])
            strand = fields[6]
            info = fields[8]

            # Initialize values
            transcript_id = None
            exon_number = None
            gene_name = None

            for field in info.split(";"):
                field = field.strip()
                if field.startswith("transcript_id"):
                    transcript_id = field.split('"')[1]
                elif field.startswith("exon_number"):
                    parts = field.split('"')
                    exon_number = parts[0].split(" ")[1]
                elif field.startswith("gene_name"):
                    gene_name = field.split('"')[1]

            if transcript_id and exon_number:
                data.append({
                    "gene_name": gene_name,
                    "transcript_id": transcript_id,
                    "exon_number": exon_number,
                    "chrom": chrom,
                    "start": start,
                    "end": end,
                    "strand": strand
                })

exons_df = pd.DataFrame(data)
exons_df.to_csv("enst.csv", sep="\t", index=False)
