from gtts import gTTS
import PyPDF2
book = open("sample.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)

myText = ""

for num in range(pdfReader.numPages):
    page = pdfReader.getPage(num)
    myText = myText + page.extractText()
print(myText)
book.close()

out = gTTS(myText, lang="en")
out.save("output.mp3")
