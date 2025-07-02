import time 

def ism_raqam(func):
    def wrapper (*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        for arg in args:
            print(f"Funksiya bajarilish vaqti: {end - start:.5f} soniya\n")
        return result
    return wrapper


class ContactManager:
    def __init__(self):
        self.kontakt = {}

    @ism_raqam
    def qoshish(self, ism, raqam):
        if len(raqam) != 13 or raqam[0] != '+' or not raqam[1:].isdigit():
            print("❌ Telefon raqam noto'g'ri! Formati: +998901234567\n")
            return

        self.kontakt[ism] = raqam
        print(f"{ism} kontakt qoshildi.") 

    def korish(self):
        if not self.kontakt:
            print("Konatkt topilmadi.\n")
        else:
            print("\n Kontaktlar ro'yxati:")
            for ism, raqam in self.kontakt.items():
                print(f"{ism} : {raqam}") 
            print()

    def ochirish(self, ism):
        if ism in self.kontakt:
            del self.kontakt[ism]
            print(f"{ism} ochirildi.\n")
        else:
            print(f"{ism} bunday kontakt mavjud emas.\n") 

    def get_raqam(self, ism):
        return self.kontakt.get(ism)          


def kontakt_menyu(kontakt_manager):
    while True:
        print("-------------Contact Manager------------------")
        print("1.Kontact qo'shish")
        print("2.Kontaktni ko'rish")
        print("3.O'chirish")
        print("0.Chiqish")
        kod = input("Tanlovni kiriting: ")

        if kod == "1":
            ism = input("Ism kiriting: ")
            raqam = input("raqamefon raqam kiriting: ")
            kontakt_manager.qoshish(ism, raqam)

        elif kod == "2":
            kontakt_manager.korish()

        elif kod == "3":
            ism = input("Ochirmoqchi bo'lgan ismni kiriting:")
            kontakt_manager.ochirish(ism)

        elif kod == "0":
            print("Dasturdan chiqilmoqda...")
            break

        else:
            print("Noto'g'ri tanlov!\n")



    
class SMSManager:
    def __init__(self):
        self.sms = []


    def sms_yuborish(self, ism, raqam, soz):
        if len(raqam) != 13 or raqam[0] != '+' or not raqam[1:].isdigit():
            print("Telefon raqam noto'g'ri!\n")
            return
        sms = {
            "ism": ism,
            "raqam": raqam,
            "matn": soz,
            "vaqt": time.strftime("%Y-%m-%d %H:%M:%S")
        }    
        self.sms.append(sms)
        print(" SMS yuborildi!")

    def korish(self):
        if not self.sms:
            print("SMSlar mavjud emas.\n")
            return
        print("\n Yuborilgan SMSlar:")
        for i, sms in enumerate(self.sms, 1):
            print(f"{i}. {sms['ism']} ({sms['raqam']}) | {sms['vaqt']}")
            print(f"     {sms['matn']}\n")


    def ochirish(self, index):
        if 0<= index < len(self.sms):
            sms = self.sms.pop(index)
            print(f"SMS o'chirildi: {sms['ism']} - {sms['matn']}\n")
        else:
            print("Noto'g'ri index!\n")

def sms_menyu(sms_manager, kontakt_manager):
     
    while True:
        print("-----------------SMS Manager------------------")
        print("1.SMS Yuborish")
        print("2.SMS Ko'rish")
        print("3.SMS ni o'chirish")
        print("0.Chiqish")
        kod = input("Tanlovni kiriting: ")

        if kod == "1":
            kontakt_manager.korish()
            ism = input("SMS yuboriladigan ismni kiriting: ")
            raqam = kontakt_manager.get_raqam(ism)
            if not raqam:
                print("Bunday ism kontaktda yo'q!\n")
                continue
            soz = input("SMS matni: ")
            sms_manager.sms_yuborish(ism, raqam, soz)

        elif kod == "2":
            sms_manager.korish()

        elif kod == "3":
            sms_manager.korish()
            try:
                index = int(input("Qaysi SMSni o'chirmoqchisiz? Index: ")) - 1
                sms_manager.ochirish(index)
            except ValueError:
                print(" Raqam kiriting!\n")

        elif kod == "0":
            break
        else:
            print(" Noto'g'ri tanlov!\n")    

def asosiy_menyu():
    kontakt_manager = ContactManager()
    sms_manager = SMSManager()

    while True:
        print("\n Asosiy menyu")
        print("1.Kontakt Manager")
        print("2. SMS Manager")
        print("0. Chiqish")
        kod = input("Tanlang: ")

        if kod == "1":
            kontakt_menyu(kontakt_manager)

        elif kod == "2":
            sms_menyu(sms_manager, kontakt_manager)

        elif kod == "0":
            print("Dasturdan chiqilmoqda...")
            break

        else:
            print("Noto'g'ri tanlov!\n")

asosiy_menyu()                