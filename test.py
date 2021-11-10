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
    ''' Tests that the data found at a particular api matches the following
        criteria, the Name must be "Carbon Credits", the CanRelist field must
        be true, and an entry in a list with the key 'Promotions' must contain
        the name 'Gallery', as well as a description that contains the text,
        "Good position in category". This is done by initally requesting the
        data, if the request is successful then the Name and CanRelist fields
        are verified. If they are what is expected then the Promotions field
        is iterated through to find the expected name and description. If those
        are found then the test passes.

        Args:
            None

        Returns:
            None
    '''

    api = ('https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?'
           'catalogue=false')
    expected_name = "Carbon credits"
    expected_name_promtions = "Gallery"
    expected_description = "Good position in category"
    data = get_api_information(api)

    if len(data) < 1:
        # Fail the test if we were unsuccessful in getting data from the api
        # passed to get_api_information
        assert False

    assert data['Name'] == expected_name
    assert data['CanRelist'] is True

    # Search the Promotions list for the expected name and expected description
    for entry in data['Promotions']:
        if (entry['Name'] == expected_name_promtions and
                expected_description in entry['Description']):
            assert True
            break
    else:
        # If we do not break out of the loop, then name and description we are
        # expecting was not found. In this case we want the test to fail
        assert False
