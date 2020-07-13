#contoh 1

kuadrat = lambda x: x * x

print(kuadrat(3))

#contoh 2

kali = lambda x, y: x * y

print(kali(3,4))

#penerapan lambda dalam filter

my_list = [1,2,3,4,5,6,7,8,9]
#memfilter bilangan ganjil
list_ganjil = list(filter(lambda x: x % 2 != 0, my_list))
print(list_ganjil)

#penerapan lambda dalam fungsi map
kuadrat = list(map(lambda x: x ** 2, my_list))
print(kuadrat)



