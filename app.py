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

    a = intinput('"angka pertama: "))


print("thx udh pake aplikasi ini")

