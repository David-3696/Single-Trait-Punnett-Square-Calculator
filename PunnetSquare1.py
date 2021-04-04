print("_______________________________________________________________________")


print("                      Punnet Square Calculator")


print("_______________________________________________________________________\n")


print("Please enter the Genotypes of each parent, use (A) for dominant alleles and (a) for recessives alleles.")


print("_______________________________________________________________________\n")


choice1 = input("First Allele of PARENT 1 (A/a)")


A = "A"
a = "a"


if choice1 == 'A':
    X = A


elif choice1 == 'a':
    X = a

choice2 = input("Second Allele of PARENT 1 (A/a)")


if choice2 == 'A':
    Y = A


elif choice2 == 'a':
    Y = a


choice3 = input("First Allele of PARENT 2 (A/a)")

if choice3 == 'A':
    Z = A


elif choice3 == 'a':
    Z = a

choice4 = input("Second Allele of PARENT 2 (A/a)")

if choice4 == 'A':
    Q = A


elif choice4 == 'a':
    Q = a


print("_______________________________________________________________________\n")


print("PUNNET SQUARE FOR PARENT 1 =", (X, Y), "PARENT 2 =", (Z, Q))


print("_______________________________________________________________________\n")


Delta1 = ([X, Z], [Y, Z])

print(*Delta1)

Delta2 = ([X, Q], [Y, Q])

print(*Delta2, "\n")


print("_______________________________________________________________________")


D = (['A', 'A'])
E = (['A', 'a'])
F = (['a', 'A'])
G = (['a', 'a'])


print("GENOTYPE COUNT / FREQUENCY")


print("_______________________________________________________________________")


listDELTA = ([X, Z], ([Y, Z]), ([X, Q]), ([Y, Q]))


elm_count1 = listDELTA.count(D)
print(elm_count1, "AA")


elm_count2 = listDELTA.count(E)
elm_count3 = listDELTA.count(F)
print(elm_count2 + elm_count3, "Aa / aA")


elm_count4 = listDELTA.count(G)
print(elm_count4, "aa")


# calculates frequency

H = elm_count1
J = elm_count2
K = elm_count3
L = elm_count4

T = (H+J+K+L)


print("_______________________________________________________________________")


FHomD = (H/T)
print("AA", FHomD*100, "%")

FHet = ((J+K)/T)
print("Aa", FHet*100, "%")

FHomR = (L/T)
print("aa", FHomR*100, "%")

print("_______________________________________________________________________")
print("PHENOTYPE FREQUENCY")
print("_______________________________________________________________________")


OMEGA = (elm_count1 + elm_count2 + elm_count3)
GAMMA = elm_count4


print(OMEGA, "DOMINANT")
print((OMEGA/4)*100, "%")


elm_count4 = listDELTA.count(G)


print(GAMMA, "RECESSIVE")
print((GAMMA/4)*100, "%")
