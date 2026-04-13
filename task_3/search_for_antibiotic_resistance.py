import csv
import sys
from collections import defaultdict

def parse_ResFinder(input_file, output_tsv):

    gene_to_ab = defaultdict(set)
    
    with open(input_file, 'r') as f:
        f.seek(0)
        reader = csv.DictReader(f, delimiter='\t')
        
        for row in reader:
            gene = row.get('Resistance gene', '').strip()
            phenotype = row.get('Phenotype', '').strip()
            if not gene or not phenotype:
                continue
            antibiotics = [ab.strip() for ab in phenotype.split(',') if ab.strip()]
            gene_to_ab[gene].update(antibiotics)
    
    with open(output_tsv, 'w') as out:
        writer = csv.writer(out, delimiter='\t')
        writer.writerow(['Gene', 'Antibiotics'])
        for gene in sorted(gene_to_ab.keys()):
            writer.writerow([gene, ", ".join(sorted(gene_to_ab[gene]))])


if __name__ == '__main__':
    input = sys.argv[1]
    output = sys.argv[2]
    parse_ResFinder(input, output)