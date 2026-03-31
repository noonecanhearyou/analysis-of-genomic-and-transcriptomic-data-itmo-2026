# Task 2 - "What causes antibiotic resistance"
## Abstract
## Main
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
fastp automatically shows a comparison between what was "before" and "after", so it doesn't make sense to additionally check with FastQC.
### Step 4 - Aligning sequences to reference
## Results
## Discussion
## References
