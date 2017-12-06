## Overview
There is so called [Myers–Briggs Type Indicator](https://en.wikipedia.org/wiki/Myers%E2%80%93Briggs_Type_Indicator) (MBTI) that divides people in 16 categories based on 4 parameters with 2 possible values in each param. Here is my version of prediction logic based on previously trained bag of words. You are passing text written by some person and as result you are getting MBTI type of that person.

Technology tags: Python, PostgreSQL, Flask

## Example of usage
#### Server
```
v:~/ml/python/mbti$ python3 service.py 
 * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 256-077-732
```

#### Client
```python
import requests, json
url = 'http://127.0.0.1:3000/api'
data = json.dumps({'text': 'smoke on the water fire in the sky'})
r = requests.post(url, data)
print(r.json())
#{'results': 'ISTJ'}
```
