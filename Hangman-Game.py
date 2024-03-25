word = "dog"
tries = 0
flag = 0
count=0
str_word = word
while True:
    # Make a copy of the word to work with


    if tries == 5:
        print("You used all tries")
        flag = 1
        break

    print("Enter a character please:")
    input_char = input()

    if input_char in str_word:
        print("Yes!! Right character")
        str_word = str_word.replace(input_char, "0")  # Replace the character in the copy
        print(str_word)
        print("num of remaining chars is:"+str(len(word)-1-count))
        count+=1
    else:
        print("Not the right character")
        tries += 1

    if all(char == '0' for char in str_word):
        print("Yes, Got it!!!")
        break

if flag == 1:
    print("The right word is: " + word)
else:print("The word is "+word)
