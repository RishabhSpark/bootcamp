import itertools

pairs = itertools.combinations([1, 2, 3], 2)
triples = itertools.permutations([1, 2, 3], 3)

# Print pairs
print("Pairs:")
for pair in pairs:
    print(pair)

# Print triples
print("\nTriples:")
for triple in triples:
    print(triple)
