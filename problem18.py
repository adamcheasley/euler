['', '', '', '70', '', '11', '', '33', '', '28', '', '77', '', '73', '', '17', '', '78', '', '39', '', '68', '', '17', '', '57', '', '', '']
['', '', '91', '', '71', '', '52', '', '38', '', '17', '', '14', '', '91', '', '43', '', '58', '', '50', '', '27', '', '29', '', '48', '', '']
['', '63', '', '66', '', '04', '', '68', '', '89', '', '53', '', '67', '', '30', '', '73', '', '16', '', '69', '', '87', '', '40', '', '31', '']
['04', '', '62', '', '98', '', '27', '', '23', '', '09', '', '70', '', '98', '', '73', '', '93', '', '38', '', '53', '', '60', '', '04', '', '23']


a = 82
b = 23
c = 75
d = 77
e = 73
f = 7

route = 'abd'
out = a + b + d
if (a + b + e) > out:
    route = 'abe'
    out = a + b + e
if (a + c + e) > out:
    route = 'ace'
    out = a + c + e
if (a + c + f) > out:
    route = 'acf'
    out = a + c + f

print len(x)
print len(y)
print len(z)



# New solution:
# produce all possible sets of 4 level arrays
# only sum if next array index is equal or +1 of current array index
[(0, b, c, d) for b in range(3) for c in range(4) for d in range(5)]
