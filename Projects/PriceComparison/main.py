import managerbrowser
import amazonpackage
import MLpackage

def AmazonScrap(browser):
    ProductList = []
    managerbrowser.SubmitSearch(browser, 'amazon')
    managerbrowser.ClickGoogleLink(browser)
    amazonpackage.SearchAmzProduct(browser)
    ProductList = amazonpackage.GetAmzProducts(browser)
    amazonpackage.TableToExcel(ProductList)
    
def MLScrap(browser):
    managerbrowser.SubmitSearch(browser, 'mercado livre')
    managerbrowser.ClickGoogleLink(browser)
    MLpackage.FindMLProd(browser)
    MLpackage.WriteMLProd(browser)
    return

browser = managerbrowser.OpenGoogleWindow(Show=True) 
MLScrap(browser)
managerbrowser.DefGoogleUrl(browser)

AmazonScrap(browser)
managerbrowser.DefGoogleUrl(browser)


browser.close()