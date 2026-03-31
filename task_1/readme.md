# Task 1 - "How to catch the right fish: searching for viruses in sequencing data"
## Abstract
SARS-related pandemics have had an undeniable impact on both the health and social sectors. The history of SARS-related pandemics and major outbreaks is characterized by three distinct, highly pathogenic coronaviruses emerging from animal reservoirs(specifically bats) to cause global health emergencies in the 21st century:
1. The 2002–2004 SARS Outbreak (SARS-CoV-1)
    - Origin - The first severe and readily transmissible disease to emerge in the 21st century, SARS (Severe Acute Respiratory Syndrome) was first identified in Guangdong Province, China, in November 2002.
    - Impact - By the time the outbreak was contained in July 2003, there were 8,096 reported cases and 774 deaths across 29 countries, resulting in a case fatality rate of nearly 10%. No cases of SARS-CoV-1 have been reported since 2004.
2. MERS-CoV (2012–Present)
    - Origin - The Middle East Respiratory Syndrome (MERS) was first identified in Saudi Arabia in 2012.
    - Impact - MERS has a much higher fatality rate than SARS, with a case fatality rate around 34.4%. As of 2020, over 2,494 
    confirmed cases and 858 deaths have been reported across 27 countries.
3. COVID-19 Pandemic (SARS-CoV-2)
    - Origin - In December 2019, a second strain of SARS-related coronavirus (SARS-CoV-2) was identified in Wuhan, Hubei, China.
    - Impact - The COVID-19 pandemic has resulted in over 700 million confirmed cases and over 6.8 million deaths, making it significantly more destructive than the 2003 SARS outbreak, although with a lower individual case fatality rate.

## Main
All calculations were performed by two computers with the following components:
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

The goal of this work is to identify the pathogen caused the clinical case, decribed in the [article](https://www.nature.com/articles/s41586-020-2008-3). Methods and calculations are based on deep meta-transcriptomic sequencing of the bronchoalveolar lavage fluid data. By the description of the clinical case, it was concluded that the pathogen has viral type.

The work can be logically divided into 5 steps:
1. Genome assembly from the raw data;
2. Collecting the QUAST-report;
3. Identifying viral contigs;
4. BLASTing viral contigs to figure out which one belongs to the pathogen;
5. Annotating pathogen contig and comparing annotation with one, alailable on GenBank.
### Step 1 - Genome assembly from raw data
The raw sequencing data was obtained using prefetch 3.2.1:
```bash
prefetch SRR10971381
```
The .sra file was then converted to forward and reverse reads in .fastq format using fasterq-dump 3.2.1:
```bash
fasterq-dump SRR10971381
```
Using SPAdes 4.2.0, we tried to assemble the genome:
```bash
spades.py -1 SRR10971381_1.fastq  -2 SRR10971381_2.fastq -o spades_output -t 16 -m 32
```
But SPAdes displayed an error due to lack of RAM:
```bash
The reads contain too many k-mers to fit into available memory. You need approx. 38.8576GB of free RAM to assemble your dataset
```
Therefore, in the next steps we used the already assembled genome
### Step 2 - Colecting QUAST-report
To evaluate the quality of the genome assembly, a report was generated using QUAST 5.3.0 by the following command:
```bash
quast spades_scaffolds.fasta -o quast_out
```
All report files were saved to [quast_out](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/tree/main/task_1/quast_out) folder.
### Step 3 - Identifying viral contigs
To filter out contigs unsuitable for further analysis, all contigs shorter than 3,000 base pairs were discarded, as the minimum viral genome size is ~2,000-3,000 base pairs:
```bash
xargs samtools faidx spades_scaffolds.fasta > 3000.fa
```
Next, the ViralVerify 1.1 was used to clearly distinguish viral contigs from other possible contigs. Results were saved to [virver_out](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/tree/main/task_1/virver_out) folder, the database of virus/chromosome-specific HMMs was downloaded from the [official repository](https://github.com/ablab/viralVerify):
```bash
viralverify -f 3000.fa -o virver_out --hmm nbc_hmms.hmm
```
### Step 4 - BLAST
Sequence similarity searches were performed using BLAST via the NCBI BLAST server. [File with filtered congigs](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/blob/main/task_1/virver_out/Prediction_results_fasta/3000_virus.fasta), containing only 4 contigs was uploaded. Contig sequences were queried against the NCBI non-redundant (nr) protein database using BLASTX. Search was limited to include viruses (taxid:10239). The best hit for each contig was selected based on the highest bit score and lowest e-value. Results were saved in [3000_virus-HitTable.csv](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/blob/main/task_1/3000_virus-HitTable.csv) table. 
### Step 5 - Genome annotation
Prokka 1.14.6 on the Galaxy platform was selected for genome annotation. This version of prokka was released in early 2020, which will allow us to reproduce the conditions of the outbreak of the pandemic:
```bash
prokka --cpus ${GALAXY_SLOTS:-8} --quiet --outdir outdir --prefix prokka --increment 1 --gffver 3 --mincontig 200 --kingdom Viruses --gcode 1 --evalue 1e-06 /data/dnb12/galaxy_db/files/b/f/5/dataset_bf54d5ed-7a32-436b-9583-9b06ab1b416a.dat
```
## Results
Due to the fact that genome assembly from was failed because of the lack of RAM for SPAdes, it was desided to use [pre-assembled genome](https://drive.google.com/file/d/1PU6gQiF2CvxYhmWxVCWuESnG1XCZvibf/view?usp=drive_link). 

As the result of QUAST analysis, a [report.txt](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/blob/main/task_1/quast_out/report.txt) file was obtained. With the usage of terminal command, stings containing substrings "1000 " and "contig" were obtained: `cat quast_out/report.txt | grep 'contig' | grep '1000 '`. Output shown that only sone string fits the pattern: `# contigs (>= 1000 bp)      666`. Based on these data, it can be concluded that the assembled genome contains 666 contigs of at least 1000 base pairs in length. 

After operations, explained in [Step 3](#step-3---identifying-viral-contigs), amount of potential pathogen contigs was reduced from 111219 to 4. As a result of 
## Discussion
The main difficulty at the initial stage was the lack of RAM for SPAdes, which prevented de novo assembly of reads. Nevertheless, the use of ready-made contigs in combination with a length-filtering pipeline and ViralVerify proved sufficient to accurately isolate the viral sequence. The BLAST analysis unambiguously identified the pathogen as SARS-CoV-2, which corresponds to the clinical case described in the article. The annotation confirmed the structural organization of the virus genome, and the selected version of Prokka (1.14.6) allowed us to reproduce conditions close to the beginning of the pandemic
## References
1. Wu, F., Zhao, S., Yu, B. et al. A new coronavirus associated with human respiratory disease in China. Nature 579, 265–269 (2020). https://doi.org/10.1038/s41586-020-2008-3
2. NCBI SRA-Tools. https://github.com/ncbi/sra-tools
3. Prjibelski, A., Antipov, D., Meleshko, D., Lapidus, A., & Korobeynikov, A. (2020). Using SPAdes de novo assembler. Current Protocols in Bioinformatics, 70, e102. doi: 10.1002/cpbi.102
4. Alexey Gurevich, Vladislav Saveliev, Nikolay Vyahhi and Glenn Tesler, QUAST: quality assessment tool for genome assemblies, Bioinformatics (2013) 29 (8): 1072-1075. doi: 10.1093/bioinformatics/btt086
5. Antipov D, Raiko M, Lapidus A, Pevzner PA. Metaviral SPAdes: assembly of viruses from metagenomic data. Bioinformatics. 2020 Aug 15;36(14):4126-4129. doi: 10.1093/bioinformatics/btaa490. PMID: 32413137
6. Torsten Seemann, Prokka: rapid prokaryotic genome annotation, Bioinformatics, Volume 30, Issue 14, July 2014, Pages 2068–2069, https://doi.org/10.1093/bioinformatics/btu153
7. Martin Enserink, SARS: Chronology of the Epidemic.Science339,1266-1271(2013).DOI:10.1126/science.339.6125.1266
8. Peeri NC, Shrestha N, Rahman MS, Zaki R, Tan Z, Bibi S, Baghbanzadeh M, Aghamohammadi N, Zhang W, Haque U. The SARS, MERS and novel coronavirus (COVID-19) epidemics, the newest and biggest global health threats: what lessons have we learned? Int J Epidemiol. 2020 Jun 1;49(3):717-726. doi: 10.1093/ije/dyaa033. PMID: 32086938; PMCID: PMC7197734.
9. Pagani I, Ghezzi S, Alberti S, Poli G, Vicenzi E. Origin and evolution of SARS-CoV-2. Eur Phys J Plus. 2023;138(2):157. doi: 10.1140/epjp/s13360-023-03719-6. Epub 2023 Feb 16. PMID: 36811098; PMCID: PMC9933829.