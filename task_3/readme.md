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
First, the quality of the raw sequencing data was checked using FastQC 0.12.1:
```bash
fastqc -o . forward_reading.fastq reverse_reading.fastq
```
### Step 2 - Genome assembly
Then, using SPAdes 4.2.0, the genome was assembled from the raw sequencing data:
```bash
spades.py --isolate -1 forward_reading.fastq -2 reverse_reading.fastq -o spades_output -t 16 -m 32
```
The genome was also assembled using a long-read library SRR1980037:
```bash
spades.py --isolate -1 forward_reading.fastq -2 reverse_reading.fastq --pacbio SRR1980037.fastq -o long_reads_spades_output -t 16 -m 32
```
Then the quality of both builds was checked using QUAST 5.3.0:
```bash
quast scaffolds.fasta -o quast_out
```
Further steps of work were carried out with the assembly with a long-read library due to the better quality.
### Step 3 - Genome annotation
The genome was annotated using bakta 1.12.0 using a full database:
```bash
bakta --db /home/nochy/bakta_db/db scaffolds.fasta --output bakta_output --genus Escherichia --species coli --gram - --threads 16
```
Barrnap 1.10.5 was also used to find rRNAs from the genomic assembly:
```bash
barrnap scaffolds.fasta --kingdom bac --threads 16 --outseq 16s_rrna.fasta
```       
Then, using a text editor, only those contigues that belong to 16s rRNA were left.
