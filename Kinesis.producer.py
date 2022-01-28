import json
import boto3
import random
from datetime import datetime

kinesis = boto3.client('kinesis')
sname = "mgtest-stream"

#stream = kinesis.create_stream(StreamName=sname, ShardCount=3)
print(kinesis.describe_stream(StreamName=sname))
print(kinesis.list_streams())
start_time = datetime.now()

"""
with open("ratebeer1p.json", "r") as rbj:
    for line in rbj:
        aa = random.randint(10, 50)
        print(line)
        kinesis.put_record(StreamName=sname, Data=line, PartitionKey=str(hash(aa)))
"""



with open("ratebeer1p.json", "r") as rbj:
    i = 0
    b = 1
    records = []
    for line in rbj:
        aa = random.randint(10, 50)
        record = {'Data': line,'PartitionKey': str(hash(aa))}
        records.append(record)
        # if i == 100:
        #     kinesis.put_records(Records=records, StreamName=sname)
        #     print(records)
        #     records = []
        #     print(str(b) + " rekordów wysłano!")
        #     i = 0
        # else:
        #     i += 1
        kinesis.put_records(Records=records, StreamName=sname)
        print(records)
        records = []
        print(str(b) + " rekordów wysłano!")
        b += 1

end_time = datetime.now()
delta_time = end_time - start_time
print(delta_time)

#klasyfikator do AWS glue:
#$[*]