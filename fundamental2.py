# Data struktur : scalar

anak1 = 'Adi'
anak2 = 'ida'
anak3 = 'udi'
anak4 = 'joko'

print(anak1)
print(anak2)
print('-' * 20)
#List
anak_list = ['Adi', 'ida', 'Kusuma', 'mawar']

print(f'anak pertama {anak_list[0]}')

print('-' * 20)

for a in anak_list:
    print('Hai {}'.format(a))

print('-' * 20)

for sons in range(0, len(anak_list)):
    print(f'{sons+1}. Hai {anak_list[sons]}')

print('#Tamnah data ke list')
print('-' * 20)

buah = ['jeruk', 'mangga', 'apel', 'kiwi', 'semangka']
print(buah)

print(buah.sort(reverse=False))

print(buah)