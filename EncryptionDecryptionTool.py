print("For Encrypt enter 1 , For Decrypt enter 0")
inp = int(input())
print("Enter the message please")
message = input()

print("Enter the index of shift please")
x = int(input())
message2 = ""

if inp == 1:  # Encrypt
    for char in message:
        shifted_char = chr((ord(char) + x) )
        message2 += shifted_char

    print("encrypt message:", message2)

elif inp ==0:
    for char in message:
        shifted_char = chr((ord(char) - x) )
        message2 += shifted_char

    print("decrypt message:", message2)

