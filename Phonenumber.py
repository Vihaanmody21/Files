import phonenumbers.timezone
import phonenumbers.geocoder
import phonenumbers.carrier
import phonenumbers

Number = input("Enter Phone Number with Country Code: ")
Phone = phonenumbers.parse(Number)

Time = phonenumbers.timezone.time_zones_for_number(Phone)
Carrier = phonenumbers.carrier.name_for_number(Phone, "en")
Region = phonenumbers.geocoder.description_for_number(Phone, "en")

print(f"[+] Na{str(Phone).split(' Na')[1]}")
print(f"[+] {str(Phone).split(' Na')[0]}")
print(f"[+] Valid Number: {phonenumbers.is_valid_number(Phone)}")
print(f"[+] Timezone: {Time[0]}")
print(f"[+] Carrier: {Carrier}")
print(f"[+] Region: {Region}")
print(f"[+] Vanity Number: {phonenumbers.is_alpha_number(Number)}")
print(f"[+] Internationally Dialled: {phonenumbers.can_be_internationally_dialled(Phone)}")
print(f"[+] Possible Number: {phonenumbers.is_possible_number(Phone)}")
