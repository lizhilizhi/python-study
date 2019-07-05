

import json
import codecs
users={
    'li':{
        'nba':'马刺',
        'cba':'山东高速'
    },
    'wang':{
        'nba':'火箭',
        'cba':'北控'
    }
}

j = json.dumps(users, ensure_ascii=False)

with codecs.open('users.json', "w", "utf-8") as f:
    f.write(j)


