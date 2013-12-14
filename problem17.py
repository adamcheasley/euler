units = {1: 'one',
         2: 'two',
         3: 'three',
         4: 'four',
         5: 'five',
         6: 'six',
         7: 'seven',
         8: 'eight',
         9: 'nine'}
teens = {10: 'ten',
         11: 'eleven',
         12: 'twelve',
         13: 'thirteen',
         14: 'fourteen',
         15: 'fifteen',
         16: 'sixteen',
         17: 'seventeen',
         18: 'eighteen',
         19: 'nineteen'}
tens = {2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'}
letter_count = 0

for i in range(1, 1000):  # 1 to 999
    if len(str(i)) == 1:
        letter_count += len(units[i])
    elif len(str(i)) == 2:
        if str(i)[0] == '1':
            letter_count += len(teens[i])
        else:
            num = str(i)
            letter_count += len(tens[int(num[0])])  # twenty
            if num[1] != '0':
                letter_count += len(units[int(num[1])])  # two
    else:
        num = str(i)
        letter_count += len(units[int(num[0])])  # two
        letter_count += len('hundred')
        if num[1] != '0' or num[2] != '0':
            letter_count += len('and')
        if num[1] != '0' and num[1] != '1':
            letter_count += len(tens[int(num[1])])  # twenty
        if num[1] == '1':
            letter_count += len(teens[int(num[1:])])
        elif num[2] != '0' and num[1] != '1':
            letter_count += len(units[int(num[2])])  # two

letter_count += len('onethousand')
print letter_count
