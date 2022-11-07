
while True:
    # enter your number
    num1 = input('please enter your first number:')
    num2 = input('please enter you second number:')

    # wash data
    num1 = float(num1)
    num2 = float(num2)

    # calc
    result = num1 + num2

    # output
    print('your result is:', result)

    isQ = input('Do you want to quit: please enter \'q\':')
    if isQ == 'q':
        break

