#!/usr/bin/python
import json
import sys

def reduce(lines):
    lastKey = None
    sum = 0
    for line in lines:
        data = json.loads(line)
        key = data["word"]
        value = data["count"]

        if key != lastKey and lastKey is not None:
            txtDlaReduktora = '{"beerId":' + str(data["beerId"]) + ', "word":"'
            txtDlaReduktora = txtDlaReduktora + lastKey + '", "count":' + str(sum) + '}'
            print(txtDlaReduktora)
            sum = 0

        sum += int(value)
        lastKey = key

if __name__ == "__main__":
   reduce(sys.stdin)

#hadoop fs -copyToLocal [s3://bucket/plik] .
#hdfs dfs -mkdir [gdzie i jaki folder stowzyc]
#hdfs dfs -put [plik] [gdzie]
#hadoop fs -getmerge [sciezka folderu na hdfs gdzie sa nasze pliki wynikowe w czesciach] [adres i nazwa nowego polaczonego pliku z wynikami na hadoopie]

#nano map.py
#nano reduce.py
#chmod 777 map.py
#chmod 777 reduce.py
#hadoop-streaming -input /user/m/data -output /m/results/1 -mapper ./map.py -reducer ./reduce.py -file ./reduce.py -file ./map.py
#yarn logs -applicationId application_1621284709670_0002 -log_files stderr


#przyklady:
#hadoop fs -copyToLocal s3://moje-wiaderko/data/ratebeer2.json .
#hdfs dfs -put ratebeer2.json /tmp/m
