import scanpy as sc 

WEIGHT = 15

GENE_SETS = {
    "TLS": {
        "names": [
            'CD4', 'CD8A', 'CD74', 'CD79A', 'IL7R', 'ITGAE', 'CD1D', 
            'CD3D', 'CD3E', 'CD8B', 'CD19', 'CD22', 'CD52', 'CD79B', 
            'CR2', 'CXCL13', 'CXCR5', 'FCER2', 'MS4A1', 
            'PDCD1', 'PTGDS', 'TRBC'
        ],
        "weight": WEIGHT,
        "categories": "TLS"
    },
    "REACTOME_METABOLISM_OF_LIPIDS": {
        "names": [
            "AGPAT3", "LPIN3", "TAZ", "PLD1", "PNPLA8",
            "LCLAT1", "PISD", "PLBD1", "PITPNM3", "MTM1",
            "PI4K2B", "HADH", "MMUT", "PCCB", "MECR",
            "MCAT", "DECR2", "ELOVL6", "ALOX12B", "FDXR",
            "TBL1X", "MTF1", "NFYC", "HSD17B1", "DHRS7B",
            "MED21"
        ],
        "weight": WEIGHT,
        "categories": "CC"
    },
    "REACTOME_GLYCEROPHOSPHOLIPID_BIOSYNTHESIS": {
        "names": [
            "AGPAT3", "LPIN3", "TAZ", "PLD1", "PNPLA8", "LCLAT1", 
            "PISD", "PLBD1", "PITPNM3"
        ],
        "weight": WEIGHT,
        "categories": "CC"
    },
    "REACTOME_PHOSPHOLIPID_METABOLISMREACTOME_PHOSPHOLIPID_METABOLISM": {
        "names": [
            "AGPAT3", "LPIN3", "TAZ", "PLD1", "PNPLA8",
            "LCLAT1", "PISD", "PLBD1", "PITPNM3", "MTM1",
            "PI4K2B"
        ],
        "weight": WEIGHT,
        "categories": "CC"
    },
    "REACTOME_MITOCHONDRIAL_FATTY_ACID_BETA_OXIDATION": {
        "names": [
            "HADH", "MMUT", "PCCB", "MECR", "MCATHADH",
            "MMUT", "PCCB", "MECR", "MCAT"
        ],
        "weight": WEIGHT,
        "categories": "CC"
    },
    "REACTOME_VESICLE_MEDIATED_TRANSPORT": {
        "names": [
            "AGPAT3", "TUBB4A", "KIF23", "RAB8A", "KIFWEIGHTB",
            "NBAS", "BET1L", "SYS1", "EPGN", "VPS37A",
            "DENND2C", "DENND1B", "MON1A", "EPS15L1",
            "AP1M2", "COPS7A", "FCHO2", "EXOC3"
        ],
        "weight": WEIGHT,
        "categories": "CC"
    },
    "REACTOME_SIGNALING_BY_RETINOIC_ACID": {
        "names": [
            "DHRS4", "PDHB", "PDK2", "DHRS3", "RDH14"
        ],
        "weight": WEIGHT,
        "categories": "CC"
    },
    "REACTOME_CELL_CYCLE_MITOTIC": {
        "names": [
            "LPIN3", "TUBB4A", "KIF23", "RAB8A", "LIG1",
            "FEN1", "CENPF", "SEH1L", "ZWINT", "DHFR",
            "CDC23", "ANAPC15", "TFDP2", "CKS1B",
            "PPP2R3B"
        ],
        "weight": WEIGHT,
        "categories": "CC"
    },
    "REACTOME_FATTY_ACID_METABOLISM": {
        "names": [
            "HADH", "MMUT", "PCCB", "MECR", "MCAT",
            "DECR2", "ELOVL6", "ALOX12B"
        ],
        "weight": WEIGHT,
        "categories": "CC"
    },
    "REACTOME_METABOLISM_OF_AMINO_ACIDS_AND_DERIVATIVES": {
        "names": [
            "PDHB", "PXMP2", "GSTZ1", "CKB", "ALDH9A1",
            "BBOX1", "ALDH4A1", "PYCR3", "SLC25A10",
            "GPT2", "ASPG"
        ],
        "weight": WEIGHT,
        "categories": "CC"
    },
    "HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION": {
        "names": [
            "THY1","CAPG","VCAM1","SDC1","LUM","LOXL1","LOXL2","PCOLCE","FBLN1","BGN","IL32","TGFBI","FSTL1","SFRP4"
        ],
        "weight": WEIGHT,
        "categories": "CE"
    },
    "REACTOME_EXTRACELLULAR_MATRIX_ORGANIZATION": {
        "names": [
            "ITGAL","MMP9","VCAM1","SDC1","LUM","LOXL1","LOXL2","PCOLCE","FBLN1","BGN","PECAM1","VWF","COL6A1","LTBP2","LAMB2"
        ],
        "weight": WEIGHT,
        "categories": "CE"
    },
    "BIOCARTA_TCYTOTOXIC_PATHWAY": {
        "names": [
            "THY1","ITGAL","CD8A","CD2","CD3E"
        ],
        "weight": WEIGHT,
        "categories": "CE"
    },
    "REACTOME_ADAPTIVE_IMMUNE_SYSTEM": {
        "names": [
            "ITGAL","CD8A","HLA-DOA","CD3E","PRKCB","FYB1","VCAM1","CD22","C3","PLCG2","TAB2","FCGR1B","SLAMF7","LILRB2","LAIR1","BLK","ANAPC2","LAG3"
        ],
        "weight": WEIGHT,
        "categories": "CE"
    },
    "REACTOME_CYTOKINE_SIGNALING_IN_IMMUNE_SYSTEM": {
        "names": [
            "MMP9","IL4R","IL2RB","CCL19","IRF8","VCAM1","SDC1","IL32","TAB2","FCGR1B","IL10RA","CEBPD","LGALS9","TNFSF13B","CD27","SAMHD1"
        ],
        "weight": WEIGHT,
        "categories": "CE"
    },
    "REACTOME_IMMUNOREGULATORY_INTERACTIONS_BETWEEN_A_LYMPHOID_AND_A_NON_LYMPHOID_CELL": {
        "names": [
            "ITGAL","CD8A","CD3E","VCAM1","CD22","C3","SLAMF7","LILRB2","LAIR1"
        ],
        "weight": WEIGHT,
        "categories": "CE"
    },
    "BIOCARTA_THELPER_PATHWAY": {
        "names": [
            "THY1","ITGAL","CD2","CD3E"
        ],
        "weight": WEIGHT,
        "categories": "CE"
    },
    "REACTOME_SIGNALING_BY_INTERLEUKINS": {
        "names": [
            "MMP9","IL4R","IL2RB","CCL19","VCAM1","SDC1","IL32","TAB2","IL10RA","CEBPD","LGALS9"
        ],
        "weight": WEIGHT,
        "categories": "CE"
    },
    "PID_CD8_TCR_DOWNSTREAM_PATHWAY": {
        "names": [
            "CD8A","CD3E","PRKCB","IL2RB","GZMB"
        ],
        "weight": WEIGHT,
        "categories": "CE"
    },
    "KEGG_CYTOKINE_CYTOKINE_RECEPTOR_INTERACTION": {
        "names": [
            "IL4R","IL2RB","CCL19","IL10RA","TNFSF13B","CD27","CCL21","CXCL14"
        ],
        "weight": WEIGHT,
        "categories": "CE"
    },
    "HALLMARK_INTERFERON_GAMMA_RESPONSE": {
        "names": [
            "IL4R","IL2RB","IRF8","VCAM1","SLAMF7","IL10RA","SAMHD1"
        ],
        "weight": WEIGHT,
        "categories": "CE"
    }
}



def get_spatial_gene_set(adata: sc.AnnData, gene_set_categories: str):
    gene_set = []
    for gene_set_name in GENE_SETS:
        if GENE_SETS[gene_set_name]["categories"] == gene_set_categories:
            gene_set += GENE_SETS[gene_set_name]["names"]
    gene_set = list(set(gene_set))
    gene_set = list(set(gene_set).intersection(adata.var_names))
    return gene_set
