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
### Step 2 - blastp
The toolkit was changed to blastp 2.16.0 and the same work steps were completed:
```bash
makeblastdb -in peptides.fa -dbtype prot  -out task4_db  
```
```bash
blastp -db task4_db -query proteins.fa -outfmt 6 -out blastp
```
### Step 3 - Genome annotation

### Step 4 - BLAST 16s rRNA
