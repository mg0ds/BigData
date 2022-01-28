#!/usr/bin/python
import re
import sys
import json
#from langdetect import detect


stop_word = {"yet", "y", "without", "l", "flavor", "head", "aroma", "bottle", "nice", "beer", "pours", "body",
             "good", "oz", "like", "almost", "color", "finish", "ale", "one", "much", "thanks", "taste", "notes",
             "nose", "bit", "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
             "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
             "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
             "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
             "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until",
             "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during",
             "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
             "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all",
             "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only",
             "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"}

def map(lines):

    for line in lines:
        if line != "\n" or line != "":
            data = json.loads(line)
            #lang = detect(data["text"])
            #lang = "en"
            words = re.findall("[a-zA-Z]+", data["text"])

            for word in words:
                if word.lower() not in stop_word:
                    txtDlaReduktora = '{"beerId":' + str(data["beerId"]) + ', "word":"'
                    txtDlaReduktora = txtDlaReduktora + word.lower() + '", "count":1}'
                    #ewentualnie jak mozna tylko jeden kay i jedno value przesylac:
                    #txtDlaReduktora = str(data["beerId"]) + "@" + word.lower() + "/t" + "1"
                    print(txtDlaReduktora)

if __name__ == "__main__":
    map(sys.stdin)



#(?="text\":\").*(?=\.\"\})
#data = re.findall("text\":\"(.*?)\.\"\}", line)

#echo ‘{"beer name":"John Harvards Belgian Tripel", "beerId":71715, "brewerId":8481, "ABV":8.5, "style":"Abbey Tripel", "appearance":0.8, "aroma": 0.4, "palate":0.4, "taste":0.5, "overall":0.55, "time":"2000-05-19", "profileName":"PhillyBeer2112", "text":"UPDATED FEB 19, 2003 Springfield, PA. Sharp and cloyingly sweet. The alcohol presence becomes more and more noticeable."}’ | ./map.py

