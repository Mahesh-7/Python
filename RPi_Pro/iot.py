import urllib3

write_link = "http://azetech.in/office/scripts/IoT.php?api=UpdateValue&ID=IOTCMP00129&value="
read_link="http://azetech.in/office/scripts/IoT.php?api=ReadValue&ID=IOTCMP00126"

def read_data_base(url):
    http = urllib3.connection_from_url(url)
    r = http.urlopen('GET',url)
    data = r.data.decode("utf-8-sig").encode("utf-8")
    print(data)
 


def Write_Database(url,data):
    http_pool = urllib3.connection_from_url(url)
    r = http_pool.urlopen('SET',url+str(data))
    print(r)

Write_Database(write_link,50)
read_data_base(read_link)
