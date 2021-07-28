import bs4
import urllib.request as request

prefixUrl = "http://www.novelscape.net/novels/39/39215/" #由於只爬得到下一章html的檔名,所以需要prefix
myURL = "http://www.novelscape.net/novels/39/39215/2580816.html" #第一章的網址

def getWebData(url, i):
    #建立myRequest物件,附加headers訊息
    myRequest = request.Request(url, headers= {
        "cookie" : "over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    })
    with request.urlopen(myRequest) as response: #附帶headers之後去URLopen
        data = response.read().decode("big5","ignore") #request之後讀取並解碼存在data中

    #解析
    root = bs4.BeautifulSoup(data, "html.parser") #解析html
    article = root.find("div", class_ = "contentbox", id = "htmlContent")
    fileName = "chapters/ch_" + str(i) + ".txt"
    with open(fileName, "w", encoding="utf-8") as f:
        f.write(article.text)
    nextChapter = root.find("a", id = "htmlxiazhang")
    return(prefixUrl+nextChapter["href"])


for i in range(1,41): #總共有40章
    myURL = getWebData(myURL,i)
