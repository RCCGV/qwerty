def polindrom(word: str):
    if word.lower() == word.lower()[::-1]:
        print('True')
        return True
    else:
        print('False')
        return False
    
polindrom(input('Введите слово: '))


