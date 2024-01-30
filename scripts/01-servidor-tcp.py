import socket

# Cria um objeto socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define o endereço IP e a porta que o servidor irá escutar
host = '127.0.0.1'
porta = 12345

# Vincula o socket ao endereço e à porta
servidor.bind((host, porta))

# Começa a escutar por conexões
servidor.listen()

print("Servidor escutando em {}:{}".format(host, porta))

# Aceita uma conexão
conexao, endereco = servidor.accept()
print("Conectado a {}".format(endereco))

# Recebe a mensagem do cliente
mensagem = conexao.recv(1024)
print("Mensagem recebida: " + mensagem.decode())

# Envia uma resposta para o cliente
resposta = "Mensagem recebida"
conexao.send(resposta.encode())

# Fecha a conexão
conexao.close()
