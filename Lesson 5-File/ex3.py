
import json

with open('SearchShowAction.json','r') as f :
    data = json.load(f)
    print(json.dumps(data, indent=4))

    #print(data)




