from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    key = Fernet.generate_key()
    with open('encryption_key.key', 'wb') as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    with open('encryption_key.key', 'rb') as key_file:
        key = key_file.read()
    return key

# Encrypt the data
def encrypt_data(data, key):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data.encode())
    return encrypted_data

# Decrypt the data
def decrypt_data(encrypted_data, key):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data.decode()

# Ask for user input
data_to_encrypt = input("Enter the data to encrypt: ")

# Generate and save the encryption key
generate_key()

# Load the encryption key
key = load_key()

# Encrypt the data
encrypted_data = encrypt_data(data_to_encrypt, key)

# Decrypt the data (just for demonstration)
decrypted_data = decrypt_data(encrypted_data, key)

print("Encrypted data:", encrypted_data)
print("Decrypted data:", decrypted_data)