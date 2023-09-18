## LiteBans Correlation IP Tool

### Description

The LiteBans Correlation IP Tool is a Python script specifically designed to work with LiteBans user logs. It helps administrators identify patterns and correlations in user login data based on IP addresses and login dates. By tracking shared IP addresses and dates across different users, it aims to facilitate investigations into suspicious activities or behaviors, potentially signaling shared or unauthorized account usage.

### Features

1. Processes LiteBans user logs to extract login histories, including dates and IP addresses.
2. Fetches detailed geographical and ISP information for logged IP addresses using `ip-api.com`.
3. Identifies and highlights shared IP addresses and login dates across different users, aiding in pinpointing potential account sharing or unauthorized access incidents.
4. Outputs comprehensive user activity reports with enriched IP information.
5. Discord markdown supported.

### Dependencies

The following Python packages are required to run this script:

- `requests`: for making API requests to retrieve IP information from `ip-api.com`.
- `re`: for using regular expressions to parse the log file data.

You can install these dependencies using the following command:

```sh
pip install requests
```

### Installation and Usage

1. Ensure that you have a `users.txt` file with LiteBans log data in the following format:
   
   ```
   Login history for user1
   [2023-09-18] Login: 123.45.67.89
   [2023-09-18] Login: 123.45.67.90
   
   Login history for user2
   [2023-09-18] Login: 123.45.67.89
   ```

2. Clone the repository or download the script to your local system.
   
3. Run the script in your terminal:

   ```sh
   python "LiteBans Correlation Tool.py".py
   ```

4. The script will output the analyzed data with detailed IP information and markers indicating shared IPs and dates.

### Output

The script generates a detailed report for each user that includes:

- **Username Activity**:
  - Date (shared dates are highlighted with `__` underscore)
  - IP (shared IPs are highlighted with backticks `)
  - ISP
  - Country
  - Region
  - City

### Contributing

We welcome contributions to this project! Feel free to fork the repository and submit your contributions via pull requests.

### License

This project is distributed under the MIT License. See LICENSE file for more information.

### Support and Contact

If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository. We appreciate your feedback!

### Acknowledgements

This tool utilizes the IP-API service to retrieve IP address information. Use in accordance with IP-API's terms of service.
