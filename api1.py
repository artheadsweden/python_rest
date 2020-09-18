import requests

def main():

    user = {
        "name": "Joe Doe haha",
        "job": "leader"
    }

    resp = requests.post('https://reqres.in/api/users/2', user)
    print(resp.status_code)
    answer = resp.json()
    print(answer)
  
    


if __name__ == '__main__':
    main()