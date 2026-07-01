import requests
import config

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "tr",
    "Content-Type": "application/json",
    "Origin": "https://ebilet.tcddtasimacilik.gov.tr",
    "unit-id": "3895",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
}

def post_request(url, body):
    return requests.post(url, json=body, headers=headers)
