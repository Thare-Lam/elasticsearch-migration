from elasticsearch import Elasticsearch


class MigEs:

    def __init__(self, conf):
        self.index = conf['index']
        self.doc_type = conf['type']
        self.es = Elasticsearch([conf['host']])