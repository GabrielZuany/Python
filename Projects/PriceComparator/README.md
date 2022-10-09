# Price Comparator using Web Scraping with Python
## The reason behind the project:
 Automate the search, table and manipulate several information from different databases with specific structure.
 In this case, the database was a lot of commercial websites in witch each of them have their own builded HTML and CSS differently to the others.
 This project came when a realize the time and effort to collect all information manually, not easy and inefficient by the time overview. So, the idea was automate
 this process.
 
## How it works?
  Basically it works by automating the internet browsing using:
  1. **Selenium** and **Webdriver** to open browser and click or submit.
  2. **BeautifulSoup** to get html page, after establish a stable connection (Response ~200).
  3. **Pandas** and **Matplotlib** to analyze and build plot with the collected data.
  
  When the connection is stable, the script pulls the HTML page content. Once I have the HTML, I can look for elements that I'm interested to collect about the
  current page and store it into a _list_.<br>
  Using _**Selenium**_ to go through the websites pages, and _**bs4**_ to extract all data that I want to, the automating system is almost
  100% concluded.<br>
  When my product list is finished, I start to build plots (histograms) -_**Matplotlib**_- to analyse the collected data.<br>
  Then, I read the price column into dataframe (_**Pandas**_) and start to manipulate it to obtain important values like mean, median and (future) other info.<br><br>
  At the end, I will have .xlsx files with all product information (Name, price, link...) and two statistical graph to interpret the data.<br>
  
## Histograms:
  <br><br>
  <img src="https://github.com/GabrielZuany/Python/blob/master/Projects/PriceComparator/ExtractedData/JoinedPlots.png" width="500" height="400" />
  <img src="https://github.com/GabrielZuany/Python/blob/master/Projects/PriceComparator/ExtractedData/SeparatedPlots.png" width="500" height="400" />
  <br><br>
  
## XLSX files:
<br><br>
  <img src="https://github.com/GabrielZuany/Python/blob/master/Projects/PriceComparator/img/AmzScreenShot.png" width="500" height="400" />
  <img src="https://github.com/GabrielZuany/Python/blob/master/Projects/PriceComparator/img/ML_ScreenShot.png" width="500" height="400" />
  <br><br>
  
## Last Updates:
  - Remove the R script and replace it to a builded python module (reason: make the full process 100% autonomous step by step. No need to execute another script).<br>
  - Build two different histograms:<br>
    1. Superimposed histograms (JoinedPlot.png), with mean and median;<br>
    2. Histograms side by side (SeparatedPlot.png).<br>
  - Product to be search set dynamically by user.<br>
  - Comment the full code using docstring.

## Additional Information:
  - Author: Gabriel Zuany Duarte Vargas. (ES, Brazil)<br>
  - Date: 09/10/2022 (_last update_)<br>
  - **Please, feel free to suggest improvements and new features!**<br>
  - You can contact me in _gabrielzuanyduartevargas@gmail.com_.<br>
