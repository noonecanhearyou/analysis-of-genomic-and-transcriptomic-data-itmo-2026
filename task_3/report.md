# De novo assembly and annotation of the 2011 German outbreak *E. coli* X genome reveals a prophage‑encoded Shiga toxin and multidrug resistance
Ivan Uglov, Eugene Fedorov

## Abstract
In April 2011 a previously unknown *Escherichia coli* strain caused a deadly outbreak of haemolytic uraemic syndrome (HUS) in Germany, killing 53 people. Using Illumina and PacBio sequencing data we assembled the genome of this strain (*E. coli* X) *de novo*. A hybrid assembly produced 89 contigs with an N50 of 178 kb. The 16S rRNA gene identified *E. coli* 55989 as the closest known relative. Genome annotation revealed Shiga toxin genes *stx2A* and *stx2B* embedded within a prophage region, explaining the ability to cause HUS. ResFinder detected multiple acquired resistance genes (including *blaCTX‑M‑15*, *blaTEM‑1B*, *tet(A)*, *sul1/2*, *dfrA7*, *aph(3'')‑Ib/aph(6)‑Id*), conferring resistance to β‑lactams, tetracycline, sulphonamides, trimethoprim, streptomycin and others. The reference strain 55989 carried only *tet(B)*. Thus, *E. coli* X became pathogenic through lysogenic conversion by a Shiga toxin‑encoding phage and acquired multidrug resistance via mobile genetic elements.

## Introduction
Haemolytic uraemic syndrome (HUS) is a severe complication of infections with Shiga toxin‑producing *E. coli* (STEC), leading to acute kidney failure and death [1]. In 2011, Germany experienced the largest STEC outbreak ever recorded, with 3816 infections and 53 fatalities. The causative strain (here called *E. coli* X) was initially untypeable by routine biochemical tests and was later shown to belong to serotype O104:H4 – an enteroaggregative *E. coli* (EAEC) that had acquired Shiga toxin genes [2]. This unusual combination highlighted the power of whole‑genome sequencing and bioinformatics for rapid pathogen characterisation. In this project we assembled the genome of *E. coli* X from short (Illumina) and long (PacBio) reads, annotated it, identified its closest relative, located the Shiga toxin genes, and determined the antibiotic resistance profile. The results illustrate how horizontal gene transfer – particularly via bacteriophages and plasmids – can convert a commensal bacterium into a life‑threatening pathogen.

## Methods
### Data acquisition and quality control
Illumina paired‑end reads (SRR292678, 2×400 Mb, insert size 470 bp) and PacBio long reads (SRR1980037, fragment length ~20 kb) were downloaded from the SRA using `fasterq‑dump`. Read quality was assessed with FastQC v0.12.1 (default parameters).
### Genome assembly and evaluation
Two assemblies were generated using SPAdes v4.2.0 [3]:
1. Illumina‑only: `spades.py --isolate -1 forward.fastq -2 reverse.fastq -o spades_output -t 16 -m 32`
2. Hybrid (Illumina + PacBio): `spades.py --isolate -1 forward.fastq -2 reverse.fastq --pacbio SRR1980037.fastq -o hybrid_output -t 16 -m 32`
Assembly quality was compared with QUAST v5.3.0 [4] (default parameters). The hybrid assembly was used for all downstream analyses because if its better quast statistics compared to illumina‑only.
### Genome annotation
The hybrid assembly (`scaffolds.fasta`) was annotated with Bakta v1.12.0 [5] using the full database and specifying genus *Escherichia*, species *coli*. Ribosomal RNA genes were predicted with Barrnap v1.10.5.
### Identification of the closest relative
16S rRNA sequences extracted from the Bakta output were used as query in BLASTn against the RefSeq database restricted to *E. coli* genomes available before 2011 (`1900/01/01:2011/01/01[PDAT]`). The top hit was *E. coli* 55989 (accession NC_011748.1), whose genome was downloaded as reference.
### Shiga toxin gene detection and context analysis
A custom Python script parsed the Bakta GFF3 file to extract all CDS features with their locus tag, product, start, end and length. The resulting table was filtered for “shiga” or “stx” using `grep`. Neighbouring genes around the toxin loci were inspected manually in the GFF3 annotation to identify phage‑associated proteins.
### Antibiotic resistance gene detection
The hybrid assembly (`scaffolds.fasta`) and the reference genome (`55989.fasta`) were submitted to [ResFinder](https://cge.food.dtu.dk/services/ResFinder/) with the “All” antimicrobial configuration. Results were parsed with a second Python script to produce a compact table of resistance genes and the corresponding antibiotics.

All commands, intermediate results, and scripts are documented in the lab journal available at [Laboratory journal repository on GitHub](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/tree/main/task_3)


## Results
### Sequencing data and quality
FastQC reports showed high quality for both Illumina reads and no adapter contamination.
### Genome assembly statistics
The hybrid assembly dramatically improved contiguity compared to the Illumina‑only assembly (Table 1, Figure 1). The hybrid assembly was therefore used for all subsequent analyses.

| Assembly type | # contigs (≥1000 bp) | N50 (bp) |  Total length (bp) |
|---------------|----------------------|----------|--------------------|
| Illumina‑only | 125                  | 114 227  | 5 365 668          |
| Hybrid        | 19                   | 605 269  | 5 476 866          |

Table 1. QUAST metrics for the two assemblies.

![Figure 1. GC content of two assemblies in compare](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/blob/main/task_3/figures/GC.png "Figure 1. GC content of two assemblies in compare")
### Genome annotation
Bakta annotated 5,316,207 bp with 5,102 protein‑coding sequences, 22 rRNA genes, and 86 tRNAs. Among the rRNAs, four copies of 16S rRNA were identified (lengths 1,541–1,542 bp).
### Closest relative of *E. coli* X
BLASTn of the 16S rRNA sequence against the pre‑2011 RefSeq database returned *Escherichia coli* 55989 (NC_011748.1) with 100% identity and 100% coverage. This strain was originally isolated in the Central African Republic from a patient with persistent diarrhoea but without bloody stools.
### Shiga toxin genes and their origin
The toxin genes were identified in the annotation:
- **CJCOGG_03230** – Shiga toxin Stx2 subunit A (length 959 bp)
- **CJCOGG_03231** – Shiga toxin Stx2a subunit B (length 269 bp)
Both genes are located on a single contig. Inspection of the flanking regions (Table 2) revealed a typical prophage organisation: genes encoding a repressor (CI), Cro, antirepressor, antitermination proteins, helicase, primase, terminase subunits, major capsid protein, holin, endolysin, and tail fibre proteins. This cluster of phage‑associated genes strongly indicates that the *stx2* operon was acquired through lysogenic conversion by a bacteriophage.
| Locus tag        | Product                                                       |
|------------------|---------------------------------------------------------------|
| CJCOGG_03218     | Repressor protein CI                                          |
| CJCOGG_03219     | Cro Repressor                                                 |
| CJCOGG_03221     | DEAD/DEAH box helicase                                        |
| CJCOGG_03226     | Antitermination protein                                       |
| **CJCOGG_03230** | **Shiga toxin Stx2 subunit A**                                |
| **CJCOGG_03231** | **Shiga toxin Stx2a subunit B**                               |
| CJCOGG_03236     | Holin                                                         |
| CJCOGG_03237     | SAR‑endolysin                                                 |
| CJCOGG_03243     | Large subunit terminase                                       |
| CJCOGG_03246     | N4‑gp56 family major capsid protein                           |

**Table 2.** Selected genes in the prophage region surrounding the Shiga toxin operon.
### Antibiotic resistance
ResFinder detected 11 acquired resistance genes in *E. coli* X (Table 3). The reference strain 55989 carried only *tet(B)* (tetracycline resistance). The outbreak strain therefore possesses a multidrug‑resistant (MDR) profile.

| Gene           | Antibiotics (phenotype)                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------|
| aph(3'')-Ib    | Streptomycin                                                                                                |
| aph(6)-Id      | Streptomycin                                                                                                |
| blaTEM‑1B      | Amoxicillin, Ampicillin, Cephalothin, Piperacillin, Ticarcillin                                             |
| blaCTX‑M‑15    | Amoxicillin, Ampicillin, Aztreonam, Cefepime, Cefotaxime, Ceftazidime, Ceftriaxone, Piperacillin, Ticarcillin |
| sul1           | Sulfamethoxazole                                                                                            |
| sul2           | Sulfamethoxazole                                                                                            |
| tet(A)         | Doxycycline, Tetracycline                                                                                   |
| dfrA7          | Trimethoprim                                                                                                |

**Table 3.** Acquired resistance genes in *E. coli* X identified by ResFinder.

## Discussion
### How *E. coli* X became pathogenic
The reference strain 55989 is an enteroaggregative *E. coli* (EAEC) that adheres to intestinal cells via pAA‑encoded fimbriae but does not cause bloody diarrhoea. In contrast, *E. coli* X carries two Shiga toxin genes (*stx2A*, *stx2B*) located inside a complete prophage genome. The presence of integrase‑like genes, repressors, structural phage proteins and lysis genes clearly indicates that the toxin genes were acquired by **lysogenic conversion** – a classical horizontal gene transfer mechanism [6]. After integration of the Stx‑encoding phage into the chromosome, the bacterium gained the ability to produce Shiga toxin, which damages the colonic epithelium and leads to HUS.
### Antibiotic resistance acquisition
*E. coli* X harbours a broad set of resistance genes that are absent from the reference strain. The genes are clustered on a single large contig (NODE_4) together with transposases, integrases and plasmid‑related proteins (e.g., RepA, Tra proteins). This organisation suggests that most resistance genes are located on a **multidrug resistance plasmid** or within a composite transposon. The presence of two β‑lactamases (*blaTEM‑1B* and *blaCTX‑M‑15*) explains resistance to penicillins and extended‑spectrum cephalosporins (including cefotaxime and ceftazidime). The combination of *sul1*, *sul2*, *dfrA7*, *tet(A)*, and aminoglycoside phosphotransferases confers resistance to sulfamethoxazole, trimethoprim, tetracyclines, and streptomycin – a typical MDR profile often associated with mobile genetic elements in Enterobacteriaceae.
### Clinical implications and alternative treatment
During the 2011 outbreak, fluoroquinolones (e.g., ciprofloxacin) were avoided because they can induce prophage replication and increase toxin release [7]. Based on the resistance profile, carbapenems (meropenem, imipenem) or tigecycline would be appropriate choices, provided the strain is susceptible (no carbapenemase genes were detected). However, the presence of CTX‑M‑15 precludes the use of most β‑lactams, including ceftriaxone. A reasonable empirical regimen would be **meropenem** combined with supportive care (fluid management, dialysis if needed). The use of azithromycin has also been suggested, but its efficacy against O104:H4 is debated.
### Limitations and further work
We used Bakta instead of Prokka, but both provide comparable annotations. The absence of Mauve alignment due to Java incompatibility did not prevent the identification of the prophage region because we directly inspected the annotated gene neighbourhood. A complete comparative genomics analysis (e.g., using BRIG) could visualise all differences between *E. coli* X and strain 55989, including the exact integration site of the Stx phage and the resistance plasmid.

## Conclusion
We assembled the genome of the 2011 German outbreak strain *E. coli* X, identified its closest relative (55989), located the Shiga toxin genes inside a prophage, and characterised its multidrug resistance profile. The results demonstrate that the strain emerged through horizontal transfer of a Stx‑encoding phage and of several antibiotic resistance genes, most likely on a plasmid. This work underscores the importance of *de novo* assembly and annotation in outbreak investigations and highlights how genomics can guide treatment decisions.

## References
1. Tarr PI, Gordon CA, Chandler WL. Shiga‑toxin‑producing *Escherichia coli* and haemolytic uraemic syndrome. *Lancet*. 2005;365(9464):1073‑86.
2. Rohde H, Qin J, Cui Y, et al. Open‑source genomic analysis of Shiga‑toxin‑producing *E. coli* O104:H4. *N Engl J Med*. 2011;365(8):718‑24.
3. Bankevich A, Nurk S, Antipov D, et al. SPAdes: a new genome assembly algorithm and its applications to single‑cell sequencing. *J Comput Biol*. 2012;19(5):455‑77.
4. Gurevich A, Saveliev V, Vyahhi N, Tesler G. QUAST: quality assessment tool for genome assemblies. *Bioinformatics*. 2013;29(8):1072‑5.
5. Schwengers O, Jelonek L, Dieckmann MA, et al. Bakta: rapid and standardised annotation of bacterial genomes via alignment‑free sequence identification. *Microb Genom*. 2021;7(11):000685.
6. Brüssow H, Canchaya C, Hardt WD. Phages and the evolution of bacterial pathogens: from genomic rearrangements to lysogenic conversion. *Microbiol Mol Biol Rev*. 2004;68(3):560‑602.
7. Zhang X, McDaniel AD, Wolf LE, et al. Quinolone antibiotics induce Shiga toxin‑encoding bacteriophages, toxin production, and death in mice. *J Infect Dis*. 2000;181(2):664‑70.