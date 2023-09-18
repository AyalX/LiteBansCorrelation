import requests
import re
from datetime import datetime

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    return {
        'date': None,
        'ip': ip,
        'isp': data['isp'],
        'country': data['country'],
        'region': data['regionName'],
        'city': data['city'],
    }

def get_user_data_from_file(file_path):
    user_data = {}
    current_user = None
    with open(file_path, 'r') as file:
        for line in file:
            if "Login history for" in line:
                current_user = re.search(r'Login history for (\w+)', line).group(1)
                user_data[current_user] = []
            elif current_user:
                date_ip_match = re.search(r'\[(\d{4}-\d{2}-\d{2})\] \w+: (\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)', line)
                if date_ip_match:
                    user_data[current_user].append(date_ip_match.groups())
    return user_data

file_path = "users.txt"
user_data = get_user_data_from_file(file_path)

user_info = {}
for user, data in user_data.items():
    user_info[user] = [get_ip_info(ip) for date, ip in data]
    # Assign dates to the corresponding dictionaries
    for i, (date, _) in enumerate(data):
        user_info[user][i]['date'] = date

# Find shared IPs and dates
shared_dates_ips = set()
for user1_info in user_info.values():
    for user2_info in user_info.values():
        if user1_info is not user2_info:
            shared_dates_ips.update((entry['date'], entry['ip']) for entry in user1_info if entry in user2_info)

# Add formatting to shared IPs and dates
for user, info in user_info.items():
    for entry in info:
        if (entry['date'], entry['ip']) in shared_dates_ips:
            entry['date'] = f"__{entry['date']}__"
            entry['ip'] = f"`{entry['ip']}`"

# Print results
for user, info in user_info.items():
    print(f"**{user} Activity:**")
    for entry in info:
        print("- Date: {date} | IP: {ip} | ISP: {isp} | Country: {country} | Region: {region} | City: {city}".format(**entry))
