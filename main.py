import datetime
#from pprint import pprint
import sys
from optparse import OptionParser
from datetime import timedelta
from data_loader import ChunkLoader
from record_merger import RecordMerger


def main():
    """
    python main method acts as the method that accepts the arguments from console,
    create objects of various classes,
    validations variables,
    calls the methods from other classes for the domain logic invocation.
    The two other classes are ChunkLoader, RecordMerger
    ChunkLoader uses dataframe iterator to read files in chunk and load them in db table
    RecordMerger parses a csv file into list and then reduces it to unique strings in a result_list
    """

    usage = "usage: %prog [options] -s file_name_path -t task_name(chunkloader or recordmerger)"
    parser = OptionParser(usage=usage)

    parser.add_option('-s', '--file_name_path',
                      action='store',
                      type='string',
                      dest='file_name_path',
                      default=None
                      )
    parser.add_option('-t', '--task_name',
                      action='store',
                      type='string',
                      dest='task_name',
                      default=None
                      )

    (opts, args) = parser.parse_args()
    if None in (opts.file_name_path, opts.task_name):
        print("Both arguments for file_name and task_name are required")
        sys.exit(1)
    
    if opts.task_name == "chunkloader":
        loader = ChunkLoader(opts.file_name_path)
        loader.main()
    elif opts.task_name == "recordmerger":
        merger = RecordMerger(opts.file_name_path) 
        merger.main()

if __name__ == '__main__':
    main()


