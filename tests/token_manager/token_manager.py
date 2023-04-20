import pytest
import requests

import config
from fixtures.controller_manager import *
from assertpy import assert_that


@pytest.mark.passant
@pytest.mark.end2end
def test_generate_token(generate_token):
    token_request = generate_token.status_code
    response = generate_token.json()
    if token_request == 201:
        token = response['token']
        creationDate = response['creationDate']
        expirationDate = response['expirationDate']
        assert_that(token).is_not_empty()
        assert_that(creationDate).is_not_empty()
        assert_that(expirationDate).is_not_empty()
        print("\n token = {token_request}".format(token_request=token_request))
    if token_request == 200:
        token = response['token']
        creationDate = response['creationDate']
        expirationDate = response['expirationDate']
        assert_that(token).is_not_empty()
        assert_that(creationDate).is_not_empty()
        assert_that(expirationDate).is_not_empty()
        print("\n token = {token_request}".format(token_request=token_request))


# @pytest.mark.generate
# def test_generate_token_200(generate_token):
#     token_request = generate_token.status_code
#     response = generate_token.json()
#     # if token_request == 200:
#     token = response['token']
#     creationDate = response['creationDate']
#     expirationDate = response['expirationDate']
#     assert_that(token).is_not_empty()
#     assert_that(creationDate).is_not_empty()
#     assert_that(expirationDate).is_not_empty()
#     print("\n token = {token_request}".format(token_request=token_request))

@pytest.mark.skip
@pytest.mark.non_passant
@pytest.mark.end2end
@pytest.mark.parametrize("url, body, headers, code_statut", config.base_data)
def test_generate_token_using_invalid_credential(url, body, headers, code_statut):
    token_request = requests.post(url=url, data=body, headers=headers)
    statut = token_request.status_code
    if statut == code_statut:

        assert_that(statut).is_equal_to(code_statut)
        print("\n Statut = {statut}".format(statut=statut))


