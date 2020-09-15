from gtts import gTTS
import PyPDF2
book = open("C:\\Users\\Ranjan\\Desktop\\sample.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)

myText = ""

for num in range(pdfReader.numPages):
    page = pdfReader.getPage(num)
    myText = myText + page.extractText()
print(myText)
book.close()

o = gTTS(myText, lang="en")
o.save("story.mp3")
