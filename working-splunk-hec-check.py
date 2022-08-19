import requests

## define your varriables
# channel is HEC token
channel = input("Input HEC Token: ")
# company's hostname
company = input("Input companys Splunk Cloud Hostname: ")
# http or https
protocol = "https"
# cloud customers have `http-inputs-` before hostname
host = "http-inputs-" + company + ".splunkcloud.com"
# endpoint = collector or collector/raw
endpoint = "/services/collector"

# generated url
url = protocol + "://" + host + endpoint

params = {
    "channel": channel
}

headers = {
    "Authorization": f'Splunk {channel}'
}

# verify=False if invalid cert
r = requests.post(url, params=params, headers=headers)

print(
    'You should recieve \'{"text":"No data","code":5}\' if inputs are working.')
print('Result:', r.text)
