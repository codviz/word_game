analysis_words_file = open(r"data/changemeanings_emotion.csv","r")
analysis_words_dictionary = {}

while True:
    line = analysis_words_file.readline()
    if line:
        line_list = line.split(',')
        line_list.pop(0)
        while 'NA' in line_list: line_list.remove('NA')
        while "NA\n" in line_list: line_list.remove('NA\n')
        analysis_words_dictionary[line_list[0]] = line_list[1:]
    else:
        break

analysis_words_file.close()
keys = list(analysis_words_dictionary.keys())

last_year_file = open(r"data/timeTraveler.csv","r")
last_year_list = []

while True:
    line = last_year_file.readline()
    if line:
        line_list = line.split(',')
        last_year_list.append(line_list[0])
    else:
        break

count = 0
for word in last_year_list:
    if word in keys:
        count += 1

print(count)






