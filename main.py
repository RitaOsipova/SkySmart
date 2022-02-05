######################################################################
# 31.01.2022 nr.1
# num = int(input())

# des = num // 10
# one = num % 10

# print(f'des = {des}')
# print(f'one = {one}')

######################################################################
#31.01.2022 nr.2a)

num = int(input())

hun = num // 100
mau = num % 100
des = mau // 10
one = mau % 10

print(f'hun = {hun}')
print(f'des = {des}')
print(f'one = {one}')

mal = hun * des * one
print(f' mal = {mal}')

plus = hun + des + one
print(f'plus = {plus}')

minhun = (one * 100) + (des * 10) + hun
print(minhun)
