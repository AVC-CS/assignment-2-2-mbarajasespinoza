def main():
    whatTemp = input("Temperature? ")
    tempFloat = float(whatTemp)
    
    typeofCon = input("\tIn . . . ? \n\t1. Fahrenheit\n\t2. Celsius?\n")
    if typeofCon == "1":
        answer = (5/9)*(tempFloat - 32)
        print(whatTemp + " Fahrenheit =\n" + format(answer, '.2f') + " Celsius.\n")
    elif typeofCon == "2":
        answer = (tempFloat * 9/5) + 32
        print(whatTemp + " Celsius =\n" + format(answer, '.2f') + " Fahrenheit.\n")
    else:
        print("Error!\n")
        
    return 


if __name__ == '__main__':
    main()
