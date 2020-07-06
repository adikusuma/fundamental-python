"""
Struuktur data dictionary

"""

kamus = {'anak': 'son', 'ibu': 'mother', 'ayah': 'father', 'nenek': 'grandma', 'kakek': 'grandfa'}

print(kamus['ibu'])

print('#' * 20)
print('Data driver sekitar pengguana aplikasi')
data_dari_server_gogojek = {'tanggal': '2020-07-6',
                          'driver_ist': [
                              {'nama': 'Eko', 'jarak':10},
                              {'nama': 'adi', 'jarak':30},
                              {'nama': 'budi', 'jarak':40},
                              {'nama': 'udin', 'jarak': 50}
                          ]
                            }

print(f"tanggal : {data_dari_server_gogojek['tanggal']}")
print(f"data driver : {data_dari_server_gogojek['driver_ist'][0]}")




