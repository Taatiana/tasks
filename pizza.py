pizza={'ГАВАЙСКАЯ': {'consist': ['курица',
                           'ветчина',
                           'ананас',
                           'моцарелла',
                           'томатный соус'],
               'size_price': {'M': 595, 'S': 415}},
 'МАРГАРИТА': {'consist': ['томаты', 'моцарелла', 'томатный соус'],
               'size_price': {'M': 545, 'S': 395}},
 'ПЕППЕРОНИ': {'consist': ['пепперони', 'моцарелла', 'томатный соус'],
               'size_price': {'M': 545, 'S': 395}}}

pizza_order =[]
zakaz=[]
d=dict()
import tkinter
import tkinter.ttk

window = tkinter.Tk()
# Размер окна
window.geometry("700x450")
# Название окна
window.title("Заказ пиццы")


label1=tkinter.Label(window, text="Выберете пиццы:", fg='black')
label1.grid(row=0,column=0)

label2=tkinter.Label(window, text="Выберете размер:", fg='black')
label2.grid(row=0,column=1)

label3=tkinter.Label(window, text="Укажите количество:", fg='black')
label3.grid(row=0,column=2)

label4=tkinter.Label(window, text="ПЕППЕРОНИ", fg='black')
label4.grid(row=1,column=0)

label5=tkinter.Label(window, text="МАРГАРИТА", fg='black')
label5.grid(row=2,column=0)

label6=tkinter.Label(window, text="ГАВАЙСКАЯ", fg='black')
label6.grid(row=3,column=0)

label7=tkinter.Label(window, text="Введите время заказа", fg='black')
label7.grid(row=4,column=0)

label8=tkinter.Label(window, text="Введите адрес заказа", fg='black')
label8.grid(row=4,column=1)

label9=tkinter.Label(window, text="Введите ваш номер телефона", fg='black')
label9.grid(row=4,column=2)

label10=tkinter.Label(window, text="Сумма заказа с учетом скидки:", fg='black')
label10.grid(row=8,column=1)

label11=tkinter.Label(window, text="Выберете дату заказа:", fg='black')
label11.grid(row=6,column=1)


combobox1 = tkinter.ttk.Combobox(window,values = ["-","S", "M"])
combobox1.grid(row=1,column=1)

spinbox2 = tkinter.Spinbox(window, from_=0, to=15)
spinbox2.grid(row=1,column=2)

combobox3 = tkinter.ttk.Combobox(window,values = ["-","S", "M"] )
combobox3.grid(row=2,column=1)

spinbox4 = tkinter.Spinbox(window, from_=0, to=15)
spinbox4.grid(row=2,column=2)

spinbox5 = tkinter.Spinbox(window, from_=0, to=15)
spinbox5.grid(row=3,column=2)

combobox6 = tkinter.ttk.Combobox(window,values = ["-","S", "M"] )
combobox6.grid(row=3,column=1)

combobox10 = tkinter.ttk.Combobox(window,values = ["Сегодня", "Завтра"] )
combobox10.grid(row=7,column=1)

entry7 = tkinter.Entry(window)
entry7.grid(row=5,column=1)

entry8 = tkinter.Entry(window)  
entry8.grid(row=5,column=0)

entry9 = tkinter.Entry(window)
entry9.grid(row=5,column=2)

# Команда формирования заказа
def dictionary():
      
    if (combobox10.get() == '') or (entry7 == '') or (entry8 == '') or (entry9 == ''):
        label7.config(text="Введите время заказа", fg='red')
        label8.config(text="Введите адрес заказа", fg='red')
        label9.config(text="Введите ваш номер телефона", fg='red')
        label11.config(text="Выберете дату заказа:", fg='red')
        
    else:
        global d
        print(combobox10.get())
        d['address']=entry7.get()
        d['time']=entry8.get()
        d['contact'] = entry9.get()
        print(d)


# Функция подсчета стоимости
def price():
    

    def mul(x, y):
        return x * y

    def add(x, y, z):
        return x + y + z

    MARGARITA_size = combobox3.get()
    MARGARITA_num = int(spinbox4.get())
    

    if MARGARITA_size == "-":
        MARGARITA_price = 0
        pizza_2 = 0
    else:
        if MARGARITA_num == 0:
            MARGARITA_price = 0
            pizza_2 = 0
        else:
            MARGARITA_price = int(pizza['МАРГАРИТА']['size_price'][MARGARITA_size])
            pizza_2 = mul(MARGARITA_price, MARGARITA_num)
        

    PEPPERONI_size = combobox1.get()
    PEPPERONI_num = int(spinbox2.get())
    

    if PEPPERONI_size == "-":
        PEPPERONI_price = 0
        pizza_1 = 0 
    else:
        if PEPPERONI_num == 0:
            PEPPERONI_price = 0
            pizza_1 = 0
        else:
            PEPPERONI_price = int(pizza['ПЕППЕРОНИ']['size_price'][PEPPERONI_size])
            pizza_1 = mul(PEPPERONI_price, PEPPERONI_num)
        

    GAVAISKAYA_size = combobox6.get()
    GAVAISKAYA_num = int(spinbox5.get())
    

    if GAVAISKAYA_size == "-":
        GAVAISKAYA_price = 0
        pizza_3 = 0
    else:
        if GAVAISKAYA_num == 0:
            GAVAISKAYA_price = 0
            pizza_3 = 0
        else:
            GAVAISKAYA_price = int(pizza['ГАВАЙСКАЯ']['size_price'][GAVAISKAYA_size])
            pizza_3 = mul(GAVAISKAYA_price, GAVAISKAYA_num)
 
           

# Расчет минимального значения    

    if pizza_1 == 0:
        minimum = int(min(MARGARITA_price, GAVAISKAYA_price))
    elif pizza_2 == 0:
        minimum = int(min(PEPPERONI_price, GAVAISKAYA_price))
    elif pizza_3 == 0:
        minimum = int(min(PEPPERONI_price, MARGARITA_price))
    elif (pizza_1 == 0) and (pizza_2 == 0):
        minimum = GAVAISKAYA_price
    elif (pizza_1 == 0) and (pizza_3 == 0):
        minimum = MARGARITA_price
    elif (pizza_2 == 0) and (pizza_3 == 0):
        minimum = PEPPERONI_price
    elif (pizza_1 == 0) and (pizza_2 == 0) and (pizza_3 == 0):
        minimum = 0
    else:
        minimum = int(min(PEPPERONI_price, MARGARITA_price, GAVAISKAYA_price))






    total = int(add(pizza_1, pizza_2, pizza_3))

# Расчет стоимости с учетом скидки
    if combobox10.get() =="Завтра":
        summ = float(mul((total - minimum), 0.95))
    else:
        summ = total - minimum

    label12 = tkinter.Label(window, text=summ, fg='black')
    label12.grid(row=9,column=1)

    return label12

# Определение кнопок и их функций
button1 = tkinter.Button(window, text='Заказать',command=dictionary)
button1.config(width=20, height=1, fg='black')
button1.grid(row=11,column=1)

button2 = tkinter.Button(window, text='Выход', command=window.destroy)
button2.config(width=20, height=1, fg='black')
button2.grid(row=12,column=1)


button3 = tkinter.Button(window, text='Рассчитать стоимость', command=price)
button3.config(width=20, height=1, fg='black')
button3.grid(row=10,column=1)

window.mainloop()                   

