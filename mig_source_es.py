from mig_es import MigEs


class MigSourceEs(MigEs):

    def __init__(self, conf):
        super().__init__(conf)
        self.size_per_search = conf.get('size_per_handle', 500)
        self.scroll_alive = conf.get('scroll_alive', '1m')
        self.dsl = conf.get('dsl', {})

    def get_mapping(self):
        mapping = self.es.indices.get_mapping(index=self.index, doc_type=self.doc_type)
        return mapping[self.index]['mappings'][self.doc_type]

    def init_scroll(self):
        return self.es.search(index=self.index, doc_type=self.doc_type, scroll=self.scroll_alive,
                              size=self.size_per_search, sort=['_doc'], body=self.dsl)

    def scroll(self, scroll_id):
        return self.es.scroll(scroll_id=scroll_id, scroll=self.scroll_alive)