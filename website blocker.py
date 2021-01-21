from datetime import datetime

host_path= "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

website_list = ["facebook.com", "www.facebook.com"]

start_date = datetime(2021,1,20)
end_date = datetime(2021,2,8)
today_date = datetime(datetime.now().year, datetime.now().month, datetime.now().day)

while True:
    if (start_date <= today_date < end_date):
        with open(host_path, "r+") as file:
            content = file.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")

        print("ALL THE LISTED WEBSITES ARE BLOCKED!!")
        break
    else:

        with open(host_path, "r+") as file:
            content = file.readline()
            file.seek(0)

            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)

            file.truncate()
        print("WEBSITES ARE UNBLOCKED!!")

        break