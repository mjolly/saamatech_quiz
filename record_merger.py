from difflib import SequenceMatcher
import itertools
import csv
import logging
import os
from logging.handlers import TimedRotatingFileHandler
import warnings
import sys
warnings.simplefilter(action='ignore', category=FutureWarning)


formatter = logging.Formatter('%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s')

handler = TimedRotatingFileHandler('record_merger.log',
                                   when='midnight',
                                   backupCount=10)
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

class RecordMerger(object):
    def __init__(self, file_data):
        logger.info("file_data : %s",file_data)
        self.file_data = file_data
        self.data = None

    def matcher(self, text_1, text_2):
        return SequenceMatcher(None, text_1, text_2).ratio()

    def csvtolist(self):
        logger.info("start-csvtolist")
        if self.file_data:
            self.data = []
            with open(self.file_data, newline='') as f:
                for row in csv.reader(f):
                    self.data.append(row[0])
        logger.info("self.data:%s",self.data)
        logger.info("end-csvtolist")

    def parselist(self):
        logger.info("start-parselist")
        result_list = []
        if self.data:
            for i in range(len(self.data)):
                holder_list = []
                for j in range(i + 1, len(self.data)):
                    ratio_result = self.matcher(str(self.data[i]), str(self.data[j]))
                    if ratio_result > 0.5:
                        holder_list.append(str(self.data[i]))
                        holder_list.append(str(self.data[j]))
                    #logger.info("holder_list : %s",holder_list)
                shortest_result = min(holder_list, key=len, default="EMPTY")
                result_list.append(shortest_result)
        result_list = list(dict.fromkeys(result_list))
        result_list.remove('EMPTY')
        logger.info("result_list : %s",result_list)
        logger.info("end-parselist")
                    

    def main(self):
        logger.info("start-main")
        self.csvtolist()
        self.parselist()
        logger.info("end-main")
