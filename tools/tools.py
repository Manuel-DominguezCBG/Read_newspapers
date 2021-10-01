import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation

from tools.list_of_newspapers import papers

class Read_papers():
    def __init__(self,papers):
        self.papers = papers
        
    def list_url():
        return list(papers().values())
    
    def CleanText(text):
        text = str(text)
        forbidden = [r'\n', r'.', r'?', r'!', r'(', r')']
        for i in forbidden:
            text.replace(i, '')
        return text

    def ReturnCount(url, word):
        r = requests.get(url, allow_redirects=False)
        soup = BeautifulSoup(r.content, 'lxml')
        words = ''.join([t for t in soup.body.find_all(text=True)])
        words = CleanText(words.lower())
        words = words.split()
        return words.count(word.lower())






# # We get the url
# r = requests.get("https://en.wikiquote.org/wiki/Khalil_Gibran")
# soup = BeautifulSoup(r.content)

# # We get the words within paragrphs
# text_p = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
# c_p = Counter((x.rstrip(punctuation).lower() for y in text_p for x in y.split()))

# # We get the words within divs
# text_div = (''.join(s.findAll(text=True))for s in soup.findAll('div'))
# c_div = Counter((x.rstrip(punctuation).lower() for y in text_div for x in y.split()))

# # We sum the two countesr and get a list with words count from most to less common
# total = c_div + c_p
# list_most_common_words = total.most_common() 