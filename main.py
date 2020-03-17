import requests
from pathlib import Path

reqheaders={
    'X-SOCIALEDGE-ID': '3da9ff7e400b1d535b0115ca064dee02',
    'Content-Type': "application/json"
}

Path("./datas").mkdir(exist_ok=True)

with open("./campaignIds") as fp:
    line = fp.readline()
    while line:
        id = line.strip()
        print(id)
        r = requests.get("https://api.creatoriq.com:443/api/campaign/" + id, headers = reqheaders)
        if r.status_code != 200 :
            raise Exception("error")
        fp1 = open("./datas/" + id + ".json","w")
        fp1.write(r.text)
        r.close()
        fp1.close()
        r = requests.get("https://api.creatoriq.com:443/api/campaign/" + id + "/activity", headers = reqheaders)
        if r.status_code != 200 :
            raise Exception("error")
        fp1 = open("./datas/" + id + "_activity.json","w")
        fp1.write(r.text)
        r.close()
        fp1.close()
        line = fp.readline()
