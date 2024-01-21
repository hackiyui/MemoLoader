import subprocess
import random
import wmi

# Générer une adresse IP aléatoire
def generate_random_ip():
    ip = '.'.join(str(random.randint(0, 255)) for _ in range(4))
    return ip

# Obtenir l'interface réseau active
def get_active_interface():
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        if interface.DefaultIPGateway:
            return interface.Description
    return None

# Changer l'adresse IP
def change_ip(interface):
    new_ip = generate_random_ip()
    subprocess.call(["netsh", "interface", "ip", "set", "address", f"name='{interface}'", "static", new_ip, "255.255.255.0"])
    print("Nouvelle adresse IP :", new_ip)

# Utilisation du code
interface = get_active_interface()

if interface:
    print("Interface réseau active :", interface)
    change_ip(interface)
else:
    print("Aucune interface réseau active trouvée.")

input("[ENTREZ] pour terminer le programme")