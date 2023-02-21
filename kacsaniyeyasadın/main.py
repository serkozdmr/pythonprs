from datetime import *

birth = datetime.strptime(input("Doğum tarihiizi giriniz(gün.ay.yıl): " ), "%d.%m.%Y")
age = datetime.now() - birth
print("şu kadar {} saniye yaşadınız: ".format(age.total_seconds()))
