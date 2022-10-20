# How to build a Web Scraping script with spider?
- Start:
~~~~Shell
pip install scrapy
mkdir ProjectName
cd ProjectName
scrapy startproject ProjectName
cd ProjectName/ProjectName/spiders/
scrapy genspider FileName URL
~~~~
---

- Run:
~~~Shell
scrapy runspider -O OutputFileName.extension ./PATH/spiders/PythonMainFileName.py
~~~~

---