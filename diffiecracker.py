# Add your values here
A = 3
B = 9
p = 13
g = 7

# Input ciphertext
ciphertext = input("Enter the ciphertext: ")

# Function to find the discrete logarithm
def find_exponent(base, mod, target):
    for exp in range(1, 10):
        if (base ** exp) % mod == target:
            return exp
    return None

# Find 'a' and 'b' using the function
a = find_exponent(g, p, A)
b = find_exponent(g, p, B)

if a is not None:
    print(f"a is {a}")
if b is not None:
    print(f"b is {b}")

# Calculate shared key
k0 = (B ** a) % p
k1 = (A ** b) % p

if k0 == k1:
    shared_key = k0
    print(f"Shared key is {shared_key}")
else:
    print("Keys do not match")
    shared_key = None

# Decrypt ciphertext
if shared_key is not None:
    plaintext = ""
    for c in ciphertext:
        encrypted_digit = int(c, 16)
        decrypted_digit = encrypted_digit ^ shared_key
        plaintext += format(decrypted_digit, 'X')
    print(plaintext)
else:
    print("Decryption failed due to missing shared key.")