import pymysql
import paramiko
import json
from sshtunnel import SSHTunnelForwarder

pkeyfilepath = "klucz.pem"
mypkey = paramiko.RSAKey.from_private_key_file(pkeyfilepath)

sql_hostname = '127.0.0.1'
sql_username = 'root'
sql_password = 'moje-tajne-haslo'
sql_main_database = 'rb'
sql_port = 3306
ssh_host = 'ec2-3-43-223-124.compute-1.amazonaws.com'
ssh_user = 'ubuntu'
ssh_port = 22
sql_ip = '127.0.0.1'

with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_pkey=mypkey,
        remote_bind_address=(sql_hostname, sql_port),
        local_bind_address =('127.0.0.1', sql_port)) as tunnel:
    conn = pymysql.connect(host='127.0.0.1', user=sql_username,
            passwd=sql_password, db=sql_main_database,
            port=tunnel.local_bind_port)
    if conn.open:
        print("Połącznie udane!")
    item_count = 0
    with conn.cursor() as cur:
        plik = "ratebeer1p.json"
        # cur.execute("create table rb_test (id int, reviewid int, beer_name varchar(255), beerid int, brewerid int,"
        #             "abv varchar(255), style varchar(255), appearance double, aroma double, palate double, taste double,"
        #             "overall double, time varchar(255), profilename varchar(255), text text, lang varchar(255))")
        with open(plik, "r", encoding="utf-8", errors='ignore') as rb1p:
            for line in rb1p:
                json_line = json.loads(line)
                #print(json_line["reviewID"])
                querry = 'insert into rb (id, reviewid , beer_name, beerid , brewerid, abv, style, appearance,' \
                         'aroma, palate, taste, overall, time, profilename, text, lang) values(NULL, {}, "{}", {}, {},' \
                         '"{}", "{}", {}, {}, {}, {}, {}, "{}", "{}", "{}", "{}")'.format(json_line["reviewID"],
                                                                                          json_line["beer_name"],
                                                                                          json_line["beerId"],
                                                                                          json_line["brewerId"],
                                                                                          json_line["ABV"],
                                                                                          json_line["style"],
                                                                                          json_line["appearance"],
                                                                                          json_line["aroma"],
                                                                                          json_line["palate"],
                                                                                          json_line["taste"],
                                                                                          json_line["overall"],
                                                                                          json_line["time"],
                                                                                          json_line["profileName"],
                                                                                          json_line["text"],
                                                                                          json_line["lang"])
                #print(querry)
                cur.execute(querry)
                item_count += 1
            conn.commit()
            print("Added %d items to MySQL table" % (item_count))
    conn.close()
