import json
from mig_task import MigTask

if __name__ == '__main__':
    with open('conf.json') as r:
        conf = json.loads(r.read())
        mig_task = MigTask(conf)
        mig_task.migrate()
