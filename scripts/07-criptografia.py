from cryptography.fernet import Fernet

def gerar_chave():
    """Gera uma chave secreta."""
    return Fernet.generate_key()

def criptografar_mensagem(mensagem, chave):
    """Criptografa a mensagem usando a chave fornecida."""
    f = Fernet(chave)
    mensagem_criptografada = f.encrypt(mensagem.encode())
    return mensagem_criptografada

def descriptografar_mensagem(mensagem_criptografada, chave):
    """Descriptografa a mensagem usando a chave fornecida."""
    f = Fernet(chave)
    mensagem_descriptografada = f.decrypt(mensagem_criptografada).decode()
    return mensagem_descriptografada

# Gerar chave secreta
chave_secreta = gerar_chave()

# Mensagem a ser criptografada
mensagem_original = "Esta é uma mensagem secreta."

# Criptografar a mensagem
mensagem_criptografada = criptografar_mensagem(mensagem_original, chave_secreta)
print("Mensagem Criptografada:", mensagem_criptografada)

# Descriptografar a mensagem
mensagem_descriptografada = descriptografar_mensagem(mensagem_criptografada, chave_secreta)
print("Mensagem Descriptografada:", mensagem_descriptografada)
