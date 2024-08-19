import requests

# endpoint="https://api.perfecttense.com/correct"
endpoint="https://api.sapling.ai/api/v1/summarize"
# headers={
#      "Authorization": "qTIXirQIWId4TAbg30QLfQtt",
#    "AppAuthorization": "9WFMOlhknXEjezKx8UpHqgtt"

# }
# param={
#     "text": "This articl have some errors", 
#     "responseType": ["corrected"]
# }
param={"key":"5Q7E2TSLA3Q27U6NHJ7VW38P1VO4SD7C", 
       "text":"HTTP status codes can provide a wide range of information about client and server requests. However, some of these messages indicate problems, such as the HTTP 408 Request Timeout error.", 
       "session_id": "test session"}
response=requests.post(url=endpoint,json=param)

response_json=response.json()
print(response_json["result"])