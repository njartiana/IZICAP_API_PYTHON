from fixtures.controller_manager import *
from assertpy import assert_that

@pytest.mark.end2end
def test_create_user(create_dynamic_user):
    user_request = create_dynamic_user.status_code

    if user_request == 201:
        response = create_dynamic_user.json()
        print(response['username'])
        assert_that(response['username']).is_equal_to(username)


@pytest.mark.end2end
def test_create_static_user(create_static_user):
    user_request = create_static_user.status_code

    if user_request == 201:
        response = create_static_user.json()
        print(response['username'])
        assert_that(response['username']).is_equal_to("username11")
    if user_request == 409:
        print("\nError : User already exist")


@pytest.mark.end2end
def test_create_user_by_user(create_user_by_user):
    user_request = create_user_by_user.status_code
    if user_request == 403:
        print("\n Error : Can't create new user with a non-admin unexpired token")

@pytest.mark.end2end
def test_create_user_by_unexisting_token(create_user_by_unexisting_token):
    user_request = create_user_by_unexisting_token.status_code
    if user_request == 401:
        print("\n Error : Can't create new user without a valid unexpired token")