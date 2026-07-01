import datetime
import config
from .mail import send_email
from .api import post_request

url = "https://web-api-prod-ytp.tcddtasimacilik.gov.tr/tms/train/train-availability?environment=dev&userId=1"

def fetch_and_filter_journeys():
    departure_date = datetime.datetime.strptime(config.date, "%Y-%m-%d").strftime("%d-%m-%Y")
    body = {
        "searchRoutes": [
            {
                "departureStationId": config.binis_istasyon_id,
                "departureStationName": config.binis_istasyon_adi,
                "arrivalStationId": config.inis_istasyon_id,
                "arrivalStationName": config.inis_istasyon_adi,
                "departureDate": f"{departure_date} 00:00:00"
            }
        ],
        "passengerTypeCounts": [{"id": 0, "count": 1}],
        "searchReservation": False,
        "searchType": "DOMESTIC",
        "blTrainTypes": ["TURISTIK_TREN"]
    }
    print(f"Checking for date: {config.date}")
    response = post_request(url, body)
    print("STATUS:", response.status_code)
    if response.status_code != 200:
        print("RAW RESPONSE:", response.text[:500])
        return
    data = response.json()
    for leg in data.get("trainLegs", []):
        for availability in leg.get("trainAvailabilities", []):
            for train in availability.get("trains", []):
                check_train(train)

def check_train(train):
    departure_time_str = None
    for seg in train.get("trainSegments", []):
        if seg["departureStationId"] == config.binis_istasyon_id:
            departure_time_str = seg["departureTime"]
            break
    if not departure_time_str:
        return

    departure_dt = datetime.datetime.fromisoformat(departure_time_str)

    if departure_dt.strftime("%Y-%m-%d") != config.date:
        return

    if config.istekli_saatler and departure_dt.strftime("%H:%M") not in config.istekli_saatler:
        return

    for cca in train.get("cabinClassAvailabilities", []):
        if cca["cabinClass"]["name"] == "EKONOMİ" and cca["availabilityCount"] > 0:
            print(f"Available: {cca['availabilityCount']} EKONOMİ seat(s) on {train['name']} at {departure_dt.strftime('%H:%M')}")
            send_email(
                train["name"],
                departure_dt.strftime("%Y-%m-%d %H:%M"),
                "-",
                f"{cca['availabilityCount']} boş yer"
            )
