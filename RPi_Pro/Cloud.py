import urllib3

Write_Link = ""
Read_Link = "http://azetech.in/office/scripts/IoT.php?api=ReadValue&ID=IOTCMP00144"

def Read_Database(url):
    http_pool = urllib3.connection_from_url(url)
    r = http_pool.urlopen('GET',url)
    data = r.data.decode("utf-8-sig")
    #print(data)
    return data
    

def Write_Database(url,data):
    http_pool = urllib3.connection_from_url(url)
    r = http_pool.urlopen('SET',url+str(data))
    

