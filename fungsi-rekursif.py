def faktorial(x):
    """ fungsi untuk menentukan faktorial dari bilangan """

    if x == 1:
        return 1
    else:
        return (x * faktorial(x-1))


bil = 4
print(f'faktorial dari {bil} adalah {faktorial(bil)}')