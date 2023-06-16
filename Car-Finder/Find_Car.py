

#code just for backup


from Cars import *
import Cars

print("-"*10 + "Finding Car" + "-"*10, end = "\n\n")

Find = input("Vehicle License Plate: ").upper().replace(" ","")
Car = f"car{Find}"

#All cars in database are in USA
Country = "United States"

if Car in open(r"C:\Users\vihaa\Desktop\Python\Python-Workspace\Car-Finder\Cars.py").read():
    print(f'License Plate: {globals()[Car]["License Plate"]}')
    print(f'Vehicle: {globals()[Car]["Vehicle"]}')
    print(f'Assembled: {globals()[Car]["Assembled"]}')
    print(f'Vehicle Identification Number(VIN): {globals()[Car]["VIN"]}')
    print(f'Manufacturer: {globals()[Car]["Manufacturer"]}')
    print(f'Company: {globals()[Car]["Company"]}')
    print(f'Color: {globals()[Car]["Color"]}')
    print(f"Country: {Country}")
    print(f'State: {globals()[Car]["State"]}')
    print(f'Image Link: {globals()[Car]["Picture(Link)"]}')
else:
    print("Vehicle Not in Database or Invalid License Plate")

