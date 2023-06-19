import zipfile

# my_zip = zipfile.ZipFile("file_compressed.zip", "w")
#
# my_zip.write("My_Text_A.txt")
# my_zip.write("My_Text_B.txt")
#
# my_zip.close()


#################################################################

# TO EXTRACT

open_zip = zipfile.ZipFile("Project+Day+9.zip", "r")

open_zip.extractall()

################################################################
