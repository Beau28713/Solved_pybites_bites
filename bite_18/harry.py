import os
import urllib.request
import string
import collections

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)


def get_harry_most_common_word():
    punct = string.punctuation
    stop_list = collections.deque()

    with open(stopwords_file, 'r') as file_1, open(harry_text,'r', encoding='utf8') as file_2:
        for line in file_1:
            stop_list.append(line.strip())

        x = file_2.read()

        x = x.translate(str.maketrans('', '', punct))

        harry_list = x.lower().split()
    
    
    result = [i for i in harry_list if i not in stop_list]

    return collections.Counter(result).most_common(1)[0]