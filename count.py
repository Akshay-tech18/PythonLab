def count_char(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count
str1 = input("Enter the string : ")
str2 = count_char(str1)
for key,values in sorted(str2.items()):
    print(f" {key} : {values}")