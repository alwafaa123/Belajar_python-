import nmap

nm = nmap.PortScanner()
nm.scan('127.0.0.1', '22-443')

for host in nm.all_hosts():
    print(f'Host : {host} ({nm[host].hostname()})')
    print(f'State : {nm[host].state()}')
    for proto in nm[host].all_protocols():
        print(f'----------')
        print(f'Protocol : {proto}')
        lport = nm[host][proto].keys()
        # lport.sort() # Sorting is not necessary and might cause issues in newer Python versions
        for port in lport:
            print(f'port : {port}\tstate : {nm[host][proto][port]["state"]}')