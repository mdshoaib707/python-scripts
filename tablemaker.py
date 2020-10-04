DoContinue = 'y'

while DoContinue == 'y':
    tablenumber = int(input("Enter a number to print the table: "))
    for i in range(1,11):
        print(tablenumber, "X", i, "=", tablenumber*i)
    DoContinue = input('Do you want to continue? y/n ')

