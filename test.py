import requests


API = ('https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?'
       'catalogue=false')


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

    return None


def test_name():
    expected_name = "Carbon credits"

    data = get_api_information(API)

    assert data is not None, f"Error fetching data from {API}"

    assert data['Name'] == expected_name


def test_can_relist():
    expected_can_relist = True

    data = get_api_information(API)

    assert data is not None, f"Error fetching data from {API}"

    assert data['CanRelist'] is expected_can_relist


def test_promotions():
    expected_name_promotions = "Gallery"
    expected_description = "Good position in category"

    data = get_api_information(API)

    assert data is not None, f"Error fetching data from {API}"

    for entry in data['Promotions']:
        if (entry['Name'] == expected_name_promotions and
                expected_description in entry['Description']):
            assert True
            break
    else:
        assert False
