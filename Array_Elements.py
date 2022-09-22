import array as my
fir = my.array('b', [11, 6, 22])
fir.pop(2)
print(fir)

#finding index
fir = my.array('b', [2, 3, 3, 3, 4, 5, 6])
print(fir.index(2))

#finding reverse
fir = my.array('b', [2, 3, 3, 3, 4, 5, 6])
fir.reverse()
print(fir)

#for counting
fir = my.array('b', [2, 3, 3, 3, 4, 5, 6])
print(fir.count(5))