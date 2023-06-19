from collections import Counter, defaultdict, namedtuple

# numbers = [8,6,5,4,3,2,7,6,8,6,5,4,7,82,3,2,4,5,6,5]
# print(Counter(numbers))
# print(Counter("mississippi"))

# sentence = 'you will never win if you never begin'
# print(Counter(sentence.split()))


# numbers = Counter([8,6,5,4,3,2,7,6,8,6,5,4,7,2,3,2,4,5,6,5,6])
# print(list(numbers))
# print(numbers.most_common())
# print(numbers.values())
# print(numbers.keys())
# print(numbers.total())


########################################################

# my_dict = {"one": "green", "two": "blue", "three": "red"}
# my_dic = defaultdict(lambda: "nothing")
# my_dic["one"] = "green"
# print(my_dic["two"])
# print(my_dic)

#######################################################

person = namedtuple('person', ["name", "height", "weight"])

micheal = person("Micheal", 1.76, 79)

print(micheal[2])
