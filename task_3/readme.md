# Task 3 - "De novo assembly and annotation of bacterial genomes"
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
### Step 1 - Raw data quality analysis
```bash
fastqc -o . forward_reading.fastq reverse_reading.fastq
```
### Step 2 - Genome assembly
```bash
spades.py --isolate -1 forward_reading.fastq -2 reverse_reading.fastq -o spades_output -t 16 -m 32
```
```bash
spades.py --isolate -1 forward_reading.fastq -2 reverse_reading.fastq --pacbio SRR1980037.fastq -o long_reads_spades_output -t 16 -m 32
```
```bash
quast scaffolds.fasta -o quast_out
```
```bash
bakta --db /home/nochy/bakta_db/db scaffolds.fasta --output bakta_output --genus Escherichia --species coli --gram - --threads 16
```
```bash
barrnap scaffolds.fasta --kingdom bac --threads 16 --outseq 16s_rrna.fasta
```       
