from scapy.all import sr1, IP, ICMP
import ipaddress

# Definindo o intervalo de IPs para a varredura
network = "192.168.1.0/24"
ip_range = ipaddress.ip_network(network)

# Lista para armazenar os hosts ativos
active_hosts = []

for ip in ip_range:
    # Enviando um pacote ICMP Echo Request para cada IP
    packet = IP(dst=str(ip))/ICMP()
    response = sr1(packet, timeout=1, verbose=0)

    # Verifica se houve resposta
    if response:
        active_hosts.append(str(ip))

# Imprime os hosts ativos
print("Hosts ativos na rede:")
for host in active_hosts:
    print(host)
