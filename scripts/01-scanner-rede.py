from scapy.all import ARP, Ether, srp

def scan(ip):
    # Endereço de IP do destino
    # Exemplo: "192.168.1.1/24"
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients.append(client_dict)
    return clients

# Função para escanear a rede
network_clients = scan("192.168.15.0/24")
for client in network_clients:
    print(client)
