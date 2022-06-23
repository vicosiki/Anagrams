# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    # the sorted strings are checked
    if(sorted(word)== sorted(anagram)):
        return True
    else:
        return False

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

print(find_anagram(string1, string2))

