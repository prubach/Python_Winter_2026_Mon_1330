s = 'absfe'
match s:
    case 'abcd':
        print('s is abcd')
    case 'ab':
        print('s is ab')
    case _:
        print('s is not ab or abcd')

