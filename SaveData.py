import datetime

# #format for person's details (first name, last name, mobile no., email, DOB, 'Whatsapp name')
# contact = {'vikesh': ('vikesh', 'patil', 8600700549, "vpatil8340@gmail.com", datetime.date(2000, 5, 5), 'Vikesh P', 'Birthday'),
#            'Shreyansh': ('Shreyansh', 'Patil', 1234567890, 'shreepatil@gmail.com', datetime.date(2019, 11, 6), 'Shreyansh P CS', 'Birthday', 'Python testing 1')
#            }
#
#
# # ----------------Store Data in Text file------------------
# for key, value in contact.items():  #Writing data in text file
#     with open('contacts.txt', mode='a') as f:
#
#         writeContent = f.write(str(value[0]) + " " + str(value[1]) + " " + str(value[2]) + " " + str(value[3]) + " " + value[4].isoformat())
#
#         for i in range(5, len(value)):
#             whatsapp_name = str(value[i]).split()
#             whatsapp_name = '_'.join(whatsapp_name)
#             writeContent = f.write(" " + whatsapp_name)
#         writeContent = f.write("\n")
#


#----------------CSV File------------------#

import csv

with open('csv.csv', mode='a') as f:
    fieldNames = ['First Name', 'Last Name', 'Mobile Number', 'Email', 'Date Of Birth', 'Whatsapp Group',
                  'Facebook Group']

    writer = csv.DictWriter(f, fieldnames=fieldNames)

    writer.writeheader()

    writer.writerow({'First Name': 'Vikesh', 'Last Name': 'Patil', 'Mobile Number': 8600700549,
                     'Email': 'vikesh.patil8340@gmail.com', 'Date Of Birth': '2019-11-11',
                     'Whatsapp Group': 'Python testing 1', 'Facebook Group': 'Birthday'})