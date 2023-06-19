text = "We are going to learn six methods today"
result1 = text[4].upper()
result2 = text.lower()
result3 = text.split('o')
result4 = text.find("q")
# result = text.replace("e", "x")
# print(result)
#
# a = "learning"
# b = "Python"
# c = "is"
# d = "amazing"
# e = "-".join([a, b, c, d])
# print(e)
#
# word_list = ["Simple","is","better","than","complex."]
# result = " ".join(word_list)
# print(result)

text = "If the implementation is hard to explain, it might be a bad idea."
text = text.replace("hard", "easy")
text = text.replace("bad", "good")

print(text)

