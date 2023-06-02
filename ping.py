import platform
import subprocess
import threading
import time

results = {}

def ping(ip):
    """
    This method checks if the ip is reachable or not, it sends 5 ping requests
    """
    ping_list = []
    packet_loss_string = ""
    if (platform.system() == "Windows"):
        ping_list = ["ping", ip, "-n", "5"]
        packet_loss_string = "(0% loss"
    else:
        ping_list = ["ping", ip, "-c", "5"]
        packet_loss_string = " 0% packet loss"
    resp = subprocess.Popen(ping_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = resp.stdout.read().decode("utf-8")
    # We will check if the output contains the string '0% packet loss' or not
    output_list = output.split(packet_loss_string)
    if len(output_list) > 1:
        results[ip] = "UP"
        return "UP"
    else:
        results[ip] = "DOWN"
        return "DOWN"


def ping_all(ips):
    """
    pings all ips and returns a dictionary
    """
    threads = []
    for ip in ips:
        thread = threading.Thread(target=ping, args=(ip,))
        threads.append(thread)
        thread.start()
        time.sleep(.2)
    for thread in threads:
        thread.join()
    return results
