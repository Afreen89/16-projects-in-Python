def change_letters(type):
    def uppercase(text):
        print(text.upper())

    def lowercase(text):
        print(text.lower())

    if type == 'upp':
        return uppercase
    elif type == 'low':
        return lowercase


operation = change_letters('upp')

operation('python')
