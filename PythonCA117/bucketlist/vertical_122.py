import sys

#read stdin data to list of list of chars
data = []
for line in sys.stdin:
  data.append([char for char in line.rstrip('\n')])

#read the data column wise as is supposed to be
corr_words = []
corr_str = ''
for i in range(len(data[0])):
    for j in range(len(data)):
        corr_str += data[j][i]
    corr_words.append(corr_str)
    corr_str = ''

#sort the words
sorted_words = sorted(corr_words, key=str.lower)

#create a list of chars for every word
sorted_word_list = []
for word in sorted_words:
    sorted_word_list.append([char for char in word])

#save the words columnwise and add them to final list
final_words = []
for i in range(len(sorted_word_list[0])):
    word = ''
    for j in range(len(sorted_word_list)):
        word += sorted_word_list[j][i]
    final_words.append(word)

#print out final list
for word in final_words:
    print(word)
