from datetime import datetime
import re
from langdetect import detect

file = "ratebeer.txt"

beer_poz = [11, 13, 15, 10, 12, 19, 14, 15, 14, 16, 13, 20, 13]  # od którego indeksu kopiujemy tekst
beerVal = []  # lista do magazynowania jednej recenzji
beerID = []  # lista gdzie wrzucamy wszystkie BeerID

newfile = "ratebeer_new.json"  # nazwa pliku do którego zapisujemy dane zamienione na JSON
newBeerIDfile = "beerID.txt"  # nazwa pliku do którego zapisujemy BeerID
output = open(newfile, 'w')
output2 = open(newBeerIDfile, 'w')

start_time = datetime.now()


with open(file, "r", encoding="utf-8", errors='ignore') as rb_raw:
    #output.write("[\n")
    i = 0
    a = 0
    b = 1  # numer ID ktory dodajemy do każdej recenzji
    for line in rb_raw:

        #zamiana na nawiasy
        line = line.replace('&#40;', '(')
        line = line.replace('&#41;', ')')
        line = line.replace('&quot;', '')

        if i == 13:  # jedna pełna recenzja ma 13 wierszy i 14 jest pusty, kiedy dojdziemy do 14 zapisujemy do pliku i zerujemy indeks
            # print(beerVal)

            text12 = beerVal[12]
            newText12 = text12.replace('"', '\\"')

            # usuniecie białych znaków i innych śmieci z którymi json ma problem z recenzji
            #newText12 = re.sub('[^A-Za-z0-9.?!,$%\(\)-]+', ' ', newText12)
            newText12 = re.sub('[^A-Za-z0-9.?!,$%-]+', ' ', newText12)

            try:
                if len(newText12) < 5 or len(newText12) == None:
                    lang = "null"
                elif len(newText12) > 5:
                    lang = detect(newText12)
            except:
                lang = "null"


            # zamiana na Null
            if beerVal[3] == '-':
                beerVal[3] = 'null'

            # zamiania ocen w postaci stringow (np. 5/20) o różnym mianowniku na ogólnoą wartość procentową
            x, y = beerVal[5].split("/")
            appearance_val = int(x) / int(y)
            beerVal[5] = str(appearance_val)

            x, y = beerVal[6].split("/")
            aroma_val = int(x) / int(y)
            beerVal[6] = str(aroma_val)

            x, y = beerVal[7].split("/")
            palate_val = int(x) / int(y)
            beerVal[7] = str(palate_val)

            x, y = beerVal[8].split("/")
            taste_val = int(x) / int(y)
            beerVal[8] = str(taste_val)

            x, y = beerVal[9].split("/")
            overall_val = int(x) / int(y)
            beerVal[9] = str(overall_val)

            if b != 1:
                JSONline = '\n{"reviewID":' + str(b) + ', "beer_name":' + '"' + beerVal[0] + '"' + ', "beerId":' + beerVal[1] + ', "brewerId":' + \
                           beerVal[2] + \
                           ', "ABV":' + beerVal[3] + ', "style":"' + beerVal[4] + '", "appearance":' + \
                           beerVal[5] + ', "aroma": ' + beerVal[6] + ', "palate":' + beerVal[7] + ', "taste":' + \
                           beerVal[8] + \
                           ', "overall":' + beerVal[9] + ', "time":"' + beerVal[10] + '", "profileName":"' + beerVal[
                               11] + \
                           '", "text":"' + newText12 + '", "lang":"' + lang + '"}'
            else:
                JSONline = '{"reviewID":' + str(b) + ', "beer_name":' + '"' + beerVal[0] + '"' + ', "beerId":' + beerVal[1] + ', "brewerId":' + \
                           beerVal[2] + \
                           ', "ABV":' + beerVal[3] + ', "style":"' + beerVal[4] + '", "appearance":' + \
                           beerVal[5] + ', "aroma": ' + beerVal[6] + ', "palate":' + beerVal[7] + ', "taste":' + \
                           beerVal[8] + \
                           ', "overall":' + beerVal[9] + ', "time":"' + beerVal[10] + '", "profileName":"' + beerVal[
                               11] + \
                           '", "text":"' + newText12 + '", "lang":"' + lang + '"}'

            beerID.append(beerVal[1] + "\n")
            output.write(JSONline)
            beerVal = []
            i = 0
            a = 0
            print("reviewID = " + str(b))
            b += 1
        else:
            beerVal.append(line[beer_poz[a]:-1])  # towrzy listę wartości z recenzji, usuwa opisy
            # print(line[beer_poz[a]:])
            i += 1
            a += 1
print(len(beerID))
beerID = list(set(beerID))  # usunięcie duplikatów
print(len(beerID))
for poz in beerID:
    output2.write(poz)

#output.write("]")
output.close()
output2.close()

end_time = datetime.now()
delta_time = end_time - start_time
print(delta_time)
