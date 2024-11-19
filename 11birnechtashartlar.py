'''a = int(input("Juft son kiriting: >>> "))
if a%2 == 0 : print("Rahmat!")
else: print("Bu son juft emas.")'''

'''yosh = int(input("Yoshingiz nechida? >>> "))
if yosh<4 or yosh>60 : narh = 0
elif yosh<18 : narh = 10000
elif yosh>18 : narh = 20000
print(f"Kirish {narh} so`m")'''

'''a = float(input("Birinchi sonni kiriting: >>> "))
b = float(input("Ikkinchi sonni kiriting: >>> "))
if a<b: print(f"{a} < {b}")
else: print(f"{a} > {b}")'''

'''mahsulotlar = ['olma', 'anor','uzum','nok','shaftoli']
savat = []
for n in range(3):
	savat.append(input(f"Savatga {n+1}-mahsulotni qo`shing:  "))
for meva in savat:
    if meva in mahsulotlar:
        print(f"Do`konimizda {meva} bor ")
    else:
        print(f"Do`konimizda {meva} yo`q ")'''

'''mahsulotlar = ['olma', 'anor','uzum','nok','shaftoli']
royhat = []
bor_mahsulotlar = []
mavjud_emas=[]

for n in range(3):
    royhat.append(input(f"Savatga {n+1} - mahsulotni qo`shing: "))

for meva in royhat :
	if meva.lower() in mahsulotlar :  bor_mahsulotlar.append(meva)
	elif meva.lower() not in mahsulotlar :   mavjud_emas.append(meva)

if mavjud_emas:
    print(f"Do`konimizda quyidagi mahsulotlar yo`q")
    for k in mavjud_emas:
	    print(f" {k}")
else:
	print("Siz so`ragan barcha mahsulotlar bor")'''

'''foydalanuvchilar = ['rushana', 'fotima', 'nargiza', 'soliha']
login = input("Loginingizni kiriting : >>> ")
if login.lower() in foydalanuvchilar :
    print("Login band, yangi login tanlang!")
else :
    foydalanuvchilar.append(login)
    print("Xush kelibsiz foydalanuvchi!")
print(foydalanuvchilar)'''

'''a = int(input("Son kiriting >>> "))
for n in range(2,11):
    if a % n == 0 :
        print(f"{a} soni {n} ga qoldiqsiz bo`linadi")'''


# xatolar bilan ishlash
'''son = float(input("Juft son kiriting: "))
if son % 2 != 0:
    print("Bu son juft emas.")
else:
    print("Rahmat!")'''

'''yosh = int(input("Yoshingiz nechida? >>> "))
if yosh <= 4 or yosh >= 60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")'''

'''x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f'{x}<{y}')
else:
    print(f"{x}>{y}")'''

'''mahsulotlar = ['un', "yog", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else:
    print("Savatingiz bo'sh")'''

'''mahsulotlar = ['un', "yog", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat = []
bor_mahsulotlar = []
mavjud_emas = []

for n in range(5):
    savat.append(input(f"Savatga {n + 1}-mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")'''

users = ['alisher1983','aziza','yasina', 'umar']

login = input("Yangi login tanlang: >>>" )

if login in users:
    print('Login band, yangi login tanlang!')
else:
    print("Xush kelibsiz!")
