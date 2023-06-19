def decorate_greeting(function):
    def another_function(word):
        print('Hello')
        function(word)
        print('Goodbye')

    return another_function


# @decorate_greeting
def uppercase(text):
    print(text.upper())


# @decorate_greeting
def lowercase(text):
    print(text.lower())


"""
You can activate the decorators like above or you can create
a function within a function to execute a decorator
"""

decorated_uppercase = decorate_greeting(uppercase)
uppercase('afreen') # this will call the function without decorator
decorated_uppercase('afreen') # this will be with decorator
