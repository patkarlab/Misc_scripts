#!/usr/bin/env bash

path_to_fastq="/samba/NextSeq1000/runs/250630_VH00985_76_222CGHNNX/fastq"
AML_folder="Transcriptome_250630"
output_location="s3://hematopath-data/Clinical_NGS_Analysis/01FastqArchival2025"

# Make a folder and copy the fastq.gz files here
mkdir -p ${AML_folder}

# Search for fastq files and choose only the ones without a digit at their start and move them to a folder named in MISC
for i in `ls $path_to_fastq/*fastq* | sed "s:$path_to_fastq/::g" | grep -E '^[0-9]+' | grep -v 'Undetermined*'`
do
	file_name=$(basename $i)
	echo $file_name $AML_folder
	mv $path_to_fastq/$file_name $AML_folder/
done

exit_stat=1
while [ $exit_stat -ne 0 ]; do
	aws s3 sync ${AML_folder} ${output_location}/${AML_folder}/
	exit_stat=$?
done
echo "`ls ${AML_folder}/*` synced to ${output_location}/${AML_folder}" >> ${AML_folder}.dat.info
