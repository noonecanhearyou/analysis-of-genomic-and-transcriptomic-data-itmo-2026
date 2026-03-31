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
seqkit stats amp_res_1.fastq
```
### Step 3 - Identifying viral contigs
### Step 4 - BLAST
## Results
## Discussion
## References
