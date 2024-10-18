from cryptography.fernet import Fernet
 
# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)
 
# Data to be encrypted
data = b"Confidential information"
 
# Encryption
cipher_text = cipher_suite.encrypt(data)
print("Encrypted:", cipher_text)
 
# Decryption
plain_text = cipher_suite.decrypt(cipher_text)
print("Decrypted:", plain_text.decode('utf-8'))
