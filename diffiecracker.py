# Prompt user for values
A = int(input("Enter decimal value for A (public key of party 1): "))
B = int(input("Enter decimal value for B (public key of party 2): "))
p = int(input("Enter decimal value for p (prime modulus): "))
g = int(input("Enter decimal value for g (generator): "))

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

if a is None or b is None:
    print("Failed to compute private keys 'a' or 'b'. Ensure the inputs are correct.")
    exit()

print(f"a is {a}")
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