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

# Get counts for dates and IPs
date_users = {}
ip_users = {}
for user, info in user_info.items():
    for entry in info:
        date_users.setdefault(entry['date'], set()).add(user)
        ip_users.setdefault(entry['ip'], set()).add(user)

# Mark dates and IPs
for user, info in user_info.items():
    for entry in info:
        if len(date_users[entry['date']]) > 1:
            entry['date'] = f"__{entry['date']}__"
        if len(ip_users[entry['ip']]) > 1:
            entry['ip'] = f"`{entry['ip']}`"

for user, info in user_info.items():
    print(f"{user} Activity:")
    for entry in info:
        print("- Date: {date} | IP: {ip} | ISP: {isp} | Country: {country} | Region: {region} | City: {city}".format(**entry))
