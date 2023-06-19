import re
#
# text = "If you need help call (658)-598-9977 any time for online help"
#
# pattern = 'help'
#
# # search = re.search(pattern, text)
# # search2 = re.findall(pattern, text)
# # print(search2)
#
# for finding in re.finditer(pattern, text):
#     print(finding.span())

#################################################

# text = "call to 564-525-6588 right now"
#
# pattern1 = r'\d\d\d-\d\d\d-\d\d\d\d'
# pattern1 = r'\d{3}-\d{3}-\d{4}'
# pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# result = re.search(pattern, text)
#
# print(result)
# print(result.group(2))

################################################
#
# password = input("Password: ")
#
# pattern = r"\D{1}\w{7}"
#
# check = re.search(pattern, password)
#
# print(check)

#################################################

text = "Saturday and sunday this store is closed"

search1 = re.search(r'sunday|monday', text)
search2 = re.search(r'...lose', text)
search = re.search(r'^\D', text)


print(search)
