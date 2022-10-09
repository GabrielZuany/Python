import MainPackages.managerbrowser as managerbrowser
import MainPackages.amazonpackage as amazonpackage
import MainPackages.dataAnalysis as dataAnalysis
import MainPackages.MLpackage as MLpackage

def AmazonScrap(browser, product):
    """
    Controls the main commands to make web scraping in Amazon website.

    Args:
        browser (webdriver): chromedriver.
        product (str): product to be searched.

    Returns:
        DataFrame: dataframe with name, price and link of all products found.
    """
    ProductList = []
    managerbrowser.SubmitSearch(browser, 'amazon')
    managerbrowser.ClickGoogleLink(browser)
    amazonpackage.SearchAmzProduct(browser, product)
    ProductList = amazonpackage.GetAmzProducts(browser)
    df = amazonpackage.TableToExcel(ProductList) # build a .xlsx file from a list and returns the match DataFrame.
    price_column = df['AMZ Price (R$)']
    dataAnalysis.BuildJoinedPlot(price_column, 'AMZ', 'c', 'b', 'g', 'purple')
    return df
    
    
    
def MLScrap(browser, product):
    """
    Controls the main commands to make web scraping in Mercado Livre website.

    Args:
        browser (webdriver): chromedriver.
        product (str): product to be searched.

    Returns:
        DataFrame: dataframe with name, price and link of all products found.
    """
    ProductList = []
    managerbrowser.SubmitSearch(browser, 'mercado livre')
    managerbrowser.ClickGoogleLink(browser)
    MLpackage.SearchMLProduct(browser, product)
    ProductList = MLpackage.GetMLProducts(browser)
    df = MLpackage.TableToExcel(ProductList) # build a .xlsx file from a list and returns the match DataFrame.
    price_column = df['ML Price (R$)']
    dataAnalysis.BuildJoinedPlot(price_column, 'ML', 'r', 'y', '#444444', 'black')
    return df


    """
    Created by: Gabriel Zuany Duarte Vargas.
    Date: 08/10/2022 (Last update).
    Protected by GNU V3.0.
    
    Copyright (C) <2022>  <Gabriel Zuany Duarte Varga>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.   
    """
