print('''Consider the grammar G given by S->
OSA2. S->012, 2A->A2, A->11.
Test whether (a) 00112 ∈ L(G)''')

str1 = '00112'
S1 = 'OSA2'
S2 = '012'
C = 'A2'  # take 2A=C
D = '11'  # take 1A=D

# Step 1: Replace 'S' in S1 with S2
step1 = S1.replace('S', S2)
print('String after replacing S:', step1)

if '2A' in step1 and 'A2' in step1:
    print('This is not accepting because both 2A and A2 are present in the string.')
else:
    print('This is acceptable.')

# Step 2: Replace '2A' with '1'
step2 = step1.replace('2A', '1')

if str1 == step2:
    print('Now, 00112 ∈ L(G):', step2)
