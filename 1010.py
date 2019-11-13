codP1,numP1,valP1 = input().split(" ")
codP2,numP2,valP2 = input().split(" ")

codP1 = int(codP1)
numP1 = int(numP1)
valP1 = float(valP1) 

codP2 = int(codP2)
numP2 = int(numP2)
valP2 = float(valP2)

total = (numP1 * valP1) + (numP2 * valP2)
print("VALOR A PAGAR: R$ %.2f" % total)
