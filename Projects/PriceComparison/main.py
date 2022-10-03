import managerbrowser
import amazonpackage
import MLpackage

def AmazonScrap(browser):
    managerbrowser.SubmitSearch(browser, 'amazon')
    managerbrowser.ClickGoogleLink(browser)
    amazonpackage.FindAmzProducts(browser)
    amazonpackage.WriteAmzProducts(browser)
    
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
