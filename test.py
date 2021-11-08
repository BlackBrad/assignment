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
    expected_name = "Carbon credits"
    expected_name_promtions = "Gallery"
    expected_description = "Good position in category"
    data = get_api_information()

    if data is None:
        # TODO: probably need to do something better than this!
        assert False

    assert data['Name'] == expected_name
    assert data['CanRelist'] == True

    for entry in data['Promotions']:
        if (entry['Name'] == expected_name_promtions and
                expected_description in entry['Description']):
            assert True

    print(data)
