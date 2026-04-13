import csv

def parse_gff(gff_file, output_tsv):
    with open(gff_file, 'r') as infile, open(output_tsv, 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter='\t')
        writer.writerow(['Locus_tag', 'Product', 'Start', 'End', 'Length'])
        
        for line in infile:
            if line.startswith('#'):
                continue
                
            parts = line.strip().split('\t')
            if len(parts) < 9:
                continue
                
            feature_type = parts[2]
            if feature_type != 'CDS':
                continue
            
            attrs = {}
            for attr in parts[8].split(';'):
                if '=' in attr:
                    key, value = attr.split('=', 1)
                    attrs[key] = value
            
            locus = attrs.get('locus_tag', '')
            product = attrs.get('product', '')
            
            writer.writerow([
                locus,
                product,
                parts[3],  
                parts[4],
                int(parts[4])-int(parts[3])
            ])

parse_gff('bakta_output/scaffolds.gff3', 'gene_table.tsv')