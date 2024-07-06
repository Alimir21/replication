def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions


def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        if Pattern not in freq:
            freq[Pattern] = 0
        else:
            freq[Pattern] += 1
    return freq


def ReverseComplement(Pattern):
    def Complement(Pattern):
        comp = ""
        for char in Pattern:
            if char == 'A':
                comp += 'T'
            elif char == 'T':
                comp += 'A'
            elif char == 'C':
                comp += 'G'
            elif char == 'G':
                comp += 'C'
            else:
                comp += char  # Append non-nucleotide characters as is
        return comp

    def Reverse(Pattern):
        rev = ""
        for char in reversed(Pattern):
            rev += char
        return rev

    complemented_pattern = Complement(Pattern)
    reverse_complement = Reverse(complemented_pattern)
    return reverse_complement


def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count


def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # Compute the count of the symbol in the first half of the genome
    array[0] = PatternCount(symbol, Genome[0:n//2])

    for i in range(1, n):
        # Update the count based on the previous count and the symbols at the current position and its complement
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] += 1  # Increment the count if the symbol matches
        if ExtendedGenome[i + (n//2)] == symbol:
            array[i] -= 1  # Decrement the count if the symbol matches

    return array


def SkewArray(Genome):
    n = len(Genome)
    Skew = [0]  # Initialize Skew array with just one element

    for i in range(1, n + 1):  # Start loop from index 1
        if Genome[i - 1] == 'A' or Genome[i - 1] == 'T':
            Skew.append(Skew[i - 1])
        elif Genome[i - 1] == 'C':
            Skew.append(Skew[i - 1] - 1)
        elif Genome[i - 1] == 'G':
            Skew.append(Skew[i - 1] + 1)

    return Skew


def MinimumSkew(Genome):
    positions = []
    skewarray = SkewArray(Genome)
    min_skew = min(skewarray)  # Find the minimum value of all values in the skew array
    for i, skew in enumerate(skewarray):
        if skew == min_skew:
            positions.append(i)  # Add all positions achieving the min to positions
    return positions


def HammingDistance(p, q):
    # Initialize the Hamming distance counter
    distance = 0

    # Iterate through the characters of the strings p and q
    for i in range(len(p)):
        # If the characters at position i are not the same, increment the distance counter
        if p[i] != q[i]:
            distance += 1

    # Return the computed Hamming distance
    return distance


def ApproximatePatternMatching(Text, Pattern, d):
    positions = []
    k = len(Pattern)
    n = len(Text)

    for i in range(n - k + 1):
        substring = Text[i:i + k]
        if HammingDistance(Pattern, substring) <= d:
            positions.append(i)

    return positions


def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    # your code
    k = len(Pattern)
    n = len(Text)

    for i in range(n - k + 1):
        substring = Text[i:i + k]
        if HammingDistance(Pattern, substring) <= d:
            count += 1

    return count

