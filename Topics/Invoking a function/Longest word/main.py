word1 = input()
word2 = input()

# How many letters does the longest word contain?
letters_count_1 = len(word1)
letters_count_2 = len(word2)

if letters_count_1 >= letters_count_2:
    print(letters_count_1)
    
if letters_count_2 > letters_count_1:
    print(letters_count_2)
