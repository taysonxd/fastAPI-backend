
import os

# text_file = open('./file.txt', 'w+')

# text_file.write("Mi nombre es German\nMi apellido es Azuaje\ntengo 21 años\nmi lenguaje favorito es python")

# # print(text_file.read(10))
# # print(text_file.readline())
# # print(text_file.readline())

# # for line in text_file.readlines():
# #     print(line)

# text_file.write('\nAunque tambien me gusta javascript')

# # print(text_file.readline())

# text_file.close()

# # os.remove("./file.txt")

# with open("./file.txt", "a") as my_file:
#     my_file.write("\nY PHP")


# #  json files

# import json

# json_file = open('./json_file.json', 'w+')

# json_text = {
#     "name": "german",
#     "lastname": "azuaje",
#     "age": 31,
#     "languages": ["python", "javascript", "nodejs", "php"],
#     "website": "none"
# }

# json.dump(json_text, json_file, indent= 4)

# json_file.close()

# with open('./json_file.json', 'r') as json_file:
#     for line in json_file.readlines():
#         print(line)

# json_dict = json.load(open('./json_file.json'))
# print(json_dict, type(json_dict))
# print(json_dict['name'])

#  csv file

import csv

csv_file = open('./csv_file.csv', 'w+')
writer = csv.writer(csv_file)

writer.writerow(['name','lastname','age','language','website'])
writer.writerow(['German','Azuaje',31,'Python','ninguna'])
writer.writerow(['roswell','**',2,'COBOL','ninguna'])

csv_file.close()

with open('./csv_file.csv') as csv_file:
    for line in csv_file.readlines():
        print(line)
