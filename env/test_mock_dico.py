import fbapp.parsage as script

import requests
from bs4 import BeautifulSoup


def test_http_return2(monkeypatch):
    results = ("nm")

    def mockreturn(request):
        return results

    monkeypatch.setattr(requests, 'request', mockreturn)
    assert script.search_dico("l'ardoise") == results

