# Updated and comprehensive variant analysis pipeline
pipeline_steps = [
    {
        "Step": "1. Data Retrieval",
        "Tool/Method": "NCBI SRA Toolkit / Galaxy EU",
        "Details": "Download 5 human sequence samples (FASTQ) via SRA accessions."
    },
    {
        "Step": "2. Quality Control",
        "Tool/Method": "FastQC + Trimmomatic",
        "Details": "Assess raw-read quality and trim adapters/low-quality bases."
    },
    {
        "Step": "3. Genome Indexing",
        "Tool/Method": "HISAT2 / STAR",
        "Details": "Prepare hg38 reference index (or select pre-indexed)."
    },
    {
        "Step": "4. Read Alignment",
        "Tool/Method": "RNA STAR",
        "Details": "Map reads to reference and generate sorted/indexed BAMs."
    },
    {
        "Step": "5. Variant Calling",
        "Tool/Method": "FreeBayes",
        "Details": "Call SNPs/indels on BAMs to produce a raw VCF."
    },
    {
        "Step": "6. VCF Parsing & Summary",
        "Tool/Method": "Python + pandas",
        "Details": "Extract CHROM, POS, REF, ALT, QUAL, DP, AF, AC, MQM, SAP, SRP, RO, AO, ODDS into a summary table."
    },
    {
        "Step": "7. Inspect Annotation Tags",
        "Tool/Method": "Manual + Python",
        "Details": "Check whether SnpEff used `ANN=` or legacy `EFF=` in INFO."
    },
    {
        "Step": "8. Functional Annotation with SnpEff",
        "Tool/Method": "SnpEff (Galaxy EU)",
        "Details": "Annotate VCF (GRCh38.86) to add gene, codon change, impact, etc."
    },
    {
        "Step": "9. Parse SnpEff EFF Field",
        "Tool/Method": "Python + pandas",
        "Details": "Extract Effect, Impact, Gene_ID, Gene_Name, Feature_ID, Codon changes from `EFF=`."
    },
    {
        "Step": "10. Merge Summaries & Annotations",
        "Tool/Method": "pandas.merge",
        "Details": "Join FreeBayes summary and SnpEff annotation on CHROM/POS/REF/ALT."
    },
    {
        "Step": "11. Data Cleaning",
        "Tool/Method": "pandas",
        "Details": "Drop incomplete rows, coerce to numeric, fill NAs, save cleaned CSV."
    },
    {
        "Step": "12. Visualization",
        "Tool/Method": "matplotlib + seaborn",
        "Details": "Generate correlation heatmap for coverage, quality, frequencies, bias metrics."
    },
    {
        "Step": "13. Export Outputs",
        "Tool/Method": "pandas + filesystem",
        "Details": "Save final tables (CSV/Excel) and figures (PNG) for reports."
    },
    {
        "Step": "14. Optional Enrichment Analysis",
        "Tool/Method": "g:Profiler / Enrichr",
        "Details": "Perform pathway/GO analysis on high-impact genes."
    },
    {
        "Step": "15. Optional Browser Review",
        "Tool/Method": "IGV / JBrowse",
        "Details": "Visualize specific variants in their genomic context."
    },
    {
        "Step": "16. Reporting & Documentation",
        "Tool/Method": "Manual + Galaxy Histories",
        "Details": "Compile narrative, tables, and figures into a final manuscript or presentation."
    }
]
