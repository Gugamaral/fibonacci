sequence =  [1]
f = 1

for i in range(11):
    sequence.append(f)
    f += sequence[i]
print(sequence)