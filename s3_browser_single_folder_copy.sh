#!/usr/bin/env bash

path_to_fastq="/samba/aviti/AV244711/20251028_AV244711_AMLMRD_IDTCAPTUREASSAY_28_10_25/IDT_MRD/Samples/DefaultProject"
AML_folder="RESEARCH_IDTMRD_20251028"
output_folder="s3://hematopath-data/Clinical_NGS_Analysis/01FastqArchival2025"

# Make a folder and copy the fastq.gz files here
mkdir -p ${AML_folder}

# Search for fastq files and choose only the ones without a digit at their start and move them to a folder named in MISC
#for i in `ls $path_to_fastq/*fastq* | sed "s:$path_to_fastq/::g" | grep -E '^[^0-9]+' | grep -v 'Undetermined*'`
#do
#	file_name=$(basename $i)
#	echo $file_name $AML_folder
#	mv $path_to_fastq/$file_name $AML_folder/
#done

# Search for all fastq.gz or .bam files except those with Undetermined* in their name
for fq in `find ${path_to_fastq} -type f \( -iname '*.bam' -o -iname '*.fastq.gz' ! -iname 'Undetermined*' \)`; do
	if [[ -f "$fq" ]]; then
		ln -sf "$fq" "${AML_folder}/"
	fi
done

exit_stat=1
while [ $exit_stat -ne 0 ]; do
	aws s3 sync ${AML_folder} ${output_folder}/${AML_folder}/
	exit_stat=$?
done
echo "`ls ${AML_folder}/*` synced to ${output_folder}/${AML_folder}" >> ${AML_folder}.dat.info
