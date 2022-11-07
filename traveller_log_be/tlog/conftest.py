from datetime import datetime, timezone
import json
import pytest

from django.contrib.auth.models import User
from tlog.models import Travel, Entry
from auth_token.views import login_view

@pytest.fixture
def user_sample(db):
    yield User.objects.create_user(username="test_user", password="password")

@pytest.fixture
def user_sample_token(rf, user_sample):
    creds = json.dumps({
        "username":"test_user",
        "password":"password"
    })
    request = rf.post("/auth/login/", creds, content_type="application/json")
    response = login_view(request)

    # todo find a better way to obtain token
    token = response.data["token"]
    yield token


@pytest.fixture
def travel_sample(user_sample):
    yield Travel.objects.create(traveller=user_sample)

@pytest.fixture
def entry_sample_1(travel_sample):
    yield Entry.objects.create(travel=travel_sample, location="testlocation", time=int(datetime.now(timezone.utc).timestamp()), content="testcontent")