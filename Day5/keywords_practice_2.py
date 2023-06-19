def list_attributes(**kwargs):
    attribute = []
    for key, value in kwargs.items():
        attribute.append(value)
    return attribute


print(list_attributes(x='one', y='two'))
