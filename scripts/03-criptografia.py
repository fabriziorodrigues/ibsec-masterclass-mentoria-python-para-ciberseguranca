from cryptography.fernet import Fernet

# Geração da chave
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Criptografar uma mensagem
text = b"Ola, IBSEC!"
cipher_text = cipher_suite.encrypt(text)
print("Texto criptografado:", cipher_text)

# Descriptografar a mensagem
decipher_text = cipher_suite.decrypt(cipher_text)
print("Texto decifrado:", decipher_text)