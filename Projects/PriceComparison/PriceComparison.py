import amazonpackage
import managerbrowser

def AmazonScrap(browser):
    managerbrowser.SubmitSearch(browser, 'amazon')
    managerbrowser.ClickGoogleLink(browser)
    amazonpackage.FindAmzProducts(browser)
    amazonpackage.WriteAmzProducts(browser)
    
def MLScrap(browser):
    return
    
def AmericanasScrap(browser):
    return

browser = managerbrowser.OpenGoogleWindow(Show=True) 
AmazonScrap(browser)
managerbrowser.DefGoogleUrl(browser)

MLScrap(browser)
managerbrowser.DefGoogleUrl(browser)

AmericanasScrap(browser)
managerbrowser.DefGoogleUrl(browser)

browser.close()
