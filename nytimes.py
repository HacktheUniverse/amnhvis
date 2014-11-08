import time

nytimes_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?page=1&&fq=section_name:("+"\"U.S.\""+")&begin_date=%s&end_date=%s&api-key"
nytimes_key = "SECRET"

outfile = open("headlines.csv", "w")

for year in range(1982,2013):
    for month in range(1,12):
        
        start_date = "%d%02d%02d" % (year,month,1)
        end_date = "%d%02d%02d" % (year,month,2)
        
        link = nytimes_url % (start_date, end_date, nytimes_key)
        r = requests.get(link)

        articles = r.json()

        for article in articles['response']['docs']:
            try:
                headline = "\"%s\"" % (article['headline']['main'])
                snippet = "\"%s\"" % (article['snippet'])
                url = "\"%s\"" % (article['web_url'])
                out_str = ",".join([start_date,headline,snippet,url])
                print out_str
                outfile.write(out_str)
        
                break
            except:
                pass
    time.sleep(10)    
    
outfile.close()
