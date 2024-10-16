# To create and initialize the modules for the database

from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

class DBFiles:
    def __init__(self, files):
        self.documents = [] # Documents to hold the data that is read frm the file
        self.chunks = []    # List to store all the chunks of Data
        self.textsplitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.getData(files)

    def getData(self, files):
        #print(files)
        textfiles, pdffiles = self.segregateFiles(files)
        #print(textfiles, pdffiles)
        documents = self.readTextFiles(textfiles)
        documents.extend(self.readPdfFiles(pdffiles))
        self.chunks = self.partitionData(documents)
        self.documents = documents

    def addData(self, newdocuments):
        self.documents.extend(newdocuments)
        newchunks = self.partitionData(newdocuments)
        self.chunks.extend(newchunks)

    def partitionData(self, documents):
        chunks = self.textsplitter.split_documents(documents)
        return chunks

    def segregateFiles(self, files):
        textfiles, pdffiles = [], []
        for file in files:
            extension = file[-4:]
            if extension == '.txt':
                textfiles.append(file)
            elif extension == ".pdf":
                pdffiles.append(file)
        return textfiles, pdffiles
    
    def readTextFiles(self, files):
        documents = []
        for file in files:
            doc = self.readTextFile(file)
            if doc:
                documents.extend(doc)
        return documents
    
    def readTextFile(self, file):
        if os.path.exists(file):
            doc = TextLoader(file)
            return doc.load()
        else:
            return None
    
    def readPdfFile(self, file):
        if os.path.exists(file):
            doc = PyPDFLoader(file)
            return doc.load()
        else:
            return None

    def readPdfFiles(self, files):
        documents = []
        for file in files:
            doc = self.readPdfFile(file)
            if doc:
                documents.extend(doc)
        return documents


dbfile = DBFiles(["/home/user/legal-bot/constitution_of_india.pdf"])

# print(type(dbfile.chunks[0]), len(dbfile.documents))
cnt = 0
for file in dbfile.documents:
    cnt += 1
    print(file)

print(cnt)