import requests

import logging

log = logging.getLogger(__name__)

API = ('https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?'
       'catalogue=false')


def get_api_information(api):
    ''' Using the requests library, gets the information from the given
        api and returns the data formatted as JSON. If the request to get
        the api fails then None is returned instead.

        Args:
            api (str): URL for the api to get data from

        Returns:
            dict | None: Empty if the request fails. Returns None otherwise
    '''
    log.info(f"Request data from {api}")
    expected_response_code = "200"

    try:
        response_code = requests.get(api)
    except requests.exceptions.ConnectionError:
        log.error(f"Unable to connect to given URL: {api}")
        raise
    except requests.exceptions.MissingSchema:
        log.error(f"The given URL {api} is invalid")
        raise

    if expected_response_code in str(response_code):
        log.info(f"Succesfully requested data from {api}")
        return response_code.json()

    log.error("Unable to succesfully request data from {api}")
    log.error(f"Expected response code containg {expected_response_code} but "
              f"got {response_code}")
    return None


def test_name():
    ''' Tests that a given api with the key-value pair with the key 'Name'
        contains the value 'Carbon Credits'.

        Args:
            None

        Returns:
            None
    '''
    log.info("Starting test_name")
    expected_name = "Carbon credits"

    data = get_api_information(API)

    assert data is not None, f"Error fetching data from {API}"

    assert data['Name'] == expected_name, (f"Expected '{expected_name}', got "
                                           f"'{data['Name']}'")


def test_can_relist():
    ''' Tests that a given api with a key-value pair, with the key 'CanRelist'
        has a value set to True

        Args:
            None

        Returns:
            None
    '''
    log.info("Starting test_can_relist")
    expected_can_relist = True

    data = get_api_information(API)

    assert data is not None, f"Error fetching data from {API}"

    assert data['CanRelist'] is expected_can_relist, (
            f"Expected '{expected_can_relist}', got {data['CanRelist']}")


def test_promotions():
    ''' Tests that a given api with a key-value pair, with the key 'Promotions'
        contains a list of more key-value pairs. One of those key-value pairs
        must contain the key 'Name' with the value 'Gallery'. It must also
        contain they key 'Description' with a value containg 'Good position in
        category'. This is done by iterating through the Promotions key in
        the api and verifying that the criteria stated above is met, if so the
        test passes.

        Args:
            None

        Returns:
            None
    '''
    log.info("Starting test_promotions")
    expected_name = "Gallery"
    expected_description = "Good position in category"

    data = get_api_information(API)

    assert data is not None, f"Error fetching data from {API}"

    log.info("Iterate through the Promotions list")
    for entry in data['Promotions']:
        if (entry['Name'] == expected_name and
                expected_description in entry['Description']):
            log.info(f"Expected name: '{expected_name}' and "
                     f"expected_description: '{expected_description}' found "
                     "in Promotions list")
            assert True
            break
    else:
        # If the for loop does not break then expected_name and
        # expected_description were not found. In this case we want to fail
        log.info(f"Unable to find Name: '{expected_name}' and Description: "
                 f"'{expected_description}' in Promotions list")
        assert False
