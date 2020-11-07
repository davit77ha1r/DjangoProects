#swith open('read.txt',"r") as file:
    #read_value = file.read()
    #print(read_value)
    #   The 5 characters
    #read_value = file.read(5)
    # for line in file:
    #   print(line)
    #print(read_value)
# with open("read.json","w") as file:
#     file.write("Helloooooooooooooo")
# with open("read.txt","a")as file:
#     file.write("ooooook")
import json
with open("sample_json.json","r") as file2:
    data = json.load(file2)
#print(data)
print(type(data))
print(data["items"][0])