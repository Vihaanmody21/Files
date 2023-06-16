

#code just for backup


print("-"*10 + "Adding Car to Database" + "-"*10, end = "\n\n")

License = input("Enter Vehicle License Plate: ").upper()
Vehicle = input("Enter Full Vehicle Name: ")
Assembled = input("Enter Vehicle Assembled: ")
VIN  = input("Enter Vehicle Identification Number: ")
Manufacturer = input("Enter Vehicle Manufacturer: ")
Company = input("Enter Vehicle Company: ")
Color = input("Enter Vehicle Color: ")
State = input("Enter Vehicle State[In United States]: ")
Picture = input("Enter Vehicle Image[Link]: ")

Format = f"""
car{License.replace(" ","")} = {{
    'License Plate': '{License}',
    'Vehicle':'{Vehicle}',
    'Assembled':'{Assembled}',
    'VIN':'{VIN}',
    'Manufacturer':'{Manufacturer}',
    'Company':'{Company}',
    'Color':'{Color}',
    'State':'{State}',
    'Image(Link)':'{Picture}'
}}
\n
"""
if f"car{License.replace(' ','')}" not in open(r"C:\Users\vihaa\Desktop\Python\Python-Workspace\Car-Finder\Cars.py").read():
    with open("Cars.py", "a") as Cars:
        Cars.write(Format)
        Cars.close()
    print("Success!")
else:
    print("Vehicle License Plate already added in Database(No duplicates allowed)")

