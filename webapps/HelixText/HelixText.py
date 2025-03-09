import argparse
import random

# Reverse translation table with multiple codons for each amino acid
reverse_translation_table = {
    'A': ['GCT', 'GCC', 'GCA', 'GCG'],    # Alanine
    'C': ['TGT', 'TGC'],    # Cysteine
    'D': ['GAT', 'GAC'],    # Aspartic acid
    'E': ['GAA', 'GAG'],    # Glutamic acid
    'F': ['TTT', 'TTC'],    # Phenylalanine
    'G': ['GGT', 'GGC', 'GGA', 'GGG'],    # Glycine
    'H': ['CAT', 'CAC'],    # Histidine
    'I': ['ATT', 'ATC', 'ATA'],    # Isoleucine
    'K': ['AAA', 'AAG'],    # Lysine
    'L': ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'],    # Leucine
    'M': ['ATG'],    # Methionine (start codon)
    'N': ['AAT', 'AAC'],    # Asparagine
    'P': ['CCT', 'CCC', 'CCA', 'CCG'],    # Proline
    'Q': ['CAA', 'CAG'],    # Glutamine
    'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],    # Arginine
    'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],    # Serine
    'T': ['ACT', 'ACC', 'ACA', 'ACG'],    # Threonine
    'V': ['GTT', 'GTC', 'GTA', 'GTG'],    # Valine
    'W': ['TGG'],    # Tryptophan
    'Y': ['TAT', 'TAC'],    # Tyrosine
    # Ambiguous amino acids
    'B': ['RAT', 'RAC'],    # B = Aspartic acid (GAT) or Asparagine (AAT) -> RAY
    'J': ['MTA', 'MTC', 'MTT'],    # J = Leucine (CTT) or Isoleucine (ATT) -> MTH
    'O': ['TAA'],    # O (Pyrrolysine) not standard, using stop codon
    'U': ['TGA'],    # U (Selenocysteine) uses stop codon TGA
    'X': ['NNN'],    # X = Any amino acid -> NNN
    'Z': ['SAA', 'SAG'],    # Z = Glutamic acid (GAA) or Glutamine (CAA) -> SAR
}

# Inverse translation table for reverse translation (DNA -> text)
inverse_translation_table = {
    codon: amino_acid for amino_acid, codons in reverse_translation_table.items() for codon in codons
}

def text_to_dna(text):
    # Convert text to uppercase to match dictionary keys
    text = text.upper()
    dna_sequence = []

    for char in text:
        if char in reverse_translation_table:
            # Randomly select a codon from available codons
            dna_sequence.append(random.choice(reverse_translation_table[char]))
        else:
            raise ValueError(f"Unsupported character '{char}' in input text")

    return ''.join(dna_sequence)

def dna_to_text(dna_sequence):
    text = []
    # Split DNA sequence into codons (groups of 3 nucleotides)
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3].upper()
        if codon in inverse_translation_table:
            text.append(inverse_translation_table[codon])
        else:
            raise ValueError(f"Unsupported codon '{codon}' in input DNA sequence")

    return ''.join(text)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert text to DNA or DNA to text using reverse translation.")
    parser.add_argument('sequence', type=str, help="The text or DNA sequence to convert")
    parser.add_argument('--reverse', action='store_true', help="Flag for reverse translation (DNA to text)")
    
    # Parse arguments
    args = parser.parse_args()

    if args.reverse:
        # Convert DNA to text
        try:
            text = dna_to_text(args.sequence)
            print(f"Amino Acid: {text}")
        except ValueError as e:
            print(e)
    else:
        # Convert text to DNA
        try:
            dna_sequence = text_to_dna(args.sequence)
            print(f"DNA Sequence: {dna_sequence}")
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()

