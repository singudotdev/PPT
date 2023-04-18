import PyPDF2

# Open PDF in binary read mode
with open(input("Insert file path: "), 'rb') as file:
    # Create PdfFileReader object in order to read PDF
    reader = PyPDF2.PdfReader(file)

    # Access to PDF metadata
    metadata = reader.metadata

    # Print metadata
    print("Title:", metadata.title)
    print("Author:", metadata.author)
    print("Subject:", metadata.subject)
    print("Producer:", metadata.producer)
    print("Created at:", metadata.get('/CreationDate'))
    print("Modified at:", metadata.get('/ModDate'))
