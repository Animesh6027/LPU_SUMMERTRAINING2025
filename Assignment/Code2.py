'''Count Vowels and Consonants:
Write a program that takes a string as input. Use a for loop to iterate through the string,
and use an if-else condition inside the loop to count the number of vowels and consonants.
Print the counts at the end.'''

str=input("Enter the word:")
vowels=0
consonants=0
vowels_set="aeiouAEIOU"
for char in str:
    if char.isalpha():
        if char in vowels_set:
            vowels+=1
        else:
            consonants+=1

print("Your vowel count is:",vowels)
print("Your consonant count is:",consonants)