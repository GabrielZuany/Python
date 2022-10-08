import MainPackages.managerbrowser as managerbrowser
import MainPackages.amazonpackage as amazonpackage
import MainPackages.MLpackage as MLpackage

def AmazonScrap(browser, product):
    ProductList = []
    managerbrowser.SubmitSearch(browser, 'amazon')
    managerbrowser.ClickGoogleLink(browser)
    amazonpackage.SearchAmzProduct(browser, product)
    ProductList = amazonpackage.GetAmzProducts(browser)
    amazonpackage.TableToExcel(ProductList)
    
def MLScrap(browser, product):
    ProductList = []
    managerbrowser.SubmitSearch(browser, 'mercado livre')
    managerbrowser.ClickGoogleLink(browser)
    MLpackage.SearchMLProduct(browser, product)
    ProductList = MLpackage.GetMLProducts(browser)
    MLpackage.TableToExcel(ProductList)
    
    
#-----Main------
product = input('What do you want to search? ')

browser = managerbrowser.OpenGoogleWindow(Show=True) 

MLScrap(browser, product)
managerbrowser.DefGoogleUrl(browser)

AmazonScrap(browser, product)
managerbrowser.DefGoogleUrl(browser)

browser.close()