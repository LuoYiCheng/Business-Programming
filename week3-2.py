a = int(input())
cash = 1000 - a

five_hundred = cash // 500
one_hundred = (cash % 500) // 100
fifty = (cash%100) // 50
ten = (cash%50) // 10
five = (cash%10) // 5
one = cash % 5

str_500 = ''
str_100 = ''
str_50 = ''
str_10 = ''
str_5 = ''
str_1 = ''

seperation = bool(five_hundred) + bool(one_hundred) + bool(fifty) + bool(ten) + bool(five) + bool(one) - 1

if five_hundred >= 1:
    str_500 += '500, ' + str(five_hundred)
    if seperation >= 1:
        str_500 += "; "
        seperation -= 1
        
if one_hundred >= 1:
    str_100 += '100, ' + str(one_hundred)
    if seperation >= 1:
        str_100 += '; '
        seperation -= 1
    
if fifty >= 1:
    str_50 += '50, ' + str(fifty)
    if seperation >= 1:
        str_50 += '; '
        seperation -= 1
    
if ten >= 1:
    str_10 += '10, ' + str(ten)
    if seperation >= 1:
        str_10 += '; '
        seperation -= 1
    
if five >= 1:
    str_5 += '5, ' + str(five)
    if seperation >= 1:
        str_5 += '; '
        seperation -= 1
    
if one >= 1:
    str_1 += '1, ' + str(one)
    if seperation >= 1:
        str_1 += '; '
        seperation -= 1
    

print(str_500, str_100, str_50, str_10, str_5, str_1, sep='')

