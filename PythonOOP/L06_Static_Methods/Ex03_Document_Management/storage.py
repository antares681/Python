from Ex03_Document_Management.category import Category
from Ex03_Document_Management.document import Document
from Ex03_Document_Management.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)


    def edit_category(self, category_id: int, new_name:str):
        for category in self.categories:
            if category.id == category_id:
                category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder):
        topic = [topic for topic in self.topics if topic.id == topic_id][0]
        for tp in self.topics:
            if tp == topic:
                tp.topic = new_topic
                tp.storage_folder = new_storage_folder


    def edit_document(self, document_id: int, new_file_name: str):
        document = [doc for doc in self.documents if doc.id == document_id][0]
        for doc in self.documents:
            if doc == document:
                doc.file_name = new_file_name


    def delete_category(self, category_id: int):
        for category in self.categories:
            if category.id == category_id:
                self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = [topic for topic in self.topics if topic.id == topic_id][0]
        for tp in self.topics:
            if tp == topic:
                self.topics.remove(tp)


    def delete_document(self, document_id: int):
        document = [doc for doc in self.documents if doc.id == document_id][0]
        if document and document in self.documents:
            self.documents.remove(document)


    def get_document(self, document_id):
        return [document for document in self.documents if document.id == document_id][0]


    def __repr__(self):
        return "\n".join([doc.__repr__() for doc in self.documents])
