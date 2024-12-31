def create_dict(words):
    dict = {}
    for word in words:
        if word:
            first_char=word[0].upper()
        if first_char in dict:
            dict[first_char].append(word)
        else:
            dict[first_char]=[word]
    return dict
string1 = input("Enter the string with proper spaces = ")
words = string1.split()
result = create_dict(words)
for key,values in sorted(result.items()):
    print(f"{key} : {values}")