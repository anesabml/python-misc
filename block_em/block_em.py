import time
from datetime import datetime

hosts_path = r"/etc/hosts"
hosts_temp = "hosts"
redirect = "127.0.0.1"
web_sites_list = ["facebook.com"]

while True:
    today = datetime.now()
    if datetime(today.year, today.month, today.day, 8) < today < datetime(today.year, today.month, today.day, 16):
        print "Go get shit done"

        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in web_sites_list:
                if website not in content:
                    file.write(redirect+" "+website+"\n")
    else:
        print "Go have fun"
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in web_sites_list):
                    file.write(line)
                file.truncate()
                time.sleep(5)