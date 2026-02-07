logs = [
    ("192.168.1.1", "/home", "Chrome"),
    ("192.168.1.2", "/login", "Firefox"),
    ("192.168.1.1", "/dashboard", "Chrome"),
    ("192.168.1.3", "/home", "Edge"),
    ("192.168.1.2", "/home", "Firefox")
]
urls_por_ip = {}
visitas_url = {}
uso_nave = {}
ips_unicas = set()

for ip, url, navegador in logs:
    if ip not in urls_por_ip:
        urls_por_ip[ip] = set()
    urls_por_ip[ip].add(url)
    if url in visitas_url:
        visitas_url[url] += 1
    else:
        visitas_url[url] = 1
    if navegador in uso_nave:
        uso_nave[navegador] += 1
    else:
        uso_nave[navegador] = 1
    ips_unicas.add(ip)
navegador_top = ""
max_votos = 0
for nav, cuenta in uso_nave.items():
    if cuenta > max_votos:
        max_votos = cuenta
        navegador_top = nav
lista_ips_orden = sorted(list(ips_unicas))

print(f"URLs por IP: {urls_por_ip}\n")
print(f"Visitas por URL: {visitas_url}\n")
print(f"Navegador más utilizado: {navegador_top}\n")
print(f"Lista de IPs ordenadas: {lista_ips_orden}")