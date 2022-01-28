import boto3
import time

kinesis = boto3.client('kinesis')

shard_id = 'shardId-000000000000' #we only have one shard!
shard_it = kinesis.get_shard_iterator(StreamName="BotoDemo", ShardId=shard_id, ShardIteratorType="LATEST")["ShardIterator"]
while 1==1:
    out = kinesis.get_records(ShardIterator=shard_it, Limit=2)
    shard_it = out["NextShardIterator"]
    print(out)
    time.sleep(0.2)

