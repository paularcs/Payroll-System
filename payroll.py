
def payroll():
    print('')
    print("=======================WELCOME TO=======================")
    print('')
    print("====================EPAYROLL TROLLEY====================")
    print('')
    print("========================================================")
    print('')
    # Yes
    yeslist = ['Y', 'y', 'YES', 'yes', 'Yes']
    nolist = ['N', 'n', 'NO', 'No', 'no']

    # employee
    namelist = ["Bernadette", "bernadette", "", "Joan", "joan",
                "Roel", "roel", "'Janeth", "janeth", "Melinda", "melinda", "John", "john", "Robert", "robert"]
    print("------------------EMPLOYEE------------------")
    employee = "Bernadette", "Joan", "Roel", "Janeth", "Melinda", "John", "Robert"
    month1 = ['february']  # 28days
    month2 = ['april', 'june', 'september', 'november']  # 30days
    month3 = ['january', 'march', 'may', 'july', 'august', 'october', 'december']  # 31 days
    month123 = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'ocotober', 'november', 'december']
    holiday1 = ['march']  # 1
    holiday2 = ['january', 'june', 'august', 'october']  # 2
    holiday3 = ['february', 'july', 'september', 'november']  # 3
    holiday4 = ['may']  # 4
    holiday5 = ['april']  # 5
    holiday6 = ['december']  # 6
    print('')
    for x in reversed(range(5)):
        print(employee)
        print('')
        print('Please enter employee name')
        print('')
        fname = input("→ ")
        print('')
        if fname in namelist:
            print('')
            print('-----------------------------------Please select a Month-----------------------------------')
            print('january,', 'february,', 'march,', 'april,', 'may,', 'june,', 'july,', 'august,',
                  'september,', 'october,', 'november,', 'december')
            while True:
                print('')
                month = input("→ ")
                print("")
                if month in month123:
                    print('')
                    print("----Type 0 if none----")
                    while True:
                        try:
                            print('')
                            print('Please enter the Number of hours worked in a day')
                            print('')
                            num_hrs = int(input("→ "))
                            print('')
                        except ValueError:
                            print('')
                            print('***Input Invalid***')
                        else:
                            while True:
                                try:
                                    print('')
                                    print('Rate per hour')
                                    print('')
                                    rate = float(input("→ "))
                                    print('')
                                except ValueError:
                                    print('')
                                    print('***Input Invalid***')
                                else:
                                    while True:
                                        try:
                                            print('')
                                            print("Please Enter how many times you worked on a holiday of", month)
                                            print('')
                                            holiday = int(input("→ "))
                                            holiday = (num_hrs * rate) * holiday * 2
                                            print('')
                                        except ValueError:
                                            print('')
                                            print('***Input Invalid***')
                                        else:
                                            while True:
                                                try:
                                                    print('')
                                                    print("Please Enter how many times you worked on sunday of", month)
                                                    print('')
                                                    sunday = int(input("→ "))
                                                    sunday = (num_hrs * rate) * sunday * 1.50
                                                    print('')
                                                except ValueError:
                                                    print('')
                                                    print('***Input Invalid***')
                                                else:
                                                    while True:
                                                        try:
                                                            print('')
                                                            print("Please Enter overtime hours")
                                                            print('')
                                                            overtime = int(input("→ "))
                                                            overtime = (overtime * rate * 1.25)
                                                        except ValueError:
                                                            print('')
                                                            print('***Input Invalid***')
                                                        else:
                                                            while True:
                                                                try:
                                                                    print('')
                                                                    print("Please Enter how many times you worked halfday")
                                                                    print('')
                                                                    halfday = int(input("→ "))
                                                                    halfday = (halfday * (num_hrs / 2) * rate)
                                                                    print('')
                                                                except ValueError:
                                                                    print('')
                                                                    print('***Input Invalid***')
                                                                else:
                                                                    while True:
                                                                        try:
                                                                            print('')
                                                                            print("if you are absent or Dayoff please Enter how many times")
                                                                            print('')
                                                                            absent = int(input("→ "))
                                                                            absent = (absent * num_hrs * rate)
                                                                            print('')
                                                                        except ValueError:
                                                                            print('')
                                                                            print('***Input Invalid***')
                                                                        else:
                                                                            # program will calculate deduction depend on how many days in a month.
                                                                            if month in month1:
                                                                                if month in holiday1:
                                                                                    num_hrs = (num_hrs * 23)
                                                                                elif month in holiday2:
                                                                                    num_hrs = (num_hrs * 22)
                                                                                elif month in holiday3:
                                                                                    num_hrs = (num_hrs * 21)
                                                                                elif month in holiday4:
                                                                                    num_hrs = (num_hrs * 20)
                                                                                elif month in holiday5:
                                                                                    num_hrs = (num_hrs * 19)
                                                                                elif month in holiday6:
                                                                                    num_hrs = (num_hrs * 18)

                                                                            elif month in month2:
                                                                                if month in holiday1:
                                                                                    num_hrs = (num_hrs * 25)
                                                                                elif month in holiday2:
                                                                                    num_hrs = (num_hrs * 24)
                                                                                elif month in holiday3:
                                                                                    num_hrs = (num_hrs * 23)
                                                                                elif month in holiday4:
                                                                                    num_hrs = (num_hrs * 22)
                                                                                elif month in holiday5:
                                                                                    num_hrs = (num_hrs * 21)
                                                                                elif month in holiday6:
                                                                                    num_hrs = (num_hrs * 20)

                                                                            elif month in month3:
                                                                                if month in holiday1:
                                                                                    num_hrs = (num_hrs * 25)
                                                                                elif month in holiday2:
                                                                                    num_hrs = (num_hrs * 24)
                                                                                elif month in holiday3:
                                                                                    num_hrs = (num_hrs * 23)
                                                                                elif month in holiday4:
                                                                                    num_hrs = (num_hrs * 22)
                                                                                elif month in holiday5:
                                                                                    num_hrs = (num_hrs * 21)
                                                                                elif month in holiday6:
                                                                                    num_hrs = (num_hrs * 40)


                                                                            ah = absent + halfday
                                                                            # this will be the total salary of the employee.
                                                                            expected = num_hrs * rate

                                                                            tgross_pay = ((num_hrs * rate) + overtime + sunday + holiday)

                                                                            gross_pay = ((num_hrs * rate) + overtime + sunday + holiday) - (absent + halfday)

                                                                            def payslip_nobalance():
                                                                                print("")
                                                                                print("====================DETAILS====================")
                                                                                print('')
                                                                                print('EMPLOYEE NAME:', fname.upper())
                                                                                print('')
                                                                                print('--GROSS PAY  : NO BALANCE--')
                                                                                print('')
                                                                                print("----------Please See The HR Thank you----------")
                                                                                print("")
                                                                                print("====================DETAILS====================")
                                                                                exit()

                                                                            def payslip_belowaverage():
                                                                                print("*****YOU ARE REQUIRED TO SEE THE 'HR' ASAP THANK YOU!*****")
                                                                                print('')
                                                                                print('---------------', month.upper(), '---------------')
                                                                                print('')
                                                                                print('EMPLOYEE NAME:', fname.upper())
                                                                                print('')
                                                                                print("EXPECTED SALARY IN A MONTH")
                                                                                print('----------{:.1f}----------'.format(tgross_pay))
                                                                                print('')
                                                                                print('----------DEDUCT----------')
                                                                                print('ABSENT       :', absent, 'PESOS')
                                                                                print('HAFTDAY      :', halfday, 'PESOS')
                                                                                print('--TOTAL DEDUCT : {:.1f}--'.format(absent + halfday))
                                                                                print('----------DEDUCT----------')
                                                                                print('')
                                                                                print('--GROSS PAY  : {:.1f}--'.format(gross_pay))
                                                                                print('')
                                                                                print("*****YOU ARE REQUIRED TO SEE THE 'HR' ASAP THANK YOU!*****")
                                                                                print('')
                                                                                exit()

                                                                            def payslip():
                                                                                import time
                                                                                t = time.ctime()
                                                                                print(t)
                                                                                print("")
                                                                                print("====================DETAILS====================")
                                                                                print('---------------', month.upper(),'---------------')
                                                                                print('')
                                                                                print('-----',t,'-----')
                                                                                print("")
                                                                                print('EMPLOYEE NAME:', fname.upper())
                                                                                print('')
                                                                                print("EXPECTED SALARY IN A MONTH")
                                                                                print('----------{:.1f}----------'.format(expected))
                                                                                print('')
                                                                                print("-----------ADDITIONAL-----------")
                                                                                print('HOLIDAY       :', holiday, 'PESOS')
                                                                                print('SUNDAY        :', sunday,'PESOS')
                                                                                print('OVERTIME      :', overtime,'PESOS')
                                                                                print("-----------ADDITIONAL-----------")
                                                                                print('')
                                                                                print("TOTAL SALARY IN A MONTH")
                                                                                print('----------{:.1f}----------'.format(tgross_pay))
                                                                                print('')
                                                                                print("----------DEDUCTION----------")
                                                                                print('ABSENT       :', absent, 'PESOS')
                                                                                print('HAFTDAY      :', halfday,'PESOS')
                                                                                print("----------DEDUCTION----------")
                                                                                print('')
                                                                                print('--GROSS PAY  : {:.1f}--'.format(gross_pay))
                                                                                print('')
                                                                                print('**********DEDUCTION**********')
                                                                                print('PHILHEALTH   : {}'.format(philhealth), '  Pesos')
                                                                                print('PAGIBIG      : {}'.format(pagibig),'   Pesos')
                                                                                print('SSS          : {}'.format(sss),'  Pesos')
                                                                                print('--TOTAL DEDUCT : {:.1f}--'.format(total_deduct))
                                                                                print('**********DEDUCTION**********')
                                                                                print('')
                                                                                print('--NETPAY     : {:.1f}--'.format(net_pay))
                                                                                print('')
                                                                                print("====================DETAILS====================")
                                                                                print('')
                                                                                Return = input("Do you want to return Main? (Y/N):")
                                                                                print("")
                                                                                if Return in yeslist:
                                                                                    payroll()
                                                                                else:
                                                                                    print('')
                                                                                    print("-------------Thank you! Come again.-------------")
                                                                                    exit()

                                                                            if ah > tgross_pay:
                                                                                payslip_nobalance()

                                                                            elif gross_pay < 1000:
                                                                                payslip_belowaverage()

                                                                            # Deduction of total gross depend on employee salary.
                                                                            elif gross_pay >= 1000 and gross_pay <= 1249.99:
                                                                                sss = 36.30
                                                                                philhealth = 100
                                                                                pagibig = 29.98
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 1250 and gross_pay <= 1749.99:
                                                                                sss = 54.50
                                                                                philhealth = 100
                                                                                pagibig = 29.98
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 1750 and gross_pay <= 2249.99:
                                                                                sss = 72.70
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 2250 and gross_pay <= 2749.99:
                                                                                sss = 90.80
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 2750 and gross_pay <= 3249.99:
                                                                                sss = 109
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 3250 and gross_pay <= 3749.99:
                                                                                sss = 127.20
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 3750 and gross_pay <= 4249.99:
                                                                                sss = 145.30
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 4250 and gross_pay <= 4749.99:
                                                                                sss = 163.50
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 4750 and gross_pay <= 5249.99:
                                                                                sss = 181.70
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 5250 and gross_pay <= 5749.99:
                                                                                sss = 199.80
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 5750 and gross_pay <= 6249.99:
                                                                                sss = 218
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 6250 and gross_pay <= 6749.99:
                                                                                sss = 236.20
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 6750 and gross_pay <= 7249.99:
                                                                                sss = 254.20
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 7250 and gross_pay <= 7749.99:
                                                                                sss = 272.50
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 7750 and gross_pay <= 8249.99:
                                                                                sss = 290.70
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 8250 and gross_pay <= 8749.99:
                                                                                sss = 308.80
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 8750 and gross_pay <= 9249.99:
                                                                                sss = 327
                                                                                philhealth = 100
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 9250 and gross_pay <= 9749.99:
                                                                                sss = 345.20
                                                                                philhealth = 112
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 9750 and gross_pay <= 10249.99:
                                                                                sss = 363.30
                                                                                philhealth = 112
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 10250 and gross_pay <= 10749.99:
                                                                                sss = 381.50
                                                                                philhealth = 125
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 10750 and gross_pay <= 11249.99:
                                                                                sss = 399.70
                                                                                philhealth = 125
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            elif gross_pay >= 11250 and gross_pay <= 11749.99:
                                                                                sss = 417.80
                                                                                philhealth = 137
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)

                                                                            else:
                                                                                sss = 436
                                                                                philhealth = 137
                                                                                pagibig = 60
                                                                                total_deduct = (sss + philhealth + pagibig)
                                                                                net_pay = (gross_pay - total_deduct)


                                                                            # this will ask the employee if he/she wants to see the payslip or restart the system or exit .
                                                                            while True:
                                                                                print('')
                                                                                menu = input("Do you want to see the payslip? type: 'Y' or ('N' to restart) or ('X' to exit)")
                                                                                if menu in yeslist:
                                                                                    payslip()
                                                                                elif menu in nolist:
                                                                                    payroll()
                                                                                elif menu == 'x' or menu == 'X':
                                                                                    print('')
                                                                                    print("-------------Thank you! Come again.-------------")
                                                                                    exit()
                                                                                else:
                                                                                    print('')
                                                                                    print("-----Please read the instruction above thank you!-----")

                else:
                    print('')
                    print("--Please select only from the selection above thankyou--")
                    print('')

        else:
            print('')
            print('You have', x, 'Attemp left')
            print('')
            if x == 1:
                print('')
                print("***This is your last Attemp***")
                print('')
            if x == 0:
                print("Try again after 15 seconds.")
                import time
                import sys
                for i in reversed(range(8)):
                    sys.stdout.write('\rPlease wait ◜ .')
                    time.sleep(0.3)
                    sys.stdout.write('\rPlease wait ◠ ..')
                    time.sleep(0.3)
                    sys.stdout.write('\rPlease wait ◝ ...')
                    time.sleep(0.3)
                    sys.stdout.write('\rPlease wait ◞ ....')
                    time.sleep(0.3)
                    sys.stdout.write('\rPlease wait ◡ .....')
                    time.sleep(0.3)
                    sys.stdout.write('\rPlease wait ◟ ')
                    time.sleep(0.3)
                    sys.stdout.write('\rDone!   ')
                payroll()

payroll()
