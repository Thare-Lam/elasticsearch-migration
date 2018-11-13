from mig_es import MigEs
from elasticsearch.helpers import bulk


class MigTargetEs(MigEs):

    def __init__(self, conf):
        super().__init__(conf)
        self.index_thread_num = conf['index_thread_num']
        try:
            self.es.indices.create(index=self.index)
        except:
            pass

    def put_mapping(self, mapping):
        self.es.indices.put_mapping(index=self.index, doc_type=self.doc_type, body=mapping)

    def bulk_index(self, docs, executor, callback):
        executor.submit(self.do_bulk_index, docs, callback)

    def do_bulk_index(self, docs, callback):
        bulk(self.es, self.gen_data(docs))
        callback(len(docs))

    def gen_data(self, docs):
        for doc in docs:
            source_id = doc['_id']
            source_source = doc['_source']
            handled_id = self.handle_id(source_id, source_source)
            handled_source = self.handle_source(source_id, source_source)

            if handled_id is None or handled_source is None:
                continue

            yield {
                '_op_type': 'index',
                '_index': self.index,
                '_type': self.doc_type,
                '_id': handled_id,
                '_source': handled_source
            }

    def handle_id(self, id, source):
        """
        handle id
        :param id: source id
        :return: target id. If return None, this doc will be ignored
        """
        return id

    def handle_source(self, id, source):
        """
        handle source
        :param source: source source
        :return: target source. If return None, this doc will be ignored
        """
        return source
