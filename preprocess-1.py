import re
import nltk
nltk.download('stopwords')
try:
  with open(r"D:\Fake-news-detection\jupyter_project\fake_or_real_news_test.csv",'r',encoding='utf-8') as input_str:
    noNewLines = re.sub("\n", "", input_str.read())
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e)
# re-add new line at end of each row
noNewLines = re.sub("title,text", "title,text\n", noNewLines)
  

noNewLines = re.sub(",FAKE", ",FAKE\n", noNewLines)
# noNewLines = re.sub(",FAKE,(?!,)",",FAKE,,\n",noNewLines)
# noNewLines = re.sub(",FAKE,,(?!,)",",FAKE,,\n",noNewLines)
  
noNewLines = re.sub(",REAL", ",REAL\n", noNewLines)
# noNewLines = re.sub(",REAL,(?!,)",",REAL,,\n",noNewLines)
# noNewLines = re.sub(",REAL,,(?!,)",",REAL,,\n",noNewLines)
  

# Replace any commas between two quotes with |
lines = noNewLines.split('\n')

def removeComma(g):
  t = g.groups()
  t = [t[0], t[1].replace(',', ' |'), t[2], t[3]]
  return "".join(t)

betweenQuotes = lambda line: re.sub(r'(.*,")(.*)(",)(.*)', lambda x: removeComma(x), line)

secondCol = lambda line: re.sub(r'^([0-9]+,)(.*,.*)(,\")(.*)$', lambda x: removeComma(x), line, 1)


lines = [betweenQuotes(l) for l in lines]
lines = [secondCol(l) for l in lines]

finalString = '\n'.join(lines)

try:
  with open(r'D:\Fake-news-detection\jupyter_project\fake_or_real_news_test_CLEANED.csv', 'w',encoding='utf-8') as file:
    file.write(finalString)
except UnicodeEncodeError as e:
    print("UnicodeEncodeError:", e)
file.close()
