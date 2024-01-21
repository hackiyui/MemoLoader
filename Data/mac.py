import subprocess
import random
import uuid
import wmi
import re
import winreg
import string
import os
import re
import win32api
import win32file

# Générer une adresse MAC aléatoire
def generate_random_mac():
    mac = [random.choice('0123456789ABCDEF') for _ in range(12)]
    return ':'.join(mac)



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

# Changer l'adresse MAC
def change_mac(interface):
    new_mac = generate_random_mac()
    subprocess.call(["ipconfig", "/release"])
    subprocess.call(["ipconfig", "/flushdns"])
    subprocess.call(["ipconfig", "/renew"])
    subprocess.call(["reg", "add", "HKLM\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}", "/v", "NetworkAddress", "/d", new_mac, "/f"])
    subprocess.call(["wmic", "nic", "where", "NetConnectionID='{}'".format(interface), "call", "disable"])
    subprocess.call(["wmic", "nic", "where", "NetConnectionID='{}'".format(interface), "call", "enable"])
    print("Nouvelle adresse MAC :", new_mac)

# Changer l'adresse IP
def change_ip(interface):
    new_ip = generate_random_ip()
    subprocess.call(["netsh", "interface", "ip", "set", "address", "name='{}'".format(interface), "static", new_ip, "255.255.255.0"])
    print("Nouvelle adresse IP :", new_ip)

# Générer un code HWID aléatoire
def generate_hwid():
    hwid = ""
    characters = "0123456789ABCDEF"
    for i in range(16):
        hwid += random.choice(characters)
    return hwid

# Générer un UUID aléatoire
def generate_uuid():
    return str(uuid.uuid4())

# Classe de composant
class Component:
    def __init__(self, component_id, hw_id, uuid):
        self.component_id = component_id
        self.hw_id = hw_id
        self.uuid = uuid

# Mettre à jour un composant
def update_component(component):
    # Simule la mise à jour d'un composant
    print(f"Composant {component.component_id} mis à jour avec le nouveau code HWID : {component.hw_id} et UUID : {component.uuid}")

def get_mac_address():
    ipconfig_output = subprocess.check_output('ipconfig /all').decode(errors='ignore')
    mac_addresses = re.findall(r'Physical Address[\. ]+: ([\da-fA-F-]+)', ipconfig_output)
    return mac_addresses[0] if mac_addresses else None

def get_mac_address():
    getmac_output = subprocess.check_output('getmac').decode(errors='ignore')
    mac_addresses = re.findall(r'([\da-fA-F]{2}[:-]){5}[\da-fA-F]{2}', getmac_output)
    return mac_addresses[0] if mac_addresses else None

def generate_random_hwid(length):
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))

def change_hwid():
    # Generate a random HWID
    new_hwid = generate_random_hwid(16)

    try:
        base_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\VideoAdapterBusses\PCIBus", 0, winreg.KEY_ALL_ACCESS)
        num_subkeys = winreg.QueryInfoKey(base_key)[0]

        for i in range(num_subkeys):
            subkey_name = winreg.EnumKey(base_key, i)
            subkey_path = os.path.join(r"HARDWARE\DESCRIPTION\System\VideoAdapterBusses\PCIBus", subkey_name)
            gpu_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path, 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(gpu_key, "HardwareID", 0, winreg.REG_SZ, new_hwid)
            winreg.CloseKey(gpu_key)
        winreg.CloseKey(base_key)
    except Exception as e:
        print("Error modifying GPU HWID:", str(e))

    # Modify HWID values for the CPU
    try:
        cpu_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0", 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(cpu_key, "ProcessorNameString", 0, winreg.REG_SZ, new_hwid)
        winreg.CloseKey(cpu_key)
    except Exception as e:
        print("Error modifying CPU HWID:", str(e))

    # Modify HWID values for the motherboard
    try:
        motherboard_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\BIOS", 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(motherboard_key, "SystemManufacturer", 0, winreg.REG_SZ, new_hwid)
        winreg.CloseKey(motherboard_key)
    except Exception as e:
        print("Error modifying motherboard HWID:", str(e))

    # Modify HWID values for the RAM
    try:
        ram_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0", 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(ram_key, "Identifier", 0, winreg.REG_SZ, new_hwid)
        winreg.CloseKey(ram_key)
    except Exception as e:
        print("Error modifying RAM HWID:", str(e))

    print("The HWID of the GPU, CPU, motherboard, and RAM has been modified with the newly generated HWID:", new_hwid)

def generate_random_id():
    hwid = ''.join(random.choices('0123456789ABCDEF', k=16))
    return hwid

def change_hwid2():
    new_hwid = generate_random_id()
    cmd1 = f'reg add "HKLM\SYSTEM\CurrentControlSet\Control\SystemInformation" /v SystemProductName /t REG_SZ /d "New Product Name" /f'
    cmd2 = f'reg add "HKLM\SYSTEM\CurrentControlSet\Control\SystemInformation" /v SystemManufacturer /t REG_SZ /d "New Manufacturer" /f'
    cmd3 = f'reg add "HKLM\SYSTEM\CurrentControlSet\Control\SystemInformation" /v SystemFamily /t REG_SZ /d "New Family" /f'
    cmd4 = f'reg add "HKLM\SYSTEM\CurrentControlSet\Control\SystemInformation" /v SystemSKU /t REG_SZ /d "New SKU" /f'
    cmd5 = f'reg add "HKLM\SYSTEM\CurrentControlSet\Control\SystemInformation" /v SystemUUID /t REG_SZ /d {new_hwid} /f'
    subprocess.call(cmd1, shell=True)
    subprocess.call(cmd2, shell=True)
    subprocess.call(cmd3, shell=True)
    subprocess.call(cmd4, shell=True)
    subprocess.call(cmd5, shell=True)

# Utilisation du code
interface = get_active_interface()

def kill_processes():
    processes = [
        "EasyAntiCheat_Setup.exe",
        "FortniteLauncher.exe",
        "EpicWebHelper.exe",
        "FortniteClient-Win64-Shipping.exe",
        "EasyAntiCheat.exe",
        "BEService_x64.exe",
        "EpicGamesLauncher.exe",
        "FortniteClient-Win64-Shipping_BE.exe",
        "FortniteClient-Win64-Shipping_EAC.exe",
        "BEService",
        "EasyAntiCheat"
    ]
    
    # Execute the command to kill each process
    for process in processes:
        command = f"taskkill /f /im {process}"
        os.system(command)

def generate_random_hwid33(length):
    characters = string.ascii_letters + string.digits
    random_hwid = ''.join(random.choice(characters) for _ in range(length))
    return random_hwid

def change_hwid_c_drive():
    c = wmi.WMI()
    for physical_disk in c.Win32_DiskDrive():
        if "C:" in physical_disk.Name:
            new_hwid = generate_random_hwid33(16)
            physical_disk.SerialNumber = new_hwid
            physical_disk.Save()

if interface:
    print("Interface réseau active :", interface)
    change_mac(interface)
    change_hwid_c_drive() 
else:
    print("Aucune interface réseau active trouvée.")

input("[ENTREZ] pour terminer le programme")