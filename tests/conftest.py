import os
import tempfile

import pytest

from pytest_intro.models import Article


@pytest.fixture(autouse=True)
def database():
    _, file_name = tempfile.mkstemp()
    os.environ['DATABASE_NAME'] = file_name
    Article.create_table(database_name=file_name)
    # Using yield here runs the test and once done will continue with fixture
    yield
    os.unlink(file_name)
