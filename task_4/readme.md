# Task 4 - "Tardigrades: from genestealers to space marines "
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
### Step 1 - The first attempt
First, using diamond 2.1.24, a protein database was created for further work:
```bash
diamond makedb --in peptides.fa --db diamond_db
```
The peptides were then processed using the previously created database:
```bash
diamond blastp -d diamond_db.dmnd -q proteins.fa -f 6 -o diamond_output --very-sensitive
```
The results turned out to be incorrect, because, as it turned out later, diamond does not work well with short sequences.
### Step 2 - The second attempt
The toolkit was changed to blastp 2.16.0 and the same work steps were completed:
```bash
makeblastdb -in proteins.fa -dbtype prot  -out task4_db  
```
```bash
blastp -db task4_db -query peptides.fa -outfmt 6 -out blastp.txt
```
Then the repetitive ones were deleted from the whole protein file:
```bash
awk '{print $2}' blastp.txt | sort | uniq > sorted_proteins.txt
```
The sequences of these proteins were also obtained using seqtk 1.5:
```bash
seqtk subseq proteins.fa sorted_proteins.txt > working_sequence.fa
```
### Step 3 - Subcellular localization
Web-version of WoLF PSORT was used to predict subcellular localization of proteins

[WoLF Result](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/blob/main/task_4/WoLF_PSORT_output.txt)
Web-version of TargetP was used to confirm the presence of signaling and mitochondrial peptides

[TargetP Result](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/blob/main/task_4/targetp_output.txt)
### Step 4 - blast
blastp with UniProtKB/Swiss-Prot database was used to search for homologous proteins

[blastp result](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/blob/main/task_4/blast_output.txt)
### Step 5 - HMMER
The web version of HMMER was used to search for proteins by collection of profile-HMMs.

[HMMER result](https://www.ebi.ac.uk/Tools/hmmer/results/2ea15112-2c06-48fc-abb4-75b5e22f85de/score)
