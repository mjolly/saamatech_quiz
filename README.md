<p># saamatech_quiz Read the file Python, SQL (Take Home).pdf to understand the questions.</p>

<p>**Python environment setup:** </p>
<p> python3.9 -m venv .venv </p>
<p> source .venv/bin/activate </p>
<p> pip install -r requirements.txt</p>

<p>**Task 1 Solution:** </p>
<p>  The csv file has been trimmed from 1 GB to few KB to be uploaded to github. In test the code works with files  great than 1 GB in size. </p>
<p>  $ python main.py -s 'serious-injury-outcome-indicators-2000-2020-CSV.csv' -t 'chunkloader'</p>

<p>log file output: </p>
<p>  $ cat data_loader.log 2022-04-02 08:50:55,155,155 data_loader INFO file_data : serious-injury-outcome-indicators-2000-2020-CSV.csv 2022-04-02 08:50:55,196,196 data_loader INFO start - main 2022-04-02 08:50:55,196,196 data_loader INFO file_raw : True 2022-04-02 08:50:55,197,197 data_loader INFO start - load_df 2022-04-02 08:50:55,197,197 data_loader INFO self.df iterator: <pandas.io.parsers.TextFileReader object at 0x114b01310> 2022-04-02 08:50:55,204,204 data_loader INFO end - load_df 2022-04-02 08:50:55,204,204 data_loader INFO start - load_db_table 2022-04-02 08:25:06,467,467 data_loader INFO end - load_db_table 2022-04-02 08:25:06,467,467 data_loader INFO end - main</p>

<p>demo_table data snippet: sample data from demo_table using select query: 
  => select * from demo_table limit 5;  index | Series_reference | Period | Type | Data_value | Lower_CI | Upper_CI | Units | Indicator | Cause | Validation | Population | Age | Severity -------+------------------+---------+----------------+------------------+------------------+------------------+----------+-----------+---------+------------+------------+----------+----------  
  0 | W_A11 | 2000-02 | Moving average | 59.6666666666666 | 50.9258230199682 | 68.407510313365 | Injuries | Number | Assault | Validated | Whole pop | All ages | Fatal  1 | W_A11 | 2001-03 | Moving average | 60 | 51.2347745942341 | 68.7652254057658 | Injuries | Number | Assault | Validated | Whole pop | All ages | Fatal  2 | W_A11 | 2002-04 | Moving average | 59 | 50.308125050352 | 67.6918749496479 | Injuries | Number | Assault | Validated | Whole pop | All ages | Fatal  3 | W_A11 | 2003-05 | Moving average | 59 | 50.308125050352 | 67.6918749496479 | Injuries | Number | Assault | Validated | Whole pop | All ages | Fatal  4 | W_A11 | 2004-06 | Moving average | 61.3333333333333 | 52.4712516678722 | 70.1954149987944 | Injuries | Number | Assault | Validated | Whole pop | All ages | Fatal (5 rows)</p>

<p>=> select count(*) from demo_table ;  </p>
<p>  count ---------  5886216 (1 row)</p>

<p>**Task 2 Solution:** </p>
<p> Log file has the result in the list result_list. The csv file records.csv has the input strings.</p>

<p>$ python main.py -s 'records.csv' -t 'recordmerger'</p>

<p>log file output: </p>
 <p> $ cat record_merger.log 
  2022-04-02 09:23:35,869,869 record_merger INFO file_data : records.csv 2022-04-02 09:23:35,869,869 record_merger INFO start-main 2022-04-02 09:23:35,870,870 record_merger INFO start-csvtolist 2022-04-02 09:23:35,870,870 record_merger INFO self.data:['Equipment ONLY - Saama Technologies', 'Saama Technologies', 'SaamaTech', 'Takeda Pharmaceutical SA - Central Office', '*** DO NOT USE *** Takeda Pharmaceutical', 'Takeda Pharmaceutical', 'Ship to AstraZeneca', 'AstraZeneca', 'AstraZeneca (use AstraZeneca'] 2022-04-02 09:23:35,870,870 record_merger INFO end-csvtolist 2022-04-02 09:23:35,870,870 record_merger INFO start-parselist 2022-04-02 09:23:35,873,873 record_merger INFO result_list : ['Saama Technologies', 'SaamaTech', 'Takeda Pharmaceutical', 'AstraZeneca'] 2022-04-02 09:23:35,873,873 record_merger INFO end-parselist 2022-04-02 09:23:35,873,873 record_merger INFO end-main</p>

<p>**SQL Solution:** </p>
<p>  The sql solution has been provided with solutions in the file sql_solution.txt. </p>
<p>  PostgreSQL database was used for the test. </p>
<p>  Note: The question 4 from sql questions is unanswered as I did not understand the question. </p>
<p>  Please use https://sqliteonline.com/ to copy paste the solutions and test them.</p>
