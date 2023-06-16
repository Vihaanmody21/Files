import nmap

NM = nmap.PortScanner()
NM.scan('localhost', '1-1000')

for Host in NM.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (Host, NM[Host].hostname()))
    print('State : %s' % NM[Host].state())

    for Proto in NM[Host].all_protocols():
        print('----------')
        print('Protocol : %s' % Proto)

        Ports = NM[Host][Proto].keys()
#       lport.sort()
        for Port in Ports:
            print ('Port : %s\tState : %s' % (Port, NM[Host][Proto][Port]['state']))