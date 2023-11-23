import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    #print(r.text)

    #By default the r variable has a type of str
    categories = r.json()
    #Now categories var it is a list.
    print(categories[0])
    #Iterate through the list of dict.
    for category in categories:
        print(category['id'])