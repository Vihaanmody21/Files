from Cars import *
import Cars
import sys

def Add_Car():
    print("-"*10 + "Adding Car to Database" + "-"*10, end = "\n\n")
    try:
        License = input("Enter Vehicle License Plate: ").upper()
        Vehicle = input("Enter Full Vehicle Name: ")
        Assembled = input("Enter Vehicle Assembled: ")
        VIN  = input("Enter Vehicle Identification Number: ")
        Manufacturer = input("Enter Vehicle Manufacturer: ")
        Company = input("Enter Vehicle Company: ")
        Color = input("Enter Vehicle Color: ")
        State = input("Enter Vehicle State[In United States]: ")
        Picture = input("Enter Vehicle Image[Link]: ")
    except KeyboardInterrupt:
        return

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


def Find_Car():
    print("-"*10 + "Finding Car" + "-"*10, end = "\n\n")
    try:
        Find = input("Vehicle License Plate: ").upper().replace(" ","")
    except KeyboardInterrupt:
        return

    Car = f"car{Find}"

    #All cars in database are in USA
    Country = "United States"
    if Car in open(r"C:\Users\vihaa\Desktop\Python\Python-Workspace\Car-Finder\Cars.py").read():
        try:
            print(f'License Plate: {globals()[Car]["License Plate"]}')
            print(f'Vehicle: {globals()[Car]["Vehicle"]}')
            print(f'Assembled: {globals()[Car]["Assembled"]}')
            print(f'Vehicle Identification Number(VIN): {globals()[Car]["VIN"]}')
            print(f'Manufacturer: {globals()[Car]["Manufacturer"]}')
            print(f'Company: {globals()[Car]["Company"]}')
            print(f'Color: {globals()[Car]["Color"]}')
            print(f"Country: {Country}")
            print(f'State: {globals()[Car]["State"]}')
            print(f'Image Link: {globals()[Car]["Image(Link)"]}')
        except KeyError:
            print("Car added recently. Exit and run program again to obtain results.")
    else:
        print("Vehicle Not in Database or Invalid License Plate")

while True:
    try:
        Option = input("""
1) Add Vehicle Registration in Database
2) Find a Vehicle using its License Plate
3) Exit
""")
    except KeyboardInterrupt:
        break
    if "1" in Option:
        Add_Car()
    elif "2" in Option:
        Find_Car()
    else:
        sys.exit(0)