from datetime import datetime

Users = []
products = []

class User:

    def __init__(self,login,password):
        self.login = login
        self.password = password
        self.role = 0

    def set_role(self,role):
        with open("Admin.txt") as file:
            for i in passes.readlines():
                key, val = i.strip().split(':')
                putUsersData[key] = val
        self.role = role


class Monitor:

    def __init__(self,name,price,resolution,hertz,model):
        self.name = name
        self.price = price
        self.resolution = resolution
        self.hertz = hertz
        self.model = model

    def addData(self):
        self.name = input("Введите производителя: ")
        self.price = input("Введите цену: ")
        self.resolution = input("Введите разрешение: ")
        self.hertz = input("Введите герцовку: ")
        self.model = input("Введите модель: ")
        with open("products.txt", "a") as file:
            file.write(f"\n{self.name},{self.price},{self.resolution},"
                       f"{self.hertz},{self.model}")

    def editData(self):
        openFile()
        print("Выебрите элемент для редактирования")
        for elem in products:
            temp = elem
            num = products.index(temp) + 1
            elem = Monitor(temp[0], temp[1], temp[2], temp[3], temp[4])
            print(f"{num} - ", end="")
            Monitor.prints(elem)

        select = int(input(""))
        select -= 1
        if select in range(0,len(products)+1):
            select2 = int(input("Что хотите отредактировать? 1 - Бренд, 2 - "
                                "Цену, 3 - Разрешение, 4 - Герцовку, "
                                "5  - Модель, 6 - Выйти"))
            if select2 == 6:
                print("Изменения сохранены")
            elif select in range (1, 6):
                products[select][select2-1] = input()
                print(products[select])
            else:
                print("Введите от 1 до 6")
        else:
            print("Введите корректный элемент")

        saveFile()

    def deleteData(self):
        openFile()
        print("Выберите элемент для удаления")
        for elem in products:
            temp = elem
            num = products.index(temp) + 1
            elem = Monitor(temp[0], temp[1], temp[2], temp[3], temp[4])
            print(f"{num} - ", end="")
            Monitor.prints(elem)

        select = int(input())
        select -= 1
        if select in range(0, len(products) + 1):
            products.pop(select)
            select += 1
            print(f"Элемент {select} удален")
        else:
            print("Выберите корректный элемент")
        saveFile()

    def prints(self):
        print(f"Бренд {self.name}, цена {self.price}, разрешение экрана "
              f"{self.resolution}, {self.hertz} герц, "
              f"{self.model} модель")

    def changeData(self):
        products.clear()
        while True:
            print("1 - Добавить элемент, 2 - Редактировать элемент, 3 - "
                  "Удалить элемент, 4 - Выйти")
            select = int(input())
            if select == 1:
                Monitor.addData(self)
            elif select == 2:
                Monitor.editData(self)
            elif select == 3:
                Monitor.deleteData(self)
            elif select == 4:
                print("Данные обновлены")
                break

    def sortData(self):
        products.clear()
        openFile()
        select = int(input("Выберите параметр сортировки: 1 - Бренд, 2 - Цена,"
                           " 3 - Разрешение, 4 - "
                           "Герцовка "))
        if select in range(1,5):
            if select == 1 or select == 3:
                select -= 1
                temp = sorted(products, key = lambda elem: elem[select])
                dataViewT(temp)
            elif select == 2 or select == 4:
                select -= 1
                Swapped = True
                while Swapped:
                    Swapped = False
                    for elem in range(0,len(products)-1):
                        if int(products[elem][select]) > int(products[elem+1]
                                                             [select]):
                            products[elem][select], products[elem+1][select] =\
                                products[elem+1][select], \
                                products[elem][select]
                            Swapped = True
                dataViewT(products)

        else:
            print("Введите корректное значение для сортировки")
        change = int(input("Желаете что-либо купить? 1 - Да, 2 - Нет"))
        if change == 1:
            Monitor.paymentReceiptT(self, products)
        else:
            print()

    def filterInRange(self):
        products.clear()
        openFile()
        templist = []
        select = int(input("Выеберите объект для указания диапазона: 1 - Цена,"
                           " 3 - Герцовка"))
        min = int(input("Выеберите минимальное значение: "))
        max = int(input("Выеберите максимальное значение: "))
        for elem in range(0,len(products)):
            n = int(products[elem][select])
            if n > max or n < min:
                templist.append(elem)
        templist.sort(reverse = True)
        for elem in templist:
            temp = int(elem)
            products.pop(elem)
        dataViewT(products)
        change = int(input("Желаете что-либо купить? 1 - Да, 2 - Нет"))
        if change == 1:
            Monitor.paymentReceiptT(self, products)
        else:
            print()

    def searchByValue(self):
        products.clear()
        openFile()
        temp = []
        select = input("Введите нужную модель:")
        for elem in range(0,len(products)):
            for item in range(0,5):
                if select == products[elem][item]:
                    temp.append((products[elem]))
        if len(temp) == 1:
            dataViewT(temp)
        else:
            print("Введенная модель отсутствует в магазине")
        change = int(input("Желаете что-либо купить? 1 - Да, 2 - Нет"))
        if change == 1:
            Monitor.paymentReceiptT(self, products)
        else:
            print()
        # dataViewT(products)

    def paymentReceiptT(self,products):
        print("Выебрите элементы для покупки через запятую")
        for elem in products:
            temp = elem
            num = products.index(temp) + 1
            elem = Monitor(temp[0], temp[1], temp[2], temp[3], temp[4])
            print(f"{num} - ", end="")
            Monitor.prints(elem)

        select = input("")
        listOfShopping = select.split(",")
        for elem in range(0, len(listOfShopping)):
            temp1 = int(listOfShopping[elem])
            temp1 -= 1
            listOfShopping[elem] = str(temp1)

        sum = 0
        for elem in listOfShopping:
            sum += int(products[int(elem)][1])

        now = datetime.now()
        print(now.strftime("%d/%m/%y %I:%M"))
        print()

        for elem in listOfShopping:
            elem = int(elem)
            print(products[elem][0], products[elem][4], products[elem][1])
        print()

        print(f"Итого к оплате: {sum}")

    def paymentReceipt(self):
        products.clear()
        openFile()
        Monitor.paymentReceiptT(self,products)

def openFile():
    with open("products.txt", "r") as file:
        for line in file:
            a = line.strip("'\n")
            b = a.split(",")
            products.append(b)

def saveFile():
    with open("products.txt", "w") as file:
        for elem in products:
            temp = str(elem)
            temp = temp.strip("]")
            temp = temp.strip("[")
            temp = temp.replace("'", "")
            temp = temp.replace(" ", "")
            file.write(temp)
            file.write("\n")

def dataView ():
    products.clear()
    openFile()

    for elem in products:
        temp = elem
        elem = Monitor(temp[0],temp[1],temp[2],temp[3],temp[4])
        Monitor.prints(elem)

def dataViewT (list):
    for elem in list:
        temp = elem
        elem = Monitor(temp[0], temp[1], temp[2], temp[3], temp[4])
        Monitor.prints(elem)

def admin (user):
    if user in adminUsers:
        return True
    
def main ():
    Admins = {}
    putUsersData = {}
    with open("Admin.txt") as passes:
        for i in passes.readlines():
            key, val = i.strip().split(':')
            Admins[key] = val
    putUsersData.update(Admins)
    with open("d:/test/users.txt") as passes:
        for i in passes.readlines():
            key,val = i.strip().split(':')
            putUsersData[key] = val
    person = User(input("Введите логин: "),input("Введите пароль: "))

    for key, value in putUsersData.items():
        if person.login == key and person.password == value:
            if key in Admins.keys():

                print(f"Вы вошли как администратор {key}")
                while True:
                    select = int(input("Нажимите 1 чтобы выйти, 2 - Посмотреть"
                                       " продукцию, 3 - Редактировать "
                                       "продукцию, 4 - "
                                        "Найти продукцию, 5 - Отсортировать "
                                       "продукцию, 6 - Отфильтровать по "
                                       "диапазаону, 7 - "
                                   "Купить что-либо"))
                    if select == 1:
                        print("Вы вышли из магазина")
                        break
                    elif select == 2:
                        dataView()
                    elif select == 3:
                        Monitor.changeData(self = Monitor)
                    elif select == 4:
                        Monitor.searchByValue(self = Monitor)
                    elif select == 5:
                        Monitor.sortData(self = Monitor)
                    elif select == 6:
                        Monitor.filterInRange(self = Monitor)
                    elif select == 7:
                        Monitor.paymentReceipt(self = Monitor)
            else:
                print(f"Вы вошли как пользователь {key}")
                while True:
                    select = int(input("Нажимите 1 чтобы выйти, 2 - Посмотреть "
                                       "продукцию, 3 - Найти продукцию, "
                              "4 - Отсортировать продукцию, 5 - Отфильтровать"
                                       " по диапазаону, 6 - "
                              "Купить что-либо"))
                    if select == 1:
                        print("Вы вышли из магазина")
                        break
                    elif select == 2:
                        dataView()
                    elif select == 3:
                        Monitor.searchByValue(self=Monitor)
                    elif select == 4:
                        Monitor.sortData(self=Monitor)
                    elif select == 5:
                        Monitor.filterInRange(self=Monitor)
                    elif select == 6:
                        Monitor.paymentReceipt(self=Monitor)
    if person.login != key or person.password != value:
        print("Введен неправильный логин или пароль")
main()





