# Task 2 - "What causes antibiotic resistance"
## Lab Journal
All calculations were performed by the following platforms:
- PC 1:
    ```
    OS: Fedora Linux 43 (KDE Plasma Desktop Edition) x86_64
    CPU: AMD Ryzen 7 3700X
    GPU: AMD Radeon RX 7800 XT
    Memory: 32 GiB
    ```
- PC 2:
    ```
    OS: Linux Mint 22.3 x86_64
    CPU: AMD Ryzen 7 8845HS
    GPU: AMD Radeon 780M
    Memory: 32 GiB
    ```
Both Linux computers have Desktop Environment, so basic operations such as moving files between directories, unzipping archives, and so on were performed not using the command line, but using built-in solutions for the corresponding Desktop Environments.
### Step 1 - Getting raw data
First, we received the data for further processing:
```bash
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.fna.gz # sequence in .fna format
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.gff.gz # annotation in .gff format
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.gbff.gz # annotation in .gbff format
```
The raw sequencing data was downloaded from the resource https://figshare.com/ndownloader/articles/10006541/versions/3
### Step 2 - Primary inspection
Using seqkit 2.13.0, detailed information was obtained about .fastq file:
```bash
seqkit stats forward_reading.fastq
```
Using FastQC 0.12.1, a report was obtained for [forward](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/blob/main/task_2/forward_reading_fastqc.html) and [reverse](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/blob/main/task_2/reverse_reading_fastqc.html) readings:
```bash
fastqc -o . forward_reading.fastq reverse_reading.fastq
```
### Step 3 - Filtering the reads
Using fastp 0.23.4, trimming was performed according to the following parameters:
1. Cut bases off the start of a read if quality below 20
2. Cut bases off the end of a read if quality below 20
3. Trim reads using a sliding window approach, with window size 10 and average quality within the window 20
4. Drop the read if it is below length 20
```bash
fastp -i forward_reading.fastq -I reverse_reading.fastq -o trimmed_forward_reading.fastq -O trimmed_reverse_reading.fastq -5 -3 -r -W 10 -M 20 -l 20
```
Trimming was also performed with an increase in all parameters to 30:
```bash
fastp -i forward_reading.fastq -I reverse_reading.fastq -o 30_trimmed_forward_reading.fastq -O 30_trimmed_reverse_reading.fastq -5 -3 -r -W 10 -M 30 -l 30
```
fastp automatically shows a comparison between what was "before" and "after", so it doesn't make sense to additionally check with FastQC.
The fastp reports are located in the [fastp_out directory](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/tree/main/task_2/fastp_out)
### Step 4 - Aligning sequences to reference
First, an index for alignment was created using bwa 0.7.19-r1273:
```bash
bwa index GCF_000005845.2_ASM584v2_genomic.fna
```
Then, alignment to the reference was performed:
```bash
bwa mem GCF_000005845.2_ASM584v2_genomic.fna trimmed_forward_reading.fastq trimmed_reverse_reading.fastq > alignment.sam
```
The alignment in sam format was compressed to bam using samtools 1.23.1:
```bash
samtools view -S -b alignment.sam > alignment.bam
```
Basic statistics was also collected from the alignment file:
```bash
samtools flagstat alignment.bam
```
The bam file was then sorted by sequence coordinate on reference and indexed for faster search:
```bash
samtools sort alignment.bam -o alignment_sorted.bam
samtools index alignment_sorted.bam
```
### Step 5 - Variant calling
For further work, we need to create a technical mpileup file that looks at whether each base is related to a reference or not:
```bash
samtools mpileup -f GCF_000005845.2_ASM584v2_genomic.fna alignment_sorted.bam >  my.mpileup
```
Then, in order to see which inconsistencies are a mutation and not a sequencing error, we used varscan 2.4.6:
```bash
varscan mpileup2snp my.mpileup --min-var-freq 0.20 --variants --output-vcf 1 > VarScan_results.vcf
```
min-var-freq option sets the minimum percent of non-reference bases at a position required to call it a mutation in the sample. The [varscan documentation](https://pmc.ncbi.nlm.nih.gov/articles/PMC4278659/table/T2/) says that for isolated samples, the min-var-freq should be 0.20. Values lower are applicable for samples with multiple organisms.
### Step 6 - SNP annotation
A database for SnpEff 5.4.0c was created for further processing:
```bash
echo "k12.genome : ecoli_K12" > snpEff.config
mkdir -p data/k12
gunzip GCF_000005845.2_ASM584v2_genomic.gbff.gz
cp GCF_000005845.2_ASM584v2_genomic.gbff data/k12/genes.gbk
snpEff build -genbank -v k12
```
SNPs were then annotated using SnpEff:
```bash
snpEff ann k12 VarScan_results.vcf > VarScan_results_annotated.vcf
```
### Step 7 - Variant effect prediction
To extract key information about identified variants (position, gene, mutation type, impact, and amino acid change), the following command was used:

```bash
echo "Position,Gene,Type,Impact,Protein_change" > table_full.csv

grep -v "^#" VarScan_results_annotated.vcf | \
awk -F'\t' '{
  split($8, info, "ANN=");
  split(info[2], ann, ",");
  split(ann[1], fields, "|");
  print $2 "," fields[4] "," fields[2] "," fields[3] "," fields[11]
}' >> table_full.csv
```
This command parses the annotated VCF file and extracts relevant fields from the ANN annotation generated by SnpEff. The resulting file [table_full.csv]() contains a structured summary of variants suitable for downstream analysis. 
![table_full.csv](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/blob/main/task_2/table_full.csv)