import json

with open('resp.txt') as fh:
    data = json.load(fh)
    print(
        json.dumps(
            data,
            indent=4
        )
    )