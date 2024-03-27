#THE PUBLIC KEY I INPUTTED: 11945029
#THE PRIVATE KEY IT RETURNED: 553894074592639696

def decrypt_message(message, private_key, computer):
  private_key = str(private_key)
  num = len(private_key) / 2
  temp = private_key[0:int(num)]
  decode = 0
  if temp[0] == "0":
    decode += 5
  digits = []
  while temp != 0:
    digits.insert(0, int(temp) % 10)
    temp = int(temp) // 10
  last = digits[len(digits) - 1]
  digits.pop(len(digits) - 1)
  new_digits = []
  for digit in digits:
    if digit - last < 0:
      num = 10 - (last - digit)
      new_digits.append(num)
    else:
      new_digits.append(digit - last)
  mult = 10 ** (len(new_digits) - 1)
  key = 0
  for digit in new_digits:
    key += (digit * mult)
    mult = mult // 10
  key -= computer
  key = str(key)
  for digit in key:
    decode += int(digit)
  decoded_text = ""
  for char in message:
    decoded_text += decrypt_character_with_offset(char, decode)
  return decoded_text


def encrypt_message(message, public_key):
  encode = 0
  temp = public_key
  digits = []
  while temp != 0:
    digits.insert(0, int(temp) % 10)
    temp = int(temp) // 10
  for digit in digits:
    encode += digit
  encoded_text = ""
  for char in message:
    encoded_text += encrypt_character_with_offset(char, encode)
  return encoded_text


def encrypt_character_with_offset(my_char, offset):
  encoded_unicode = ord(my_char)
  if encoded_unicode + offset > 126:
    new_unicode = encoded_unicode + offset - 126 + 32 - 1
    encrypted_char = chr(new_unicode)
  else:
    encrypted_char = chr(encoded_unicode + offset)
  return encrypted_char


def decrypt_character_with_offset(my_char, encryption_key):
  encoded_unicode = ord(my_char)
  if encoded_unicode - encryption_key < 32:
    new_unicode = encoded_unicode - encryption_key + 126 - 32 + 1
    encrypted_char = chr(new_unicode)
  else:
    encrypted_char = chr(encoded_unicode - encryption_key)
  return encrypted_char


# --------------- MAIN PROGRAM -----------------
computer_num = int(input("Enter your computer number (1-34): "))
print("Would you like to:\n(1) Encrypt a message to someone else\n(2) Decrypt a message sent to you")
choice = int(input("Enter option (1 or 2): "))

if choice == 1:
  message_to_send = input("Enter a message to encrypt: ")
  their_public_key = int(input("Enter recipient's PUBLIC key: "))
  encrypted_message = encrypt_message(message_to_send, their_public_key)
  print("Encrypted message: " + encrypted_message)
elif choice == 2:
  message_to_you = input("Enter a message sent to you to decrypt: ")
  your_private_key = int(input("Enter YOUR PRIVATE key: "))
  decrypted_message = decrypt_message(message_to_you, your_private_key, computer_num)
  print("The message is: " + decrypted_message)
