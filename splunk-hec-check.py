import requests

## define your varriables
# channel is HEC token
channel = "00000000-0000-0000-0000-0000000000"
# http or https
protocol = "https"
# cloud customers have `http-inputs-` before hostname
host = http - inputs -$company$.splunkcloud.com
# endpoint = collector or collector/raw
endpoint = "/services/collector"

# generated url
url = protocol + "://" + host + endpoint

params = {
    "channel": channel
}

headers = {
    "Authorization": "Splunk {}".format(channel)
}

# verify=False if invalid cert
r = requests.post(url, params=params, headers=headers)

# you should recieve '{"text":"No data","code":5}' if inputs are working 
print(r.text)
