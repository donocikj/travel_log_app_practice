from datetime import datetime
import pytest

from django.contrib.auth.models import User
from tlog.models import Travel, Entry

@pytest.fixture
def user_sample(db):
    # todo review user creation, even if just for a test
    yield User.objects.create(username="test_user", password="password")

@pytest.fixture
def travel_sample(user_sample):
    yield Travel.objects.create(traveller=user_sample)

@pytest.fixture
def entry_sample_1(travel_sample):
    yield Entry.objects.create(travel=travel_sample, location="testlocation", time=datetime.now(), content="testcontent")