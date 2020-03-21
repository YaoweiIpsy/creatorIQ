import requests
import json
from pathlib import Path

reqheaders={
    'X-SOCIALEDGE-ID': '3da9ff7e400b1d535b0115ca064dee02',
    'Content-Type': "application/json"
}

Path("./datas/list").mkdir(parents = True, exist_ok=True)

with open("./listIds") as fp:
    line = fp.readline()
    while line:
        id = line.strip()
        print(id)
        with open("./datas/list/{}.json".format(id), "w") as wfp:
            skip = 0
            count = 0
            while True:
                r = requests.get(
                    "https://api.creatoriq.com/api/view?params[ListId]={}&output=cs&view=List/List&skip={}&take=2000".format(
                        id, skip), headers=reqheaders)
                if r.status_code != 200 :
                    raise Exception("error")
                data = json.loads(r.text)
                if len(data["results"]) == 0:
                    break
                for record in data["results"]:
                    wfp.write(json.dumps(record) + "\n")
                skip += 2000
        line = fp.readline()
