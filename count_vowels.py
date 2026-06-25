def count_vowels(string):
    count=0
    vowels="aeiouAEIOU"
    for char in string:
        if char in vowels:
            count += 1
    return count


string = input("Enter a string :")
print("Vowels count: ",count_vowels(string))