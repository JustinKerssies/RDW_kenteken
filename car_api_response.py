import requests


def additional_apis(url):
    # Receive the url
    search_url = url

    temp_dict = []

    r = requests.get(search_url)
    response_dict = r.json()

    if len(response_dict) == 0:
        return ''
    else:
        for response in response_dict:
            temp_dict.append(response)
        return temp_dict
