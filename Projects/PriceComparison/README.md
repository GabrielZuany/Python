# Price Comparasion with Web Scraping and R
## The reason behind the project:
 Automate the search, table and manipulate several informations from different databases with specific struct.
 In this case, the database was a lot of webstores in witch each of them have their own builded HTML and CSS differently to the others.
 This project came when a realize the time and effort to collect all informations manually, not easy and inefficient by the time overview. So, the idea was automate
 this process.
 
## How it works?
  Basically it works by automating the internet browsing using:
  1. **Selenium** and **Webdriver** to open browser and click or submit.
  2. **BeautifulSoup** to get html page, after establish a stable connection (Response ~200).
  3. **R Script** to analyze the collected data.
  
  When the connections is stable, the script pulls the HTML page content. Once I have the HTML, I can look for elements that I'm intrested to collect about the
  current page and store it in a _list_.<br>
  Using _**Selenium**_ to go through the pages of webstore (and webstores), and _**bs4**_ I can extract all data that I want to, the automating system is almost
  100% conclued.<br>
  With my product list finished, I convert it to .xlsx file and export to _**R script**_ to analyze the data.<br>
  With **R**, I load the .xlsx file and read the price column. After store in a data frame I unlist and convert to numeric value. Then start to compare the data extracted
  by each webstore and build a plot to do statistical analysis.<br><br>
  At the end, I will have .xlsx files with all product informations (Name, price, link...) and statistical graph to interpret the data.
  
## Additional Information:
  -Author: Gabriel Zuany Duarte Vargas. (ES, Brazil)<br>
  -Date: 06/10/2022 (_last update_)<br>
  -**Please, feel free to suggest improvements and new features!**<br>
  -You can contact me in _gabrielzuanyduartevargas@gmail.com_.<br>
  ;)
