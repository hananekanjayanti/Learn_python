#aplikasi kalkulator
# (+ - * / exit)
command = ""

while command != "exit":

    command = input("perintah: ")
    
    if command == "exit":
        break

    if command != "+" and command != "-" and command != "*" and command != "/":
        print("tidak dikenali")
        continue

    a = int(input("angka pertama: "))
    b = int(input("angka kedua: "))

    if command == "+":
        result = a + b
    elif command == "-":
        result = a - b
    elif command == "*":
        result = a * b
    elif command == "/":
        result = a / b

    print(f"Hasil : {result}")

print("thx udh pake aplikasi ini")

