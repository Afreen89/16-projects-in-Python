# customer = {"name": "John",
#             "last_name": "Lennon",
#             "weight": 88,
#             "height": 1.76}
#
# query = (customer["last_name"])
#
# print(query)
#
# dic = {1: 55,
#        2: [10, 20, 30],
#        3: {"s1":100, "s2":200}}
#
# print(dic[3]["s2"])
#
# dic = {"k1": ["a", "b", "c"], "k2": ["d", "e", "f"]}
#
# print(dic["k2"][1].upper())
#
# dic = {1: "a", 2: "b"}
# print(dic)
# dic[3] = "c"
# print(dic)
#
# dic[2] = 'B'
# print(dic)
#
# print(dic.values())
# print(dic.items())

my_dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
print(my_dict["points"]["points2"][1])
#Use dictionary indices to extract the second item of points2