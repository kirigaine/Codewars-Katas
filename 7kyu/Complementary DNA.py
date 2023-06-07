# ***DESCRIPTION***
#Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
#
#If you want to know more: http://en.wikipedia.org/wiki/DNA
#
#In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
#
#More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)
#
#Example: (input --> output)
#"ATTGC" --> "TAACG"
#"GTAT" --> "CATA"

# ***BASE CODE***
#def DNA_strand(dna):
    # code here
    
# ***CODE***
def DNA_strand(dna):
    
    # Create a new string to construct
    
    new_strand = ""
    
    # Iterate and match, append to new string
    
    for nucleotide in dna:
        match nucleotide:
            case 'A':
                new_strand += ("T")
            case 'T':
                new_strand += ("A")
            case 'G':
                new_strand += ("C")
            case 'C':
                new_strand += ("G")
    return new_strand