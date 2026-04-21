# Genomic Analysis of Ampicillin Resistance Mechanisms in Escherichia coli
Ivan Uglov, Eugene Fedorov

## Abstract
Antibiotic resistance poses a significant threat to modern healthcare. In this study, whole-genome sequencing data of an ampicillin-resistant *Escherichia coli* strain were analyzed to identify mutations responsible for resistance. A bioinformatics pipeline including quality control, trimming, alignment, variant calling, and annotation was applied. Several mutations affecting protein-coding genes (*ftsI*, *acrB*, *envZ*, *mntP*) were identified. These genes are associated with antibiotic target modification, efflux activity, and membrane permeability. The results suggest a multifactorial resistance mechanism and provide insights for alternative treatment strategies.

## Introduction
Antibiotic resistance is one of the most pressing challenges in modern medicine, limiting the effectiveness of commonly used drugs and increasing the risk of treatment failure. Bacteria can develop resistance through multiple mechanisms, including modification of antibiotic targets, increased efflux of drugs, enzymatic degradation, and reduced membrane permeability [1].

β-lactam antibiotics such as ampicillin act by binding to penicillin-binding proteins (PBPs), which are essential for bacterial cell wall synthesis. Mutations in these proteins or in regulatory pathways can reduce antibiotic binding and confer resistance [2]. Additionally, multidrug efflux systems and membrane porin regulation are known to play critical roles in resistance phenotypes [3].

In this study, we analyzed sequencing data from an ampicillin-resistant *E. coli* strain to identify mutations responsible for resistance. The objective was to determine the functional effects of these mutations and propose possible mechanisms of resistance, as well as potential treatment strategies.

## Methods
Sequencing data for an ampicillin-resistant *E. coli* strain were obtained from Figshare (DOI: 10.6084/m9.figshare.10006541.v3). The reference genome used was *E. coli* K-12 MG1655 (NCBI accession: GCF_000005845.2).

Quality control was performed using FastQC [4], and read statistics were obtained using SeqKit. Reads were trimmed using fastp with quality thresholds (Q20 and Q30) and minimum read length of 20 bp.

Trimmed reads were aligned to the reference genome using BWA-MEM [5]. Alignments were processed using SAMtools [6] (conversion to BAM, sorting, indexing, and alignment statistics). Variant calling was performed using VarScan [7] with a minimum variant frequency threshold of 0.20.

Variant annotation and effect prediction were conducted using SnpEff [8] with a custom-built database. A custom AWK script was used to extract relevant fields (position, gene, mutation type, impact, and amino acid change) into a tabular format.

All commands, intermediate results, and scripts are documented in the lab journal available at [Laboratory journal repository on GitHub](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/tree/main/task_2)

## Results
### Sequencing and alignment statistics
Initial quality control indicated acceptable sequencing quality. Trimming improved read quality by removing low-quality bases.
FastQC reports and FastP statistics are available in the laboratory journal.

### Identified mutations and their functional effects

| Position | Gene | Type | Impact | Protein change |
|----------|------|------|--------|----------------|
| 93043 | ftsI | missense_variant | MODERATE | Ala544Gly |
| 482698 | acrB | missense_variant | MODERATE | Gln569Leu |
| 1905761 | mntP | missense_variant | MODERATE | Gly25Asp |
| 3535147 | envZ | missense_variant | MODERATE | Val241Gly |
| 4390754 | rsgA | synonymous_variant | LOW | Ala252Ala |
| 852762 | intergenic | upstream_gene_variant | MODIFIER | — |

### Gene function analysis

- *ftsI* — encodes penicillin-binding protein 3 (PBP3), essential for cell wall synthesis and a direct target of β-lactam antibiotics [2]  
- *acrB* — encodes a component of the AcrAB-TolC multidrug efflux pump, exporting antibiotics out of the cell [3]  
- *envZ* — encodes a sensor kinase regulating the EnvZ/OmpR system, which controls outer membrane porins  
- *mntP* — encodes a manganese efflux protein involved in metal homeostasis  
- *rsgA* — encodes a ribosome-associated GTPase; synonymous mutation likely has no functional effect  

---

## Discussion
The results indicate that antibiotic resistance in this *E. coli* strain is likely driven by multiple mechanisms.

The mutation in *ftsI* suggests target modification, reducing antibiotic binding to penicillin-binding proteins. The mutation in *acrB* indicates increased efflux activity, potentially enhancing antibiotic export. The mutation in *envZ* may alter membrane permeability by regulating porin expression and reducing antibiotic uptake.

Together, these mutations represent three classical resistance mechanisms:
1. Target modification (*ftsI*)  
2. Drug efflux (*acrB*)  
3. Reduced permeability (*envZ*)  

The mutation in *mntP* may contribute indirectly through stress response or ion homeostasis, but its role remains unclear.

A limitation of this study is that functional effects are predicted computationally. Experimental validation is required to confirm these findings.

### Treatment recommendations
Based on the identified resistance mechanisms, β-lactam antibiotics such as ampicillin may be ineffective.

Possible alternatives include:
- Fluoroquinolones (target DNA gyrase)  
- Aminoglycosides (target ribosome function)  
- Tetracyclines (inhibit protein synthesis)  

Combination therapy with efflux pump inhibitors may further improve treatment effectiveness.

## References

1. Blair J.M.A. et al. (2015). Molecular mechanisms of antibiotic resistance. *Nature Reviews Microbiology*. https://doi.org/10.1038/nrmicro3380  
2. Sauvage E. et al. (2008). The penicillin-binding proteins. *FEMS Microbiology Reviews*. https://doi.org/10.1111/j.1574-6976.2008.00105.x  
3. Nikaido H. (2009). Multidrug resistance in bacteria. *Annual Review of Biochemistry*. https://doi.org/10.1146/annurev.biochem.78.082907.145923  
4. FastQC: http://www.bioinformatics.babraham.ac.uk/projects/fastqc/  
5. Li H. (2013). BWA-MEM. https://arxiv.org/abs/1303.3997  
6. Li H. et al. (2009). SAMtools. https://doi.org/10.1093/bioinformatics/btp352  
7. Koboldt D.C. et al. (2012). VarScan 2. https://doi.org/10.1101/gr.129684.111  
8. Cingolani P. et al. (2012). SnpEff. https://doi.org/10.4161/fly.19695  