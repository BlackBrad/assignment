import requests

API = 'https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'

def get_api_information():
    '''
        TODO: DO I NEED SOMETHING HERE?
    '''
    expected_response_code = "200"
    response_code = requests.get(API)

    if expected_response_code in str(response_code):
        return response_code.json()

    return None

def test_data():
    '''
        TODO: DO I NEED SOMETHING HERE?
    '''
    breakpoint()
    data = get_api_information()

    if data is None:
        # TODO: probably need to do something better than this!
        return
    
    print(data)
