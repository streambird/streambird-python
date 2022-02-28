# pylint: disable=missing-function-docstring

import os
import time
import uuid
from datetime import datetime

import pytest
import streambird

from streambird.exceptions import (
    StreambirdDuplicateResource,
    StreambirdInvalidRequest,
    StreambirdResourceNotFound,
    StreambirdUnauthorized,
)

TEST_PROJECT_NAME = 'streambird-python'

try:
    print(f'API Client Version: {streambird.__version__}')
    test_api_key = os.environ['STREAMBIRD_TEST_API_KEY']

    if test_api_key.startswith('sk_') or test_api_key.endswith('|test'):
        client = streambird.Client(test_api_key, 'pytest')
    else:
        raise Exception('Please provide a valid TEST environment key.')
except KeyError as err:
    raise Exception(
        'Please set the environment variable STREAMBIRD_TEST_API_KEY to run tests.'
    ) from err

def test_magic_links_login_or_create():
    with pytest.raises(StreambirdInvalidRequest):
        client.magic_links.email.login_or_create(email='test@streambird.io')



