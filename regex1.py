# Program that looks for a postal code in an address
import re
address = "Atlixcáyotl 5718, Reserva Territorial Atlixcáyotl, 72453 Puebla, Pue."
postalCodeRegex = re.compile(r'(\d{5})')
mo = postalCodeRegex.search(address)
print("The postal code is: " + mo.group())


