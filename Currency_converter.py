
print("===== CURRENCY CONVERTER =====")
print("1. INR to USD")
print("2. USD to INR")
print("3. INR to EUR")
print("4. INR to GBP")

choice = input("Choose conversion (1-4): ")
amount = float(input("Enter amount: "))

if choice == "1":
    result = amount / 83
    print("Amount in USD:", round(result, 2))

elif choice == "2":
    result = amount * 83
    print("Amount in INR:", round(result, 2))

elif choice == "3":
    result = amount / 90
    print("Amount in EUR:", round(result, 2))

elif choice == "4":
    result = amount / 105
    print("Amount in GBP:", round(result, 2))

else:
    print("Invalid choice!")
