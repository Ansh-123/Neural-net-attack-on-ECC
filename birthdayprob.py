bits = 64

baseprob = 1

for i in range(10000000):
    baseprob = baseprob * ((pow(2, bits))-1-i)/(pow(2, bits))

print(baseprob)