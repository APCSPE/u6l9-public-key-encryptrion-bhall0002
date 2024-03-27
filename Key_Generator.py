#THE ENCRYPTED MESSAGE I SENT TO SAMANTHA: q!0$u}y~q#0y$0{y||y~w0}u0$| (|* (ap seminar is killing me slowly) 
#THE MESSAGE I DECRYPTED, SENT TO ME BY EMMA:  lets go women in stem :D (,%43?'/?7/-%.?).?34%-?Yc)

import random

# generates a private key to go with public_key
def generate_private_key(public_key, computer):
    public_key += computer
    rand = random.randint(1, 9)
    temp = public_key
    digits = []
    while temp != 0:
        digits.insert(0, temp % 10)
        temp = temp // 10
    new_digits = []
    for digit in digits:
        if digit + rand > 9:
            num = rand - (10 - digit)
            new_digits.append(num)
        else:
            new_digits.append(digit + rand)
    new_digits.append(rand)
    num_digits = len(new_digits)
    for i in range(num_digits):
        new_digits.append(random.randint(1, 9))
    private_key = ""
    for digit in new_digits:
        private_key += str(digit)
    return private_key


# ------------ MAIN PROGRAM ---------------
computer_num = int(input("Enter your computer number (1-34): "))
my_public_key = int(input("Enter a number (e.g. 5178402) for your PUBLIC key: "))
my_private_key = generate_private_key(my_public_key, computer_num)

# COPY/PASTE THE FOLLOWING KEYS IN YOUR LAB SHEET:
print("my public key (to be shared): " + str(my_public_key))
print("my private key (kept secret): " + my_private_key)
