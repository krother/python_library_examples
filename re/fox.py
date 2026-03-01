
import re

text = "the quick brown fox jumps over the lazy dog"

# Search for `o` and show adjacent characters:
print(re.findall(r".o.", text))

# Search for three-letter words enclosed by whitespace:
print(re.findall(r"\s(\wo\w)\s*", text))

# Substitute any of `dflj` by a `w`:
print(re.sub(r"[dflj]", "w", text))

# Check if `jumps` or `swims` occurs and return details:
print(re.search(r'jumps|swims', text))
