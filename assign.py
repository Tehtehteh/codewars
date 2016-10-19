def main():
    prices = {
        'Canada': {
            'Alberta': lambda x: x * 2,
            'Ontario': lambda x: x * 3,
            'Default': lambda x: x * 4
        },
        'Usa': lambda x: x
    }
    choice = input('Your country?\n').title()
    if choice not in prices:
        print('Wrong destination country.')
        return
    else:
        price = int(input('Value?\n'))
        if choice == 'Canada':
            state = input('Which state?\n')
            print('Total price is ', prices[choice][state](price))
        else:
            print('Total price is ', prices[choice](price))

if __name__ == '__main__':
    main()
