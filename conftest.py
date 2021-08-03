# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.main_url()
    fixture.session.login(user="admin", password="secret")

    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
