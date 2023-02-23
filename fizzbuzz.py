print("""programdan çıkmak için "q" devam etmek için "c" tuşlayınız """)
program = str(input("devam etmek istiyor musunuz? "))
if program == "c":

    def fizzbuzz(n):
        if n % 3 == 0 :
            print("fizz")
        if n % 5 == 0 :
            print("buzz")
        if n % 15 == 0:
            print("fizzbuzz")
        else:
            return(str(n))
else :
    exit()

uzunluk = int(input("bir sayı giriniz : "))

for i in range (1 , uzunluk+1):
    print(fizzbuzz(i))
