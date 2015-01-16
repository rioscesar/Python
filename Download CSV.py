from urllib import request

def download_csv(url):
    response = request.urlopen(url)
    cvs = response.read()
    cvs = str(cvs)
    lines = cvs.split("\\n")
    file = r"goog.csv"
    f = open(file, "w")
    for line in lines:
        f.write(line + "\n")
    f.close()

goog_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=0&e=1&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv"

download_csv(goog_url)
