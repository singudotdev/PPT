import PyPDF2

with open(input("Insert file path: "), 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    metadata = reader.metadata

    print("Title:", metadata.title)
    print("Author:", metadata.author)
    print("Subject:", metadata.subject)
    print("Producer:", metadata.producer)
    print("Created at:", metadata.get('/CreationDate'))
    print("Modified at:", metadata.get('/ModDate'))
