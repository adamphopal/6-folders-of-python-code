import requests
import json

def get_joke():
    res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
    if res.status_code == requests.codes.ok:
        print(str(res.json()['joke']))
    else:
        print('oops!I ran out of jokes')

    joke = 'Adams joke for today is '
    joke += (str(res.json()['joke']))
    
    return joke

             


