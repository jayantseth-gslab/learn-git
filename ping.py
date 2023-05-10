import subprocess

def ping(ip):
    """
    This method checks if the ip is reachable or not, it sends 5 ping requests
    """
    resp = subprocess.Popen(["ping", ip, "-c", "5"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = resp.stdout.read().decode("utf-8")
    # We will check if the output contains the string '0% packet loss' or not
    output_list = output.split("0%\ packet\ loss")
    if len(output_list) > 1:
        return "UP"
    else:
        return "DOWN"