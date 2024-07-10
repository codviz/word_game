def create_dict():
  
    most_used_file = open(r"data/most_used_words.txt","r")
    most_used_content = most_used_file.read()
    most_used_list = most_used_content.split()

    analysis_words_file = open(r"data/changemeanings_emotion.csv","r")
    analysis_words_dictionary = {}
    analysis_words_file.readline()
    
    while True:
        line = analysis_words_file.readline()
        if line:
            line_list = line.split(',')
            line_list.pop(0)
            while 'NA' in line_list: line_list.remove('NA')
            while "NA\n" in line_list: line_list.remove('NA\n')
            if int(line_list[2]) > 2:
                if line_list[0] in most_used_list:
                    analysis_words_dictionary[line_list[0]] = line_list[1:]
        else:
            break

    most_used_file.close()
    analysis_words_file.close()
    
    return analysis_words_dictionary


####Broken, working on fixing currently
def check_years(line_list):
    start_pos = int(line_list[2]) + 3
    unique_values = 1
    for i in range(int(line_list[2]) - 1):
        if int(line_list[start_pos + 1]) != int(line_list[start_pos]):
            start_pos += 1
            unique_values += 1
    if unique_values >= 3:
        return True
    else:
        return False
