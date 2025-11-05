
import random

# random set with repeats
ALPHABET = list('AGCT')
dna = [random.choice(ALPHABET) for i in range(50)]
print(''.join(dna))


# random set without repeats
NUMBERS = range(1, 101)
print(random.sample(NUMBERS, 10))
