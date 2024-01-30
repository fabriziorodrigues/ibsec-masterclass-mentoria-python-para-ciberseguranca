import socket

# Cria um objeto socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Endereço e porta do servidor
host = '127.0.0.1'
porta = 12345

# Conecta-se ao servidor
cliente.connect((host, porta))

# Envia uma mensagem para o servidor
mensagem = "Olá, servidor!"
cliente.send(mensagem.encode())

# Recebe a resposta do servidor
resposta = cliente.recv(1024)
print("Resposta do servidor: " + resposta.decode())

# Fecha a conexão
cliente.close()
