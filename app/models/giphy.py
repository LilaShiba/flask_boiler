import json, requests

def api_call(search_term):
    # get api key
    # removed
    # create url by looking at docs
    url = 'https://api.giphy.com/v1/gifs/search?api_key='+api_key+'&q='+search_term+'&limit=25&offset=5&rating=PG-13&lang=en'
    # print url for parsing
    print(url)
    # make call
    data = requests.get(url).json()
    # basic data
    all_pics = data['data']
    # image data
    pics = data['data'][0]['images']['fixed_height_still']
    # return values
    return pics, all_pics
