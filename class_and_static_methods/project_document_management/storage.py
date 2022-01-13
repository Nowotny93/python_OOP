class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        desired_category = [c for c in self.categories if c.id == category_id][0]
        desired_category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        desired_topic = [t for t in self.topics if t.id == topic_id][0]
        desired_topic.storage_folder = new_storage_folder
        desired_topic.topic = new_topic

    def edit_document(self, document_id, new_file_name):
        desired_document = [d for d in self.documents if d.id == document_id][0]
        desired_document.file_name = new_file_name

    def delete_category(self, category_id):
        cat_to_be_del = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(cat_to_be_del)

    def delete_topic(self, topic_id):
        top_to_be_del = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(top_to_be_del)

    def delete_document(self, document_id):
        doc_to_be_del = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(doc_to_be_del)

    def get_document(self, document_id):
        doc_to_be_got = [d for d in self.documents if d.id == document_id][0]
        return doc_to_be_got

    def __repr__(self):
        result = ''
        for doc in self.documents:
            result += f'{doc}'
        return result
