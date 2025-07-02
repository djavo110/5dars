import time 

def ism_tel(func):
    def wrapper (*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        for arg in args:
            print(f"Funksiya bajarilish vaqti: {end - start:.5f} soniyna\n)")
        return result
    return wrapper

class ContactManager:
    def __init__(self):
        self.kontakt = {}

    @ism_tel
    def qoshish(self, ism, tel):
        self.kontakt[ism] = tel
        print(f"{ism} kontakt qoshildi.")

    def korish(self):
        if not self.kontakt:
            print("Kontakt topilmadi.\n")
        else:
            print("\n Kontakt ro'yxati.")
            for ism, tel in self.kontakt.items():
                print(f"{ism} : {tel}")
            print()    

    def ochirish(self, ism):
        if ism in self.kontakt:
            print(f"{ism} o'chirildi.")
        else:
            print(f"{ism} bunday kontakt mavjud emas.\n")                            

def menyu():
    manager = ContactManager()

    while True:
        print("-------------Contact Manager---------------")
        print("1.Kontakt qo'shish")
        print("2.Kontakt ko'rish")
        print("3.O'chirish")
        print("0.Chiqish")
        kod = input("Tanlov kiriting: ")

        if kod == "1":
            ism = input("Ism kiritng: ")
            tel = input("telefon raqam kiriting: ")
            manager.qoshish(ism, tel)

        elif kod == "2":
            manager.korish()

        elif kod == "3":
            ism = input("Ochirmoqchi bo'lgan ismni kiriting: ")        
            manager.ochirish(ism)

        elif kod == "0":
            print("Dasturdan chiqilmoqda...")
            break

        else:
            print("noto'g'ri tanlov!\n")

menyu()            
        