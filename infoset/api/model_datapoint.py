import sys
from ast import literal_eval
from infoset.db.db_orm import BASE
from sqlalchemy import Column, ForeignKey, Integer, String, text
from sqlalchemy.dialects.sqlite import DATETIME
sys.path.append("~/Work/infoset-ng/infoset")

class Datapoint(BASE):
    """Class defining the iset_datapoint table of the database."""

    __tablename__ = 'iset_datapoint'
   

    idx_datapoint = Column(
        Integer, primary_key=True,
        autoincrement=True)

    idx_deviceagent = Column(
        Integer, ForeignKey('iset_deviceagent.idx_deviceagent'),
        server_default='1')

    idx_department = Column(
        Integer, ForeignKey('iset_department.idx_department'),
        server_default='1')

    idx_billcode = Column(
        Integer, ForeignKey('iset_billcode.idx_billcode'),
        server_default='1')

    id_datapoint = Column(
        Integer, unique=True, nullable=True, default=None)

    agent_label = Column(Integer, nullable=True, default=None)

    agent_source = Column(Integer, nullable=True, default=None)

    enabled = Column(Integer, server_default='1')

    billable = Column(Integer, server_default='0')

    timefixed_value = Column(Integer, nullable=True, default=None)

    base_type = Column(Integer, server_default='1')

    last_timestamp = Column(
        Integer, nullable=False, server_default='0')

    ts_modified = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))

    ts_created = Column(
        DATETIME, server_default=text('CURRENT_TIMESTAMP'))
