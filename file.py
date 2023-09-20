# Python File Handling - Read & Write

# open("document path", mode="open mode")

# Absolute Document Path ex: C:/Users/user/Desktop/Python/read_file.txt
# Relative Document Path is based on the location of our program ex: read_file.txt

# mode="r" 读取
# mode="w" 覆写
# mode="a" 在原先的资料后写东西

# file = open("read_file.txt", mode="a", encoding="utf-8")
# print(file.write("\n你好我叫Darren."))
# file.close() # Why have to close the file? Because if not close it, it will occupy your computer resources and degrade your computer performance.

# this will auto close the file.
with open("read_file.txt", mode="a", encoding="utf-8") as file:
    file.write("\nOK,结束！")