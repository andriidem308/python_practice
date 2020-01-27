from docx import Document
import openpyxl
import re
import datetime 

pattern = r"\_{2}\.\_{2}\.\_{4}"
pattern2 = r"\d{2}\.\d{2}\.\d{4}"

filename = input("Enter the filename(.docx): ")

document = Document(filename)  

dates = []

for paragraph in document.paragraphs:
    for run in paragraph.runs:
    	text = run.text
    	# print(text)
    	if(re.findall(pattern2, text) != []):
    		dates.append(re.findall(pattern2, text))
    	currDate = datetime.datetime.today().strftime("%d.%m.%Y")
    	result = re.sub(pattern, currDate, text)
    	run.text = result
# print(dates)
print("Dates: ")
for i in dates:
	for j in i:
		print(j)
document.save(filename)