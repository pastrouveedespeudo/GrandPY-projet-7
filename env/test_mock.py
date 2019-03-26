import fbapp.google_map_api_python as script

import googlemaps
import urllib.request 


def test_http_return(monkeypatch):
    results = (48.8747265, 2.3505517)

    def mockreturn(request):
        return results

    monkeypatch.setattr(urllib.request, mockreturn)
    assert script.api_google_map("OpenClassrooms") == results







