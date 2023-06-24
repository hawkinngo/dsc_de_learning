import requests
import json

url = "https://ap-southeast-1.aws.data.mongodb-api.com/app/data-ihdyg/endpoint/data/v1/action/findOne"
payload = json.dumps(
    {
        "collection": "collection-1",
        "database": "de-learning-db",
        "dataSource": "de-learning",
        "projection": {"_id": 1},
    }
)
headers = {
    "Content-Type": "application/json",
    "Access-Control-Request-Headers": "*",
    "api-key": "L0lmxrtZtPWOBJKb2Guut8llKZVBJB7HwTfcRK0YADYKfZpHwT2HsDsutQRaoxU3",
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
