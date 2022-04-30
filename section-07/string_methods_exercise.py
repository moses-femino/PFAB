mixed_case = "A Song of Ice and Fire"
title_case = mixed_case.title()
words = mixed_case.split()

print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())
print(title_case)
print(mixed_case.startswith("A"))
print(mixed_case.endswith("e"))
print(words)
print("".join(words).isalpha())