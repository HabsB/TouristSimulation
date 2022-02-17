from urllib import request
import json
import ast
from flask import *
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def arts():
    data_set = {'Page': 'Art', 'Message': 'Successfully loaded the Home page', 'TimeStamp ':time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/detail/', methods=['GET'])
def request_detail():
    user_query = str(request.args.get('detail')) # /detail/?detail=Ashu
    with open('art_detail.json') as json_file:
        for msg in json_file:
            massegeObject = json.loads(msg)
            for item in massegeObject.values():
                key_list = list(item.keys())
                val_list = list(item.values())
                posn  = key_list.index('name')
                asignee = val_list[posn]
                if(asignee== user_query):
                    print(item)
                    return item
        # data_set = {'Page': 'Art Detail', 'Message':'No Detail Requested by the specific user'}
        data_set = {}
        json_dump = json.dumps(data_set)
        return json_dump    

if __name__ == '__main__':
    app.run(port=7777)  
    

    
    
      