import MainPackages.managerbrowser as managerbrowser
import MainPackages.amazonpackage as amazonpackage
import MainPackages.MLpackage as MLpackage

def AmazonScrap(browser):
    ProductList = []
    managerbrowser.SubmitSearch(browser, 'amazon')
    managerbrowser.ClickGoogleLink(browser)
    amazonpackage.SearchAmzProduct(browser)
    ProductList = amazonpackage.GetAmzProducts(browser)
    amazonpackage.TableToExcel(ProductList)
    
def MLScrap(browser):
    ProductList = []
    managerbrowser.SubmitSearch(browser, 'mercado livre')
    managerbrowser.ClickGoogleLink(browser)
    MLpackage.SearchMLProduct(browser)
    ProductList = MLpackage.GetMLProducts(browser)
    MLpackage.TableToExcel(ProductList)
    
    
#-----Main------
browser = managerbrowser.OpenGoogleWindow(Show=True) 
MLScrap(browser)
managerbrowser.DefGoogleUrl(browser)

AmazonScrap(browser)
managerbrowser.DefGoogleUrl(browser)

browser.close()