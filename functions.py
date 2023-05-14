def get_summ(one, two, delimiter='&'):
    return (str(one) + delimiter + str(two)).upper()

summ = get_summ('Learn', 'python')
print(summ)
