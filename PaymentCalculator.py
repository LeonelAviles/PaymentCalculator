def is_file(filename):
    try:
        fh=open(filename,'r')
        fh.close()
        return True
    except FileNotFoundError:
        return False
#this functions calculates the employees with maximum and/or minimum hrs
def max_hours(fhandle):
    largest = None
    for line in fhandle:
        if not line.startswith('time'):
            comma = line.find(',')
            comma2 = line.find(',',comma+1)
            name = line[:comma]
            hrs = float(line[comma+1:comma2])
            if largest == None or hrs > largest:
                largest = hrs
                worker = name
            elif hrs == largest:
                worker = worker + ','+ name
    print('The employee or employees with maximum hours:', worker)
def minimum_hours(fhandle):
    minimum = None
    for line in fhandle:
        if not line.startswith('time'):
            comma = line.find(',')
            comma2 = line.find(',', comma + 1)
            name = line[:comma]
            hrs = float(line[comma + 1:comma2])
            if minimum == None or hrs < minimum:
                minimum = hrs
                worker = name
            elif hrs == minimum:
                worker = worker + ',' + name
    print('The employee or employees with minimum hours:', worker)
#this functions calculates the employees with maximum and/or minimum rate
def max_rate(fhandle):
    maxrate = None
    for line in fhandle:
        if not line.startswith('time'):
            comma = line.find(',')
            comma2 = line.find(',', comma + 1)
            name = line[:comma]
            rate = float(line[comma2+1:])
            if maxrate == None or rate > maxrate:
                maxrate = rate
                worker = name
            elif rate == maxrate:
                worker = worker + ',' + name
    print('The employee or employees with maximum rate:', worker)
def min_rate(fhandle):
    minrate = None
    for line in fhandle:
        if not line.startswith('time'):
            comma = line.find(',')
            comma2 = line.find(',', comma + 1)
            name = line[:comma]
            rate = float(line[comma2+1:])
            if minrate == None or rate < minrate:
                minrate = rate
                worker = name
            elif rate == minrate:
                worker = worker + ',' + name
    print('The employee or employees with maximum rate:', worker)

def calculate_payment(fhandle):
    open_new_file = open('employees_payment.txt', 'w')
    print('A file employees_payment.txt containing the payment information has been created.')
    for line in fhandle:
        if ',' in line:
            comma = line.find(',')
            comma2 = line.find(',', comma + 1)
            name = line[:comma]
            hrs = float(line[comma + 1:comma2])
            rate = float(line[comma2 + 1:])
            pay = None
            if hrs >= 40 and rate > 50:
                pay = hrs * rate
            elif hrs <= 40:
                pay = hrs * rate
            else:
                pay = 40 * rate + (hrs - 40) * (rate * 1.5)
            open_new_file.write(name + ' ' + '$' + str(pay) + '\n')

def print_program_menu():
    print("\n")
    print("Welcome to payment calculator. Please, choose an option:")
    print("1. Employees payment (will create a employees_payment.txt file)")
    print("2. Employee name with maximum number of work hours")
    print("3. Employee name with minimum number of work hours")
    print("4. Employee name with maximum rate")
    print("5. Employee name with minimum rate")
    print("6. Exit")
    print('\n')
def identify_option(user_option):
    try:
        numeric_option = int(user_option)
    except:
        return -1
    if user_option.isdigit() :
        numeric_option = int(user_option)
        if numeric_option >= 1 and numeric_option <= 6:
            return numeric_option
        else:
            return -1 # invalid option
    else:
        return -1 # invalid option
def process_request(option_info):
    filename = input("Enter the name of the file to be processed: ")
    if is_file(filename):
        fhandle = open(filename,'r') #open file
        if option_info == 1:
            calculate_payment(fhandle)
        elif option_info == 2:
            max_hours(fhandle)
        elif option_info == 3:
            minimum_hours(fhandle)
        elif option_info == 4:
            max_rate(fhandle)
        elif option_info == 5:
            min_rate(fhandle)
    else:
        print("Illegal file name. Input file was not found")
def main():
    done = False
    while not done:
        print_program_menu()
        user_option = input("Enter option: ")
        option_info = identify_option(user_option)
        if option_info != -1:
            #option was valid
            if option_info == 6:
                done = True
                print("Thanks for using the payment calculation program")
            else:
                process_request(option_info)
        else:
            #option invalid
            print("Please enter a numeric option from the menu\n")
main()