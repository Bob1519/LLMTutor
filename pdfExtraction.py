import pdfplumber


#Extracts the text from a pdf and places into a text file
with pdfplumber.open("practice exam.pdf") as pdf ,open("output.txt", "w", encoding="utf-8") as f:

    for page in pdf.pages:
        t = page.extract_text()
        if t:
            f.write(t + '\n')