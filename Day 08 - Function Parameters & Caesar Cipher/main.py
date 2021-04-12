alphabet =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"]

alphabet_len = len(alphabet)-1

def encode(text,shift):
    encoded_text = ""
    shift = shift % 26
    for i in text:
        value = alphabet.index(i)
        shifted_value = value + shift
        if shifted_value > alphabet_len:
            shifted_value = shifted_value - alphabet_len - 1
        encoded_text += alphabet[shifted_value]
    print(encoded_text)

def decode(text,shift):
    decoded_text = ""
    shift = shift % 26
    for i in text:
        value = alphabet.index(i)
        shifted_value = value - shift
        decoded_text += alphabet[shifted_value]
    print(decoded_text)

running = True

while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        encode(text,shift)
        running = False
    elif direction == "decode":
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        decode(text,shift)
        running = False
    else:
        print("Incorrect input detected")
