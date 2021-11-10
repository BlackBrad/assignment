import requests


def get_api_information(api):
    ''' Using the requests library, gets the information from the given
        api and returns the data formatted as JSON. If the request to get
        the api fails then None is returned instead.

        Args:
            api (str): URL for the api to get data from

        Returns:
            dict: Empty if the request fails. Returns a dictionary full of
                  data from the api otherwise
    '''
    expected_response_code = "200"
    response_code = requests.get(api)

    if expected_response_code in str(response_code):
        return response_code.json()

    return {}


def test_data():
    '''
        TODO: DO I NEED SOMETHING HERE?
    '''

    api = ('https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?'
           'catalogue=false')
    expected_name = "Carbon credits"
    expected_name_promtions = "Gallery"
    expected_description = "Good position in category"
    data = get_api_information(api)

    if len(data) < 1:
        # TODO: probably need to do something better than this!
        assert False

    assert data['Name'] == expected_name
    assert data['CanRelist'] is True

    for entry in data['Promotions']:
        if (entry['Name'] == expected_name_promtions and
                expected_description in entry['Description']):
            assert True
