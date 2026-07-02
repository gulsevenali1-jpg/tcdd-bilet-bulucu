import requests
import config

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "tr",
    "Content-Type": "application/json",
    "Origin": "https://ebilet.tcddtasimacilik.gov.tr",
    "Referer": "https://ebilet.tcddtasimacilik.gov.tr/",
    "unit-id": "3895",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"124\", \"Chromium\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
}

def post_request(url, body):
    return requests.post(url, json=body, headers=headers)
