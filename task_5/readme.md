# Task 5 - "H+, or how to build a perfect human."
## Lab Journal
All calculations were performed by the following platforms:
- PC 1:
    ```
    OS: Linux Mint 22.3 x86_64
    CPU: AMD Ryzen 7 8845HS
    GPU: AMD Radeon 780M
    Memory: 32 GiB
    ```
Linux computer haы Desktop Environment, so basic operations such as moving files between directories, unzipping archives, and so on were performed not using the command line, but using built-in solutions for the corresponding Desktop Environments.

For the analysis daset, containing 23andMe raw data of Mikhail Rayko, was chosen.
### Step 1 - Analysis of the ancestry of the research object
To determine the subject's ancestry, 23andMe data was used. The [mthap service](https://dna.jameslick.com/mthap/) was used to determine the haplogroup and, consequently, the mtDNA ancestry. The [MorleyDNA service](https://ytree.morleydna.com/extractFromAutosomal) was used to determine the Y-chromosome ancestry. As a result, the mitochondrial haplogroup **H(T152C)** and the Y-chromosome haplogroup **R1a1a (R-M198)** were determined.

The obtained result is typical for Eastern and Central Europe, especially for Slavic peoples (Russians, Poles, Slovaks, Ukrainians, Belarusians). https://www.eupedia.com/europe/european_y-dna_haplogroups.shtml
### Step 2 - Defining sex and eye color
Firstly, for the further analysis, raw 23andMe data was converted to VCF format and saved as a [`snps_clean.vcf`]() with the usage of plink program:
```bash
plink --23file SNP_raw_v4_Full_20170514175358.txt --recode vcf --out snps_clean --output-chr MT --snps-only just-acgt
```

Sex of a subject was defined on the previous step by the existence of Y chromosome, so theкe is no need to define it with additional operations.

To define eyes color 23andMe raw data was filtered by containig one of the substrings connected to eye color. Result was saved to the [`eye_color_snps.txt`](): 
```bash
grep -E "rs12203592|rs12896399|rs12913832|rs16891982|rs6119471" SNP_raw_v4_Full_20170514175358.txt > eye_color_snps.txt
```
As a result subject's eye color was defined as brown https://pmc.ncbi.nlm.nih.gov/articles/PMC3694299/

### Step 3 - Defining lactose intolerance
To define lactose intolerance of the subject, SNP `rs4988235` was chosen because it is correlate with european populations and is located in the enhancer that controls the expression of the LCT (lactase) gene. LCT encodes an enzyme that breaks down lactose. Filtration was comleted with the command below, result was saved as [`lact_intolerance_snp.txt`]()
```bash
grep -E "rs4988235" SNP_raw_v4_Full_20170514175358.txt > lact_intolerance_snp.txt
```
The result showed that the subject is likely to be lactose intolerant. https://pubmed.ncbi.nlm.nih.gov/11788828/
