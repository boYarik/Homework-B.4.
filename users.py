import sqlite3

connect = sqlite3.connect('sochi_athletes.sqlite3')
cur = connect.cursor()

def create_table():
        cur.execute("""CREATE TABLE IF NOT EXISTS user("id" integer primary key autoincrement, "first_name" text, "last_name" text, "gender" text, "email" text, "birthdate" text, "height" float);""")


def request_data():
   print("Привет! Я запишу твои данные!")
   
   first_name = input("Введи своё имя: ")
   
   last_name = input("А теперь фамилию: ")
   
   gender = input('Ваш пол (Female/Male): ')
   while True:
      if gender.lower() == 'female':
         gender = gender.title()
         break
      elif gender.lower() == 'male':
         gender = gender.title()
         break
      else:
         gender = input('Повторите ввод пола (Female/Male): ')
         
   email = input("Мне еще понадобится адрес твоей электронной почты: ")
   while valid_email(email) == False:
        email = input("Некорректный адрес. Повторите ввод: ")
   
   birthdate = input("Ваша дата рождения в гггг-мм-чч: ")
   while valid_birthdate(birthdate) == False:
        birthdate = input("Повторите ввод в формате гггг-мм-чч: ")


   height = input('Ваш рост в см: ')
   while height.isdigit() == False:
         height = input('Повторите ввод роста в см (только цифры): ')
   height = int(height)

   
   cur.execute("""INSERT INTO user("first_name", "last_name", "gender", "email", "birthdate", "height") 
      VALUES(?, ?, ?, ?, ?, ?)""", ( first_name, last_name, gender, email, birthdate, height)
   )


def valid_email(email):
   if email.count('@') == 1:
      [name, domen] = email.split('@')
      if domen.count('.') >= 1:
         return True
      else:
         return False
   else:
      return False

def valid_birthdate(birthdate):
        if len(birthdate) == 10 or birthdate.count('-') == 2:
                [y, m, n] = birthdate.split('-')
                if len(y) == 4 and len(m) == 2 and len(n) == 2:
                        return True
                else:
                        return False
        else:
                return False


def main():
   create_table()
   request_data()
   connect.commit()
   print("Спасибо, данные сохранены!")

def ocenka_func():
   if  int(ocenka) > 10 and int(ocenka) <= 0:
      return False
   

if __name__ == "__main__":
	main()

def ocenka_func():
   if  int(ocenka) > 10 or int(ocenka) <= 0:
      return True
   else:
      return False

ocenka = input('оцените сервис от 0 до 10:')
while ocenka.isdigit() == False or ocenka_func():
   ocenka = input('повторите ввод от 0 до 10:')

if int(ocenka) < 5:
   print('Ой, попробуй найти лучше')
else:
   print('Спасибо за использование нашего сервиса!)')
