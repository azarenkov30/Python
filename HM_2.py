with open('salary.txt', 'w', encoding='UTF-8') as salary:

    name =['Ivanov', 'Petrov', 'Tinkoff', 'Aleksandrova', 'Kuznecova']
    cash = [500000, 35000, 60000, 500001, 200000]
    pay = dict((zip(name, cash)))
    for key, val in pay.items():
        salary.write(key+' - '+str(val)+'\n')

with open('salary.txt', 'r', encoding='UTF-8') as salary:
    for line in salary:
        name, dash, cash = line.split()
        if int(cash) <= 500000:
            cash_tax = int(cash) * 0.87
            print(name.upper(), dash, cash_tax)
