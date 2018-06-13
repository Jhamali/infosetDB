from ast import literal_eval
from model_datapoint import Datapoint
from infoset.db.db_orm import BASE
import logging
import sys


# Load logging configuration
log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    log.info('Create dataBASE {}'.format(BASE.db_name))
    BASE.BASE.metadata.create_all(BASE.engine)

    log.info('Insert datpoints in dataBASE')
    with open('dataponts.json', 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            point = Datapoint(**record)
            BASE.db_session.add(point)
        BASE.db_session.commit()

   