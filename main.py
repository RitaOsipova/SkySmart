n = int(input())

faktoren = []              
z = n                       

while z > 1:
  p = 2
  i = 1
  while p != 0:
    i += 1
    p = z % i
  faktoren.append(i)
  z = z // i

print(faktoren)