import logging
import os
import gc
from logging.handlers import TimedRotatingFileHandler
import warnings
import sys
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

formatter = logging.Formatter('%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')

handler = TimedRotatingFileHandler('data_loader.log',
                                   when='midnight',
                                   backupCount=10)
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

class ChunkLoader(object):
    def __init__(self,file_data=None):
        logger.info("file_data : %s",file_data)
        self.file_data = file_data
        self.df = None
        database_uri = "postgresql://username:pwd@ip_addr:port/db_name"
        self.engine=create_engine(database_uri ,pool_size=20, max_overflow=-1)

    def read_dataset(self):
        if (self.file_data.startswith('http://')):
            try:
                urllib2.urlopen(self.file_data)
            except urllib2.HTTPError as e:
                logger.info("error:%s",e.code)
            except urllib2.URLError as e:
                logger.info("error:%s",e.args)
        else:
            try:
                file_raw = os.path.exists(self.file_data)
                logger.info("file_raw : %s",file_raw)
            except OSError:
                logger.info("File Data Error: %s",ex)

    def load_df(self):
        logger.info("start - load_df")
        if self.file_data:
            self.df = pd.read_csv(self.file_data, chunksize=1000,encoding='iso-8859-1')
        logger.info("self.df iterator: %s",self.df)
        logger.info("end - load_df")

    def load_db_table(self):
        logger.info("start - load_db_table")
        for data in self.df:
            data.to_sql('demo_table', con=self.engine, schema='public',if_exists='append',chunksize=1000, method='multi')
        if self.df:
            del self.df
            gc.collect()
        logger.info("end - load_db_table")
                
    def main(self):
        logger.info("start - main")
        self.read_dataset()
        self.load_df()
        self.load_db_table()
        logger.info("end - main")
        
