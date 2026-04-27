# Genomic Characterization and Targeted Trait Optimization Based on 23andMe SNP Data

## Abstract
The analysis of single nucleotide polymorphisms (SNPs) enables extraction of biologically and clinically relevant information from consumer genomic data. In this study, 23andMe genotyping data were analyzed to determine ancestry, basic phenotypic traits, and selected functional variants. The subject was assigned to mitochondrial haplogroup H(T152C) and Y-chromosome haplogroup R1a1a, consistent with Eastern European origin. Eye color was predicted as brown, and lactose intolerance was inferred based on the rs4988235 genotype.
## Introduction
The human genome contains a large number of single nucleotide polymorphisms (SNPs), many of which are associated with phenotypic traits or disease susceptibility. Advances in genotyping technologies, such as SNP arrays used by consumer services, enable rapid identification of hundreds of thousands of variants across the genome. These datasets can be used to infer ancestry, predict physical traits, and assess genetic predispositions.

SNPs can be divided into two main categories: linked variants, which serve as markers associated with specific traits, and causative variants, which directly affect gene function or regulation. Functional interpretation of SNPs is supported by databases such as ClinVar and GWAS Catalog, which link genetic variation to phenotypic outcomes.

## Methods
Raw genotyping data obtained from 23andMe dataset were used in this study. The data correspond to the GRCh37 human genome assembly.

The dataset was converted into Variant Call Format (VCF) using PLINK [1], with filtering applied to retain only single nucleotide variants (A/C/G/T). Non-polymorphic positions identical to the reference genome were excluded to focus on informative.

Ancestry analysis was performed using external tools. Mitochondrial haplogroup assignment was carried out using the mthap service, while Y-chromosome haplogroup determination was performed using Morley Y-SNP tree tools.

Phenotypic traits were inferred from known SNPs. Eye color prediction was based on established variants described in the literature [2], particularly rs12913832 and related loci. Lactose intolerance was assessed using SNP rs4988235, located in a regulatory region controlling expression of the *LCT* gene [3].

Relevant SNPs were extracted using command-line filtering, and their biological significance was interpreted based on published studies and databases.

## Results
All commands, intermediate results, and scripts are documented in the lab journal available at [Laboratory journal repository on GitHub](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/tree/main/task_5).
### Ancestry analysis
The mitochondrial haplogroup was identified as **H(T152C)**, and the Y-chromosome haplogroup as **R1a1a (R-M198)**. These haplogroups are characteristic of Eastern and Central European populations according to [eupedia.com](https://www.eupedia.com/europe/european_y-dna_haplogroups.shtml).

### Sex determination
The presence of Y-chromosome variants indicates that the subject is genetically male.

### Eye color prediction
Analysis of pigmentation-associated SNPs predicted brown eye color, consistent with known genotype–phenotype relationships [2].

### Lactose intolerance
The genotype at SNP **rs4988235** suggests **lactose intolerance**. This variant is located in an enhancer region regulating *LCT* gene expression.


## Discussion
The results demonstrate that consumer genotyping data can be used to extract biologically meaningful and consistent information. The identified haplogroups correspond to known distributions in Eastern European populations, supporting the reliability of the ancestry inference.

The prediction of lactose intolerance is based on a well-characterized regulatory variant affecting *LCT* expression. The non-persistent allele leads to reduced lactase production in adulthood, resulting in impaired lactose digestion. This represents a clear example of a functional non-coding variant with a strong phenotypic effect.

## References
  
1. Purcell S. et al. (2007). PLINK: a tool set for whole-genome association and population-based linkage analyses. *AJHG*. https://doi.org/10.1086/519795  
2. Hart KL, Kimura SL, Mushailov V, Budimlija ZM, Prinz M, Wurmbach E. Improved eye- and skin-color prediction based on 8 SNPs. Croat Med J. 2013 Jun;54(3):248-56. doi: 10.3325/cmj.2013.54.248. PMID: 23771755; PMCID: PMC3694299. 
3. Enattah NS, Sahi T, Savilahti E, Terwilliger JD, Peltonen L, Järvelä I. Identification of a variant associated with adult-type hypolactasia. Nat Genet. 2002 Feb;30(2):233-7. doi: 10.1038/ng826. Epub 2002 Jan 14. PMID: 11788828.