import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="autosalon",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )

class AutoSalon:
    def __init__ (self, name, phone):
        self.name = name
        self.phone = phone

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO autosalons (name, phone) VALUES (%s, %s)", (self.name, self.phone))
        conn.commit()
        cur.close()
        conn.close()

    def salonlar():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, phone FROM autosalons")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    
    def ochirish(salon_id):
        conn = get_connection()    
        cur = conn.cursor()
        cur.execute("DELETE FROM autosalons WHERE id = %s", (salon_id,))
        conn.commit()
        cur.close()
        conn.close()

class Car:
    def __init__(self, salon_id, model, color, year, price):
        self.salon_id = salon_id
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
                    INSERT INTO cars (salon_id, model, color, year, price) 
                    VALUES (%s, %s, %s, %s, %s)
                    """, (self.salon_id, self.model, self.color, self.year, self.price))
        conn.commit()
        cur.close()
        conn.close()

    def salon(salon_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, model, color, year, price FROM cars WHERE salon_id = %s", (salon_id,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows    

    def ochirish(car_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM cars WHERE id = %s", (car_id,))
        conn.commit()
        cur.close()
        conn.close()

    def tahrirlash(car_id, model, color, year, price):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            UPDATE cars SET model=%s, color=%s, year=%s, price=%s WHERE id=%s
        """, (model, color, year, price, car_id))
        conn.commit()
        cur.close()
        conn.close()

def salon_menyu():
    while True:
        print("\n1. Mashinalar ro'yxati")
        print("2. Mashina qo'shish")
        print("3. Mashina o'chirish")
        print("4. Mashina tahrilash")
        print("0. Orqaga")

        tanlash = input("Tanlovingiz: ")
        if tanlash == "1":
            salon_id = int(input("Salon ID kiriting: "))
            for car in Car.salon(salon_id):
                print(car)

        elif tanlash == "2":
            salon_id = input("Salon ID: ")
            model = input("Model: ")
            color = input("Rangi: ")
            year = input("Yili: ")
            price = input("Narxi: ")
            car = Car(salon_id, model, color, year, price)
            car.save()

        elif tanlash == "3":
            car_id = int(input("Mashina o'chirish ID: "))
            Car.ochirish(car_id)

        elif tanlash == "4":
            car_id = int(input("Mashina ID: "))
            model = input("Model: ")
            color = input("Rangi: ")
            year = input("Yili: ")
            price = input("Narxi: $")
            Car.tahrirlash(car_id, model, color, year, price)

        elif tanlash == "0":
            break
        
        else:
            print("Tanlov noto'g'ri!\n")

def asosiy_menyu():
    while True:
        print("\n1. Autosalon yaratish")
        print("2. Autosalon tanlash(mashina menyusi)")
        print("3. Autosalonlar")
        print("4. Autosalonni o'chirish")            
        print("0. Chiqish")

        tanlash = input("Tanlang:")
        if tanlash == "1":
            name = input("Nomi: ")
            phone = input("Telefon: ")
            salon = AutoSalon(name, phone)
            salon.save()

        elif tanlash == "2":
            salon_menyu()
        elif tanlash == "3":
            for salon in AutoSalon.salonlar():
                print(salon)

        elif tanlash == "4":
            salon_id = int(input("AUtosalon Ochirish ID: "))
            AutoSalon.ochirish(salon_id)
        elif tanlash == "0":
            break

        else:
            print("Tanlov noto'g'ri!\n")

if __name__ == "__main__":
    asosiy_menyu()                  