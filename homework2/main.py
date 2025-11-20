def level1(text: str, method: str):
    if method == 'upper':
        return text.upper()
    elif method == 'lower':
        return text.lower()
    else:
        return text.capitalize()

def level2(text: str, method: str, what: str, replace_with: str):
    if method == 'find':
        return text.find(what)
    elif method == 'replace':
        return text.replace(what, replace_with)
    elif method == 'count':
        return text.count(what)
    elif method == 'index':
        return text.index(what)

def level3(text: str, method: str, separator: str):
    if method == 'split':
        return text.split(separator)
    else:
        return ''.join(text.split(separator))

def level4(text: str, method: str, items: list):
    if method == 'isdigit':
        return text.isdigit()
    elif method == 'isalpha':
        return text.isalpha()
    elif method == 'strip':
        return text.strip(''.join(items))
    else:
        return text.format(items)

print('Choose level (1, 2, 3, 4 or 5):')
level = int(input())

if level == 1:
    text = input('Enter your text: ')
    method = input('Choose method (upper/lower/capitalize): ')
    print('Your text:')
    print(level1(text, method))

elif level == 2:
    text = input('Enter your text: ')
    method = input('Choose method (find/replace/count/index): ')
    what = input('Enter substring to work with: ')
    
    replace_with = ''
    if method == 'replace':
        replace_with = input('Enter zamena ')
    
    print('Your text:')
    print(level2(text, method, what, replace_with))

elif level == 3:
    text = input('Enter your text: ')
    method = input('Choose method (split/join): ')
    separator = input('Enter separator: ')
    print('Your text:')
    print(level3(text, method, separator))

elif level == 4:
    text = input('Enter your text: ')
    method = input('Choose method (isdigit/isalpha/strip/format): ')
    
    items = []
    if method in ['strip', 'format']:
        items_input = input('Enter items (space separated): ')
        items = items_input.split()
    
    print('Your text:')
    print(level4(text, method, items))

elif level == 5:
    s = 'pYtHon;is;AWESome;'
    s = s.replace(';', ' ')
    s = s.capitalize()
    print(s)
