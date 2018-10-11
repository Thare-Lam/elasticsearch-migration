from mig_es import MigEs
from elasticsearch.helpers import bulk


class MigTargetEs(MigEs):

    def __init__(self, conf):
        super().__init__(conf)
        try:
            self.es.indices.create(index=self.index)
        except:
            pass

    def put_mapping(self, mapping):
        self.es.indices.put_mapping(index=self.index, doc_type=self.doc_type, body=mapping)

    def bulk_index(self, docs, executor, callback):
        def gen_data():
            for doc in docs:
                yield {
                    '_op_type': 'index',
                    '_index': self.index,
                    '_type': self.doc_type,
                    '_id': doc['_source']['id'],
                    '_source': doc['_source']
                }

        def do_bulk_index():
            resp = bulk(self.es, gen_data())
            callback(resp[0])
        executor.submit(do_bulk_index, )
