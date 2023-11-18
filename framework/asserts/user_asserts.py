from hamcrest import assert_that, is_


def assert_all_user_data_matches(response_data, expected_user):
    """
    Asserts that all relevant user data in the response matches the expected user data.

    Args:
        response_data (dict): The user data from the API response.
        expected_user (dict): The expected user data.

    Raises:
        AssertionError: If any of the assertions fail.
    """

    fields_to_compare = {
        "id": "id",
        "firstName": "first_name",
        "lastName": "last_name",
        "email": "email",
        "password": "hashed_password",
    }

    for response_field, user_field in fields_to_compare.items():
        assert_that(response_data[response_field],
                    is_(expected_user[user_field]),
                    reason=f"Expected {response_field} should be {expected_user[user_field]}, found: {response_data[response_field]}")

    # Asserting specific fields that are not directly mapped
    assert_that(response_data["stripeCustomerToken"], is_(None),
                reason='Expected user stripe customer token should be None')

    # Asserting specific fields that are not directly mapped
    assert_that(response_data["address"], is_(None),
                reason='Expected user address should be None')
