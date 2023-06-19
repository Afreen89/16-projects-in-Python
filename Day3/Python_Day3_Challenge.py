# Controlling complexity is the essence of programming. Never trust a computer you can't throw out a window.
# Python is amazing, and interesting. I like programming. I enjoy learning as well.
text = input("Give me some of your favorite text: ").lower()
letters = list(input("and your favorite letters? ").lower())

# print(f"So your text is \n{text} \nand we'll do some analysis using  {letters} letters")
print(f"the letters are {letters}.")
# Task 1
print(f"'{letters[0]}' has appeared  {text.count(letters[0])} times in the text, \n"
      f"'{letters[1]}' has appeared  {text.count(letters[1])} times in the text, and \n"
      f"'{letters[2]}' has appeared  {text.count(letters[2])} times in the text.")

# Task 2
words = text.split()
print(f"We have found {len(words)} words in your text")

# Task 3
print(f"'{text[0]}' is the first letter and '{text[-1]}' is the last letter of the text")

# Task 4
text = list(text.split(" "))
text.reverse()
result = " ".join(text)
print(result)

# Task 5
is_python = "python" in text
dic = {True: "was", False: "was not"}
print(f"The word 'Python' {dic[is_python]} found in the text")
