'''
Atenção, os códigos foram criados para fins educacionais e não devem ser utilizados para outros fins.
Esses código não são otimizados e portanto não devem ser utilizados em produção.
'''

from scapy.all import ARP, Ether, srp
import ipaddress

def scan_network(network):
    # Converter a rede em uma lista de endereços IP
    ip_list = [str(ip) for ip in ipaddress.IPv4Network(network, strict=False)]

    # Preparar o pedido ARP
    arp_request = ARP(pdst=ip_list)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    # Enviar pacotes ARP e receber respostas
    answered, _ = srp(arp_request_broadcast, timeout=2, verbose=False)

    # Processar os resultados
    active_hosts = []
    for sent, received in answered:
        active_hosts.append({'ip': received.psrc, 'mac': received.hwsrc})

    return active_hosts

# Substitua '192.168.1.0/24' pelo range de IPs da sua rede
network_range = "192.168.15.0/24"
active_hosts = scan_network(network_range)

for host in active_hosts:
    print(f"IP: {host['ip']}, MAC: {host['mac']}")
