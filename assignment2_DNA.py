def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 > dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return str.count(dna, nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    a = str.count(dna1, dna2)
    return a > 0


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (that is, it contains
    no characters other than 'A', 'T', 'C' and 'G'). 

    >>> is_valid_sequence('ATCGT')
    True
    >>> is_valid_sequence('ATCGTK')
    False

    """
    a = str.count(dna, 'A')
    g = str.count(dna, 'G')
    c = str.count(dna, 'C')
    t = str.count(dna, 'T')
    return len(dna) == (a+g+c+t)


def insert_sequence(dna1,dna2,j):
    """(str,str,int) ->str

    Return the DNA sequence obtained by inserting the second DNA sequence into
    the first DNA sequence at the given index.

    >>>insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>>insert_sequence('ACGT','T',3)
    'ACGTT'

    """

    dna1 = dna1[:j] + dna2 + dna1[j:]
    return dna1


def get_complement(n):
    """(str) ->str

    Return the nucleotide's complement.

    >>>get_complement('A')
    T
    >>>get_complement('G')
    C

    """

    if n == 'A':
        return 'T'
    if n == 'T':
        return 'A'
    if n == 'G':
        return 'C'
    if n == 'C':
        return 'G'


def get_complementary_sequence(dna):
    """(str) ->str

    Return the DNA sequence that is complementary to the given DNA sequence.

    >>>get_complementary_sequence('ATCGA')
    'TAGCT'
    >>>get_complementary_sequence('TGGGCCA')
    'ACCCGGT'

    """

    a = ""
    for i in dna:
        a = a + get_complement(i)
    return a
