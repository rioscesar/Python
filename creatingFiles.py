'''fw = open("sample.txt", "w")
fw.write("Writing to file")
fw.close()'''

fr = open("sample.txt", "r")
text = fr.read()
print(text)
fr.close()