import ipinfo

IP = input("Enter IP: ")
Token = 'dabc988d1ff453'
Handler = ipinfo.getHandler(Token)
Details = Handler.getDetails(IP)
for key, value in Details.all.items():
    print(f"{key}: {value}")