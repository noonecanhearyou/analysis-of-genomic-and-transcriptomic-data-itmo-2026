<style>
  code {
    font-family: 'Fira Code', 'Consolas', monospace !important;;
    color: #d4d4d4 !important;
  }
  pre {
    background-color: #1e1e1e !important;
    color: #d4d4d4 !important;
  }
</style>

# Integrative Bioinformatics Analysis of the *Ramazzottius varieornatus* Chromatin-Associated Proteome Reveals Novel Candidate DNA-Protective and Repair Proteins
Ivan Uglov, Eugene Fedorov

## Abstract
Tardigrades are renowned for their extraordinary tolerance to ionizing radiation, yet the full repertoire of proteins underpinning this capacity remains incompletely characterized. Here, a computational pipeline was employed to identify candidate DNA-associated proteins in the extremotolerant species *Ramazzottius varieornatus*. Starting with 16,435 predicted proteins and a set of peptides derived from a chromatin-enriched fraction, BLAST-based peptide mapping recovered 32 unique candidates. Subcellular localization prediction, homology searches against Swiss-Prot, and Pfam domain analysis identified nine nuclear-localized proteins. Among these, a zinc finger protein (g5927.t1), a SWI/SNF chromatin remodeler subunit (g7861.t1), and a histone acetyltransferase (g15484.t1) are proposed as high-priority targets for experimental validation of novel DNA-repair or protective mechanisms, complementing the known damage suppressor protein Dsup.

## Introduction
Tardigrades (phylum Tardigrada), commonly known as water bears, are microscopic invertebrates that inhabit a remarkable range of terrestrial and aquatic environments [1]. They are celebrated for their ability to survive environmental extremes that would be lethal to most other metazoans, including desiccation, temperatures from -272°C to over 150°C, pressures exceeding 1,200 atmospheres, and exposure to the vacuum and cosmic radiation of space [2]. This extremotolerance, particularly to ionizing radiation, has made tardigrades a compelling model for understanding fundamental mechanisms of DNA protection and repair.

For decades, the molecular basis of this resilience remained elusive. A pivotal advance came with the sequencing and analysis of the *Ramazzottius varieornatus* genome, which led to the discovery of the tardigrade-unique DNA-associating protein Dsup (Damage suppressor) [3]. Heterologous expression of Dsup in human cells significantly attenuated X-ray-induced DNA damage, demonstrating that tardigrades possess unique, potent proteins capable of directly shielding chromatin [3]. More recently, additional factors such as the radiation-inducible DNA-binding protein TDR1 have been identified, suggesting a multi-layered strategy that integrates both constitutive protection and active repair [4, 5].

Despite these breakthroughs, the full complement of *R. varieornatus* proteins involved in DNA-centric stress responses remains to be fully elucidated. In this study, it was hypothesized that the chromatin fraction of tardigrade cells contains novel, functionally relevant proteins that either protect DNA from damage or facilitate its efficient repair. To address this, experimentally derived chromatin-associated peptide data were integrated with a suite of computational prediction tools to identify and prioritize candidate proteins for future experimental verification.

## Methods
### Genome Data and Proteome Retrieval
The predicted proteome of *Ramazzottius varieornatus* strain YOKOZUNA-1 was obtained from precomputed AUGUSTUS results based on the NCBI genome assembly GCA_001949185.1 [6]. The total number of predicted protein sequences was determined to be 16,435, a figure consistent with the expected gene count for a multicellular eukaryote.

### Identification of Chromatin-Associated Proteins
A list of peptide sequences obtained via tandem mass spectrometry from a chromatin-enriched fraction of *R. varieornatus* was provided. To map these peptides back to their parent proteins, a local BLAST database was constructed from the predicted proteome using `makeblastdb` (BLAST+ suite, version 2.16.0) [7]. The peptide query file was searched against this database using `blastp` with default parameters and tabular output (`-outfmt 6`). Unique protein identifiers corresponding to all peptide hits were extracted, and their full-length sequences were retrieved using `seqtk subseq` [8]. No E-value threshold was applied during this initial mapping step to capture all potential chromatin-associated proteins.

### Subcellular Localization Prediction
To identify proteins with a high likelihood of nuclear residence, two complementary web-based tools were employed. WoLF PSORT [9] was used to predict subcellular localization based on integrated sorting signals and compositional features. Additionally, TargetP 2.0 [10] was used to detect N-terminal targeting peptides—specifically signal peptides (SP) and mitochondrial transit peptides (mTP)—the presence of which would argue against a nuclear or chromatin-associated function. Both tools were run with default parameters.

### Homology and Domain Annotation
Functional annotation was performed by querying each candidate sequence against the manually curated UniProtKB/Swiss-Prot database using the NCBI BLAST web server. The best hit for each protein was recorded, including the annotation, E-value, percent identity, and queryAlmagro Armenteros, J. J., Salvatore, M., Emanuelsson, O., Winther, O., von Heijne, G., Elofsson, A., & Nielsen, H. (2019). Detecting sequence signals in targeting peptides using deep learning. *Life Science Alliance*, 2(5), e201900429. coverage. Protein domain architectures were predicted by searching against the Pfam database of profile hidden Markov models (HMMs) using the `hmmscan` tool on the EMBL-EBI HMMER web server [11]. Default parameters were used for both analyses.

### Data Integration and Candidate Prioritization
The results from BLAST homology searches, Pfam domain predictions, WoLF PSORT localization, and TargetP 2.0 predictions were compiled into a single table.

## Results
All commands, intermediate results, and scripts are documented in the lab journal available at [Laboratory journal repository on GitHub](https://github.com/noonecanhearyou/analysis-of-genomic-and-transcriptomic-data-itmo-2026/tree/main/task_4).

### Identification of Chromatin-Associated Candidates
From the initial set of 16,435 predicted proteins, BLASTP mapping of the mass spectrometry-derived peptides identified **32 unique proteins** as being physically associated with the chromatin fraction. The sequences of these 32 candidates were extracted for downstream analyses.

### Subcellular Localization Predictions
WoLF PSORT analysis predicted diverse localizations for the candidate set. Notably, nine proteins (g5927.t1, g7861.t1, g8100.t1, g8312.t1, g10513.t1, g10514.t1, g11806.t1, g11960.t1, g15484.t1, g16318.t1, g16368.t1) received a nuclear or cyto-nuclear localization score. TargetP 2.0 identified a signal peptide (SP) in ten candidates, suggesting they are targeted for secretion and thus unlikely to function as direct DNA-protective factors within the nucleus.

### Homology and Domain Analysis
A BLAST search against the Swiss-Prot database yielded significant hits (E-value < 1e-5) for 22 of the 34 candidates. The remaining 12 proteins showed no significant similarity to characterized proteins, indicating they may be novel or rapidly evolving tardigrade-specific factors. A subset of the annotated proteins with clear nuclear association is highlighted below:
- **g5927.t1**: Zinc finger protein ZFP-1 (*E*=1.08e-18), a classic DNA-binding domain-containing protein.
- **g7861.t1**: SWI/SNF complex component (*E*=1.57e-71), an ATP-dependent chromatin remodeler essential for DNA repair and transcription.
- **g15484.t1**: Histone acetyltransferase (*E*=0.0), an enzyme that modifies chromatin structure to regulate DNA accessibility.
- **g11960.t1**: Nuclear protein (*E*=6.23e-98), an uncharacterized protein with a strong nuclear localization signal.

Pfam domain analysis using HMMER identified conserved domains in only a few proteins, including chitin-binding Peritrophin-A domains in g702.t1 and g1285.t1, and glycosyl hydrolase domains in g2203.t1. The absence of detectable domains in the majority of candidates may reflect sequence divergence in tardigrades or limitations of current domain models.

A consolidated summary of all 34 candidates is provided in **Table 1**.

**Table 1. Integrated Functional Annotation and Localization Predictions for Chromatin-Associated *R. varieornatus* Proteins.**
|Protein ID|Best BLAST hit (annotation, e-value)|Predicted Pfam domains|Probable localization(s) (WoLF PSORT)|Localization (TargetP-2.0)|
|---|---|---|---|---|
|g702.t1|Uncharacterized protein P0DPW4.1 (e=1.50e-11)|Chitin binding Peritrophin-A domain|extracellular (29), plasma membrane (2), lysosome (1)|Signal peptide
|g1285.t1|Uncharacterized protein P0DPW4.1 (e=1.79e-12)|Chitin binding Peritrophin-A domain|extracellular (25), plasma membrane (5)|Signal peptide|
|g2203.t1|Putative glucosidase GANAB (Q69ZQ1.2, e=2.44e-126)|Glycosyl hydrolases family 31 TIM-barrel domain, Glycosyl hydrolase family 31 C-terminal domain|plasma membrane (29), nucleus (2)|Other|
|g3428.t1|Myosin regulatory light chain 2 (Q09510.1, e=8.78e-65)|EF-hand domain pair|mitochondria (18), cytoplasm (11)|Other
|g3679.t1|Uncharacterized protein (Q19269.2, e=7.44e-22)|Fill in|extracellular (26), mitochondria (2)|Signal peptide
|g4106.t1|No significant hits found|Fill in|ER (14.5), ER/Golgi (9.5), extracellular (7)|Other
|g4970.t1|LDLRAD3 (Q9JIQ8.3, e=1.38e-15)|Fill in|plasma membrane (32)|Other
|g5237.t1|No significant hits found|Fill in|plasma membrane (24), mitochondria (8)|Other
|g5443.t1|No significant hits found|Fill in|extracellular (28), nucleus (3)|Other
|g5467.t1|Uncharacterized protein P0DPW4.1 (e=3.92e-13)|Fill in|extracellular (27), plasma membrane (4)|Signal peptide
|g5502.t1|Uncharacterized protein P0DPW4.1 (e=5.84e-14)|Fill in|extracellular (31)|Signal peptide
|g5503.t1|Uncharacterized protein P0DPW4.1 (e=6.75e-14)|Fill in|extracellular (29)|Signal peptide
|g5510.t1|No significant hits found|Fill in|plasma membrane (23), mitochondria (7)|Other
|g5616.t1|Uncharacterized protein P0DPW4.1 (e=2.25e-14)|Fill in|extracellular (31)|Signal peptide
|g5641.t1|Uncharacterized protein P0DPW4.1 (e=5.12e-13)|Fill in|extracellular (31)|Signal peptide
|g5927.t1|Zinc finger protein ZFP-1 (Q17427.1, e=1.08e-18)|Fill in|nucleus (30.5), cyto_nucl (16.5)|Other
|g7861.t1|SWI/SNF complex component (B4F769.1, e=1.57e-71)|Fill in|nucleus (16), cyto_nucl (14), cytoplasm (8)|Other
|g8100.t1|Uncharacterized protein (Q2YDR3.1, e=3.01e-46)|Fill in|nucleus (16.5), cyto_nucl (12.5), cytoplasm (7.5)|Other
|g8312.t1|V-type proton ATPase subunit (Q5KU39.1, e=0.0)|Fill in|nucleus (15.5), cyto_nucl (15.5), cytoplasm (12.5)|Other
|g10513.t1|No significant hits found|Fill in|nucleus (20), cyto_nucl (14.5), cytoplasm (7)|Other
|g10514.t1|No significant hits found|Fill in|nucleus (19), cyto_nucl (15), cytoplasm (9)|Other
|g11320.t1|No significant hits found|Fill in|plasma membrane (24.5), extr_plas (16)|Signal peptide
|g11513.t1|Uncharacterized protein (Q32PH0.1, e=6.72e-83)|Fill in|cytoplasm (17), cyto_nucl (12.8), cyto_mito (9.8)|Other
|g11806.t1|No significant hits found|Fill in|nucleus (18), cyto_nucl (11.8), mitochondria (5)|Other
|g11960.t1|Nuclear protein (Q8CJB9.1, e=6.23e-98)|Fill in|nucleus (32)|Other
|g12388.t1|Uncharacterized protein P0DPW4.1 (e=2.77e-11)|Fill in|extracellular (25), plasma membrane (4)|Signal peptide
|g12510.t1|No significant hits found|Fill in|plasma membrane (29), cytoplasm (3)|Other
|g12562.t1|Uncharacterized protein P0DPW4.1 (e=7.17e-13)|Fill in|extracellular (30)|Signal peptide
|g13530.t1|No significant hits found|Fill in|extracellular (13), nucleus (6.5), lysosome (5)|Signal peptide
|g14472.t1|Identical to P0DOW4.1 (e=0.0, 100% identity)|Fill in|nucleus (28), plasma membrane (2)|Other
|g15153.t1|Uncharacterized protein P0DPW4.1 (e=1.89e-14)|Fill in|extracellular (32)|Signal peptide
|g15484.t1|Histone acetyltransferase (Q155U0.1, e=0.0)|Fill in|nucleus (17.5), cyto_nucl (15.3), cytoplasm (12)|Other
|g16318.t1|No significant hits found|Fill in|nucleus (20.5), cyto_nucl (13), extracellular (5)|Other
|g16368.t1|No significant hits found|Fill in|nucleus (20.5), cyto_nucl (13), extracellular (5)|Other

## Discussion
The objective of this study was to leverage a multi-tiered computational approach to identify novel proteins from *R. varieornatus* that may contribute to its exceptional radiotolerance. By anchoring the analysis in experimentally derived chromatin-associated peptides, the candidate pool was enriched for proteins with a high probability of direct DNA interaction.

The pipeline successfully recovered the well-characterized damage suppressor protein **Dsup (g14472.t1)** with perfect sequence identity and a strong nuclear localization prediction, thereby validating the experimental and computational workflow. While Dsup is a known factor, its detection confirms the utility of chromatin enrichment for identifying DNA-protective proteins.

Among the remaining 33 proteins, candidates were prioritized based on two criteria: (1) a predicted nuclear localization by WoLF PSORT, and (2) functional homology to proteins known to participate in DNA metabolism or chromatin biology. Three proteins emerged as high-priority targets for experimental verification:

1.  **g5927.t1 (Zinc finger protein ZFP-1)**: Zinc finger domains are among the most common DNA-binding motifs in eukaryotes and are involved in transcriptional regulation and DNA repair [12]. The strong nuclear localization signal and homology to a known zinc finger protein make g5927.t1 a compelling candidate for a novel DNA-binding factor that may recognize specific DNA lesions or recruit repair machinery.
2.  **g7861.t1 (SWI/SNF complex component)**: The SWI/SNF family of ATP-dependent chromatin remodelers uses the energy of ATP hydrolysis to alter nucleosome positioning, thereby regulating access to DNA for transcription, replication, and repair [13]. The presence of a SWI/SNF subunit in the chromatin fraction suggests a potential role in facilitating DNA damage signaling or repair by modulating chromatin compaction in response to radiation stress.
3.  **g15484.t1 (Histone acetyltransferase)**: Histone acetylation is a key post-translational modification that relaxes chromatin structure and promotes the recruitment of DNA repair proteins [14]. This enzyme could be involved in creating a permissive chromatin environment for efficient homologous recombination or non-homologous end joining following radiation-induced double-strand breaks.

A notable subset of candidates (e.g., g702.t1, g1285.t1, g5467.t1) showed homology to the uncharacterized protein P0DPW4.1 and were predicted to be extracellular or possess signal peptides. While these proteins may represent secreted factors involved in cuticle formation or stress signaling, their predicted localization makes a direct role in DNA protection unlikely. It is recommended that these proteins be de-prioritized in initial DNA-centric experimental validations. Similarly, proteins such as the V-type ATPase subunit (g8312.t1) may represent false positives from the chromatin enrichment or have moonlighting functions; further evidence would be required to support their involvement in DNA repair.

The findings presented here align with and extend the current model of tardigrade radiotolerance. While Dsup acts as a constitutive physical shield [3], the candidates identified here - a zinc finger protein, a chromatin remodeler, and a histone acetyltransferase—point toward active, regulated mechanisms of chromatin management and DNA repair. This is consistent with the recent discovery of TDR1, an inducible DNA-binding protein that promotes repair [4], and supports the notion that tardigrades employ a layered defense strategy.

**Limitations and Future Directions.** This study is inherently computational and relies on sequence-based predictions. The absence of Pfam domain hits in most candidates may be due to the high evolutionary divergence of tardigrade proteins, which are not well represented in current domain databases. To validate these findings, the following experiments are proposed:
- **In vitro DNA-binding assays** (e.g., electrophoretic mobility shift assays) for recombinant g5927.t1, g7861.t1, and g15484.t1 to confirm direct DNA interaction.
- **Heterologous expression** in radiation-sensitive model systems (e.g., *E. coli* or human cell lines) to test for radioprotective phenotypes.

Furthermore, transcriptomic analysis of *R. varieornatus* under radiation stress could reveal whether the genes encoding these candidates are constitutively expressed or induced upon DNA damage, providing additional functional clues.

## References
1. Nelson, D. R., Guidetti, R., & Rebecchi, L. (2015). Phylum Tardigrada. In *Thorp and Covich's Freshwater Invertebrates* (pp. 347-380). Academic Press.
2. Jönsson, K. I., & Harms-Ringdahl, M. (2019). Radiation Tolerance in Tardigrades: Current Knowledge and Potential Applications in Medicine. *Cancers*, 11(9), 1333.
3. Hashimoto, T., Horikawa, D. D., Saito, Y., Kuwahara, H., Kozuka-Hata, H., Shin-I, T., ... & Kunieda, T. (2016). Extremotolerant tardigrade genome and improved radiotolerance of human cultured cells by tardigrade-unique protein. *Nature Communications*, 7, 12808.
4. Anoud M, Delagoutte E, Helleu Q, Brion A, Duvernois-Berthet E, As M, Marques X, Lamribet K, Senamaud-Beaufort C, Jourdren L, Adrait A, Heinrich S, Toutirais G, Hamlaoui S, Gropplero G, Giovannini I, Ponger L, Geze M, Blugeon C, Couté Y, Guidetti R, Rebecchi L, Giovannangeli C, De Cian A, Concordet JP. Comparative transcriptomics reveal a novel tardigrade-specific DNA-binding protein induced in response to ionizing radiation. Elife. 2024 Jul 9;13:RP92621. doi: 10.7554/eLife.92621. PMID: 38980300; PMCID: PMC11233135.
5. Møbjerg, N., & Neves, R. C. (2021). New insights into survival strategies of tardigrades. *Comparative Biochemistry and Physiology Part A: Molecular & Integrative Physiology*, 254, 110890.
6. Stanke, M., & Morgenstern, B. (2005). AUGUSTUS: a web server for gene prediction in eukaryotes that allows user-defined constraints. *Nucleic Acids Research*, 33(Web Server issue), W465-W467.
7. Altschul, S. F., Gish, W., Miller, W., Myers, E. W., & Lipman, D. J. (1990). Basic local alignment search tool. *Journal of Molecular Biology*, 215(3), 403-410.
8. Li, H. (2013). Seqtk: a fast and lightweight tool for processing FASTA or FASTQ sequences. [https://github.com/lh3/seqtk](https://github.com/lh3/seqtk)
9. Horton, P., Park, K. J., Obayashi, T., & Nakai, K. (2006). Protein Subcellular Localization Prediction with WoLF PSORT. *Proceedings of the 4th Asia-Pacific Bioinformatics Conference*, 39-48.
10. Almagro Armenteros, J. J., Salvatore, M., Emanuelsson, O., Winther, O., von Heijne, G., Elofsson, A., & Nielsen, H. (2019). Detecting sequence signals in targeting peptides using deep learning. *Life Science Alliance*, 2(5), e201900429.
11. Potter, S. C., Luciani, A., Eddy, S. R., Park, Y., Lopez, R., & Finn, R. D. (2018). HMMER web server: 2018 update. *Nucleic Acids Research*, 46(W1), W200-W204.
12. Cassandri, M., Smirnov, A., Novelli, F., Pitolli, C., Agostini, M., Malewicz, M., ... & Raschellà, G. (2017). Zinc-finger proteins in health and disease. *Cell Death Discovery*, 3, 17071.
13. Clapier, C. R., & Cairns, B. R. (2009). The biology of chromatin remodeling complexes. *Annual Review of Biochemistry*, 78, 273-304.
14. Sterner, D. E., & Berger, S. L. (2000). Acetylation of histones and transcription-related factors. *Microbiology and Molecular Biology Reviews*, 64(2), 435-459.