from mig_source_es import MigSourceEs
from mig_target_es import MigTargetEs
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor


class MigTask:

    def __init__(self, conf):
        self.source_es = MigSourceEs(conf['source'])
        self.target_es = MigTargetEs(conf['target'])
        self.copy_mapping = conf['copy_mapping']
        self.process_bar = None

    def set_process_bar(self, total):
        self.process_bar = tqdm(total=total)

    def update_process_bar(self, value):
        self.process_bar.update(value)

    def migrate(self):
        if self.copy_mapping:
            source_mapping = self.source_es.get_mapping()
            self.target_es.put_mapping(source_mapping)

        resp = self.source_es.init_scroll()
        self.set_process_bar(resp['hits']['total'])

        with ThreadPoolExecutor(3) as executor:
            continue_scroll, scroll_id = self.bulk_index(executor, resp)
            while continue_scroll:
                resp = self.source_es.scroll(scroll_id)
                continue_scroll, scroll_id = self.bulk_index(executor, resp)
        self.process_bar.clear()

    def bulk_index(self, executor, resp):
        docs = resp['hits']['hits']
        self.target_es.bulk_index(docs, executor, self.update_process_bar)
        return len(docs) > 0, resp['_scroll_id']
