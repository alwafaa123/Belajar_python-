import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+62895320256446")
phone_number2 = phonenumbers.parse("+6281231471553")
phone_number3 = phonenumbers.parse("+6289508748651")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1, "en"));
print(geocoder.description_for_number(phone_number2, "en"));
print(geocoder.description_for_number(phone_number3, "en"));

#LETS TRACK PHONE NUMBERS