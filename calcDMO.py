import math

while True:
    def clonAT():
        while True:
            clon1 = int(input("Put your base stats: "))
            clon2 = int(input("Put your clon stats: "))

            isinstance(clon1, int)
            isinstance(clon2, int)

            check = str((input("Your base stats is {} and clon stats is {}? [Y/N]: ".format(clon1, clon2))))

            if check.startswith(("Y")) or check.startswith(("y")):
                    print("Ok")
            else:
                continue
            break

        while True:
            levelclon = int(input("Put your clonlevel: "))
                    
            if(levelclon > 15):
                print("Your level clon is invalid.")
                continue
            elif(levelclon < 1):
                print("Your level clon is invalid.")
                continue
            break

        finalvalue = (clon2 / clon1 * 100)
        print("%2f" % finalvalue,"%")

        def missingAT(x):
            perfect = (clon1 * x)
            ATTotal = perfect - clon2
            return int(ATTotal)

        def result(x, y, z):
                if(finalvalue > x):
                    return print("This is not a valid clon. (Higher % than maximum value possible)")
                elif(finalvalue > y):
                    return print("Your clon is perfect!")
                else:
                    return print("Your clon is not perfect! You are missing", int(missingAT(z)), "Attack")

        if(levelclon == 15):
            result15 = result(144, 143, 1.44)
        elif(levelclon == 14):
            result14 = result(129, 128, 1.29)
        elif(levelclon == 13):
            result13 = result(114, 113, 1.14)
        elif(levelclon == 12):
            result12 = result(99, 98, 0.99)
        elif(levelclon == 11):
            result11 = result(84, 83, 0.84)
        elif(levelclon == 10):
            result10 = result(69, 68, 0.69)
        elif(levelclon == 9):
            result9 = result(54, 53, 0.54)
        elif(levelclon == 8):
            result8 = result(44, 43, 0.44)
        elif(levelclon == 7):
            result7 = result(34, 33, 0.34)
        elif(levelclon == 6):
            result6 = result(24, 23, 0.24)
        elif(levelclon == 5):
            result5 = result(19, 18, 0.19)
        elif(levelclon == 4):
            result4 = result(14, 13, 0.14)
        elif(levelclon == 3):
            result3 = result(9, 8, 0.09)
        elif(levelclon == 2):
            result2 = result(6, 5, 0.06)
        elif(levelclon == 1):
            result1 = result(3, 2, 0.02)
    def clonCT():
        while True:
            clon1 = float(input("Put your base stats: "))
            clon2 = float(input("Put your clon stats: "))

            isinstance(clon1, int)
            isinstance(clon2, int)

            check = str((input("Your base stats is {} and clon stats is {}? [Y/N]: ".format(clon1, clon2))))

            if check.startswith(("Y")) or check.startswith(("y")):
                        print("Ok")
            else:
                continue
            break

        while True:
            levelclon = int(input("Put your clonlevel: "))
                    
            if(levelclon > 15):
                print("Your level clon is invalid.")
                continue
            elif(levelclon < 1):
                print("Your level clon is invalid.")
                continue
            break

        finalvalue = (clon2 / clon1 * 100)
        print("%2f" % finalvalue, "%")

        def missingAT(x):
            perfect = (clon1 * x)
            ATTotal = perfect - clon2
            return (ATTotal)

        def result(x, y, z):
                if(finalvalue > x):
                    return print("This is not a valid clon. (Higher % than maximum value possible)")
                elif(finalvalue > y):
                    return print("Your clon is perfect!")
                else:
                    return print("Your clon is not perfect! You are missing", round(missingAT(z)), "%", "Critical Rate")


        if(levelclon == 15):
            result15 = result(720, 719, 7.20)
        elif(levelclon == 14):
            result14 = result(645, 644, 6.45)
        elif(levelclon == 13):
            result13 = result(570, 569, 5.70)
        elif(levelclon == 12):
            result12 = result(495, 494, 4.95)
        elif(levelclon == 11):
            result11 = result(420, 419, 4.20)
        elif(levelclon == 10):
            result10 = result(345, 344, 3.45)
        elif(levelclon == 9):
            result9 = result(270, 269, 2.70)
        elif(levelclon == 8):
            result8 = result(220, 219, 2.20)
        elif(levelclon == 7):
            result7 = result(170, 169, 1.70)
        elif(levelclon == 6):
            result6 = result(120, 119, 1.20)
        elif(levelclon == 5):
            result5 = result(95, 94, 0.95)
        elif(levelclon == 4):
            result4 = result(70, 69, 0.70)
        elif(levelclon == 3):
            result3 = result(45, 44, 0.45)
        elif(levelclon == 2):
            result2 = result(30, 29, 0.30)
        elif(levelclon == 1):
            result1 = result(15, 14, 0.15)
    def clonHP():
        while True:
            clon1 = int(input("Put your base stats: "))
            clon2 = int(input("Put your clon stats: "))

            isinstance(clon1, int)
            isinstance(clon2, int)

            check = str((input("Your base stats is {} and clon stats is {}? [Y/N]: ".format(clon1, clon2))))

            if check.startswith(("Y")) or check.startswith(("y")):
                print("Ok")
            else:
                continue
            break

        while True:
            levelclon = int(input("Put your clonlevel: "))
                    
            if(levelclon > 15):
                print("Your level clon is invalid.")
                continue
            elif(levelclon < 1):
                print("Your level clon is invalid.")
                continue
            break

        finalvalue = (clon2 / clon1 * 100)
        print("%2f" % finalvalue,"%")

        def missingAT(x):
            perfect = (clon1 * x)
            ATTotal = perfect - clon2
            return int(ATTotal)

        def result(x, y, z):
                if(finalvalue > x):
                    return print("This is not a valid clon. (Higher % than maximum value possible)")
                elif(finalvalue > y):
                    return print("Your clon is perfect!")
                else:
                    return print("Your clon is not perfect! You are missing", int(missingAT(z)), "Health Points")

        if(levelclon == 15):
            result15 = result(54, 53, 0.54)
        elif(levelclon == 14):
            result14 = result(49, 48, 0.49)
        elif(levelclon == 13):
            result13 = result(44, 43, 0.44)
        elif(levelclon == 12):
            result12 = result(39, 38, 0.39)
        elif(levelclon == 11):
            result11 = result(35, 34, 0.35)
        elif(levelclon == 10):
            result10 = result(31, 30, 0.31)
        elif(levelclon == 9):
            result9 = result(27, 26, 0.27)
        elif(levelclon == 8):
            result8 = result(23, 22, 0.23)
        elif(levelclon == 7):
            result7 = result(19, 18, 0.19)
        elif(levelclon == 6):
            result6 = result(15, 14, 0.15)
        elif(levelclon == 5):
            result5 = result(12, 11, 0.12)
        elif(levelclon == 4):
            result4 = result(9, 8, 0.09)
        elif(levelclon == 3):
            result3 = result(6, 5, 0.06)
        elif(levelclon == 2):
            result2 = result(4, 3, 0.04)
        elif(levelclon == 1):
            result1 = result(2, 1, 0.02)        
    def clonEV():
        while True:
            clon1 = float(input("Put your base stats: "))
            clon2 = float(input("Put your clon stats: "))

            isinstance(clon1, int)
            isinstance(clon2, int)

            check = str((input("Your base stats is {} and clon stats is {}? [Y/N]: ".format(clon1, clon2))))

            if check.startswith(("Y")) or check.startswith(("y")):
                        print("Ok")
            else:
                continue
            break

        while True:
            levelclon = int(input("Put your clonlevel: "))
                    
            if(levelclon > 15):
                print("Your level clon is invalid.")
                continue
            elif(levelclon < 1):
                print("Your level clon is invalid.")
                continue
            break

        finalvalue = (clon2 / clon1 * 100)
        print("%2f" % finalvalue, "%")

        def missingAT(x):
            perfect = (clon1 * x)
            ATTotal = perfect - clon2
            return (ATTotal)

        def result(x, y, z):
                if(finalvalue > x):
                    return print("This is not a valid clon. (Higher % than maximum value possible)")
                elif(finalvalue > y):
                    return print("Your clon is perfect!")
                else:
                    return print("Your clon is not perfect! You are missing", int(round(missingAT(z))), "%", "Evasion")

        if(levelclon == 15):
            result15 = result(576, 575, 5.76)
        elif(levelclon == 14):
            result14 = result(516, 515, 5.16)
        elif(levelclon == 13):
            result13 = result(456, 455, 4.56)
        elif(levelclon == 12):
            result12 = result(396, 395, 3.96)
        elif(levelclon == 11):
            result11 = result(336, 335, 3.36)
        elif(levelclon == 10):
            result10 = result(276, 275, 2.76)
        elif(levelclon == 9):
            result9 = result(216, 215, 2.16)
        elif(levelclon == 8):
            result8 = result(176, 175, 1.76)
        elif(levelclon == 7):
            result7 = result(136, 135, 1.36)
        elif(levelclon == 6):
            result6 = result(96, 95, 0.96)
        elif(levelclon == 5):
            result5 = result(76, 75, 0.76)
        elif(levelclon == 4):
            result4 = result(56, 55, 0.56)
        elif(levelclon == 3):
            result3 = result(36, 35, 0.36)
        elif(levelclon == 2):
            result2 = result(24, 23, 0.24)
        elif(levelclon == 1):
            result1 = result(12, 11, 0.12)
         
    while True:
        select = str(input("Select what clon you want to calculate [AT/HP/CT/BL/EV]: "))

        if select.startswith(("at")) or select.startswith(("AT")) or select.startswith(("At")):
            clonAT()
        if select.startswith(("ct")) or select.startswith(("CT")) or select.startswith(("Ct")) or select.startswith(("Cr")) or select.startswith(("cr")) or select.startswith(("CR")):
            clonCT()
        if select.startswith(("HP")) or select.startswith(("hp")) or select.startswith(("Hp")) or select.startswith(("He")) or select.startswith(("he")) or select.startswith(("HE")):
            clonHP()
        if select.startswith(("ev")) or select.startswith(("EV")) or select.startswith(("Ev")):
            clonEV()
        else:
            continue
        break