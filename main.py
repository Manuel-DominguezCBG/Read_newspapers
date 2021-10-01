from tools.tools import Read_papers
from tools.list_of_newspapers import *


papers = Read_papers.list_url()

print(papers[0])

Read_papers.ReturnCount(papers[0], "word")
#Read_papers.ReturnCount(papers,"wordJJ")
# print(Read_papers())