def romanToInt(romanValue):

    # Roman references
    roman = {'I':1, 'IV':4, 'IX':9, 'V':5, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'D':500, 'M':1000, 'CD':400, 'CM':900}
    i = 0
    num = 0

    # Iterate over the romanValue and create the Integer representation
    while i < len(romanValue):
        if i+1<len(romanValue) and romanValue[i:i+2] in roman:
            num+=roman[romanValue[i:i+2]]
            i+=2
        else:
            num+=roman[romanValue[i]]
            i+=1
    return num

#Tests
print("Output:", romanToInt("III"))
print("Output:", romanToInt("XV"))