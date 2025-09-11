import os
import requests
from datetime import datetime

def futureEvents(country: str, plannedDate: int):
    base_url = f"https://jsonmock.hackerrank.com/api/events?country={country}"
    page = 1
    events = []

    while True:
        res = requests.get(f"{base_url}&page={page}").json()
        data = res.get("data", [])

        for e in data:
            try:
                # Parse ISO datetime and convert to epoch ms
                event_time = datetime.fromisoformat(
                    e["date"].replace("Z", "+00:00")
                ).timestamp() * 1000
            except Exception:
                continue

            if event_time > plannedDate:
                # FIX: wrap values in a tuple
                events.append((event_time, e["name"]))

        if page >= res.get("total_pages", 1):
            break
        page += 1

    if not events:
        return ["", ""]
    
    events.sort(key=lambda x: x[0])
    return [events[0][1], events[-1][1]]


# ---- DO NOT MODIFY MAIN ----
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    country = input()
    plannedDate = int(input().strip())

    result = futureEvents(country, plannedDate)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
