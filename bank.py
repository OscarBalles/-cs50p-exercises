rta = input("Hello, Frank ")
rta = rta.lower().strip()
if rta.startswith("hello"):
    print("$0")
elif rta.startswith("h"):
    print("$20")
else:
    print("$100")
