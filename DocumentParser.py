import os
from bs4 import BeautifulSoup


class Parser:

    def __init__(self):
        pass

    def parse_document(self, file_name):

        soup = BeautifulSoup(open(file_name, 'r'), 'html.parser')
        texts = soup.find("pre")
        return texts.text

    def get_documents(self, directory_name):
        return os.listdir(directory_name)







