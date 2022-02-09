import argparse
import textwrap
from requests_html import HTMLSession

global session
session = HTMLSession()
global cc
cc = {'AF': 'Afghanistan', 'AL': 'Albania', 'DZ': 'Algeria', 'AS': 'American Samoa', 'AD': 'Andorra', 'AO': 'Angola', 'AI': 'Anguilla', 'AQ': 'Antarctica', 'AG': 'Antigua and Barbuda', 'AR': 'Argentina', 'AM': 'Armenia', 'AW': 'Aruba', 'AU': 'Australia', 'AT': 'Austria', 'AZ': 'Azerbaijan', 'BS': 'Bahamas', 'BH': 'Bahrain', 'BD': 'Bangladesh', 'BB': 'Barbados', 'BY': 'Belarus', 'BE': 'Belgium', 'BZ': 'Belize', 'BJ': 'Benin', 'BM': 'Bermuda', 'BT': 'Bhutan', 'BO': 'Bolivia', 'BQ': 'Bonaire, Sint Eustatius and Saba', 'BA': 'Bosnia and Herzegovina', 'BW': 'Botswana', 'BV': 'Bouvet Island', 'BR': 'Brazil', 'IO': 'British Indian Ocean Territory', 'BN': 'Brunei Darussalam', 'BG': 'Bulgaria', 'BF': 'Burkina Faso', 'BI': 'Burundi', 'CV': 'Cabo Verde', 'KH': 'Cambodia', 'CM': 'Cameroon', 'CA': 'Canada', 'KY': 'Cayman Islands', 'CF': 'Central African Republic', 'TD': 'Chad', 'CL': 'Chile', 'CN': 'China', 'CX': 'Christmas Island', 'CC': 'Cocos (Keeling) Islands', 'CO': 'Colombia', 'KM': 'Comoros', 'CD': 'Congo Democratic Republic of the)', 'CK': 'Cook Islands', 'CR': 'Costa Rica', 'HR': 'Croatia', 'CU': 'Cuba', 'CW': 'Curaçao', 'CY': 'Cyprus', 'CZ': 'Czechia', 'CI': "Côte d'Ivoire", 'DK': 'Denmark', 'DJ': 'Djibouti', 'DM': 'Dominica', 'DO': 'Dominican Republic', 'EC': 'Ecuador', 'EG': 'Egypt', 'SV': 'El Salvador', 'GQ': 'Equatorial Guinea', 'ER': 'Eritrea', 'EE': 'Estonia', 'SZ': 'Eswatini', 'ET': 'Ethiopia', 'FK': 'Falkland Islands', 'FO': 'Faroe Islands', 'FJ': 'Fiji', 'FI': 'Finland', 'FR': 'France', 'GF': 'French Guiana', 'PF': 'French Polynesia', 'TF': 'French Southern Territories', 'GA': 'Gabon', 'GM': 'Gambia', 'GE': 'Georgia', 'DE': 'Germany', 'GH': 'Ghana', 'GI': 'Gibraltar', 'GR': 'Greece', 'GL': 'Greenland', 'GD': 'Grenada', 'GP': 'Guadeloupe', 'GU': 'Guam', 'GT': 'Guatemala', 'GG': 'Guernsey', 'GN': 'Guinea', 'GW': 'Guinea-Bissau', 'GY': 'Guyana', 'HT': 'Haiti', 'HM': 'Heard Island and McDonald Islands', 'VA': 'Holy See', 'HN': 'Honduras', 'HK': 'Hong Kong', 'HU': 'Hungary', 'IS': 'Iceland', 'IN': 'India', 'ID': 'Indonesia', 'IR': 'Iran', 'IQ': 'Iraq', 'IE': 'Ireland', 'IM': 'Isle of Man', 'IL': 'Israel', 'IT': 'Italy', 'JM': 'Jamaica', 'JP': 'Japan', 'JE': 'Jersey', 'JO': 'Jordan', 'KZ': 'Kazakhstan', 'KE': 'Kenya', 'KI': 'Kiribati', 'KW': 'Kuwait', 'KG': 'Kyrgyzstan', 'LA': "Lao People's Democratic Republic", 'LV': 'Latvia', 'LB': 'Lebanon', 'LS': 'Lesotho', 'LR': 'Liberia', 'LY': 'Libya', 'LI': 'Liechtenstein', 'LT': 'Lithuania', 'LU': 'Luxembourg', 'MO': 'Macao', 'MG': 'Madagascar', 'MW': 'Malawi', 'MY': 'Malaysia', 'MV': 'Maldives', 'ML': 'Mali', 'MT': 'Malta', 'MH': 'Marshall Islands (the)', 'MQ': 'Martinique', 'MR': 'Mauritania', 'MU': 'Mauritius', 'YT': 'Mayotte', 'MX': 'Mexico', 'FM': 'Micronesia', 'MD': 'Moldova', 'MC': 'Monaco', 'MN': 'Mongolia', 'ME': 'Montenegro', 'MS': 'Montserrat', 'MA': 'Morocco', 'MZ': 'Mozambique', 'MM': 'Myanmar', 'NA': 'Namibia', 'NR': 'Nauru', 'NP': 'Nepal', 'NL': 'Netherlands', 'NC': 'New Caledonia', 'NZ': 'New Zealand', 'NI': 'Nicaragua', 'NG': 'Nigeria', 'NU': 'Niue', 'NF': 'Norfolk Island', 'MP': 'Northern Mariana Islands', 'NO': 'Norway', 'OM': 'Oman', 'PK': 'Pakistan', 'PW': 'Palau', 'PS': 'Palestine, State of', 'PA': 'Panama', 'PG': 'Papua New Guinea', 'PY': 'Paraguay', 'PE': 'Peru', 'PH': 'Philippines', 'PN': 'Pitcairn', 'PL': 'Poland', 'PT': 'Portugal', 'PR': 'Puerto Rico', 'QA': 'Qatar', 'MK': 'Republic of North Macedonia', 'RO': 'Romania', 'RU': 'Russian Federation', 'RW': 'Rwanda', 'RE': 'Réunion', 'BL': 'Saint Barthélemy', 'SH': 'Saint Helena, Ascension and Tristan da Cunha', 'KN': 'Saint Kitts and Nevis', 'LC': 'Saint Lucia', 'MF': 'Saint Martin', 'PM': 'Saint Pierre and Miquelon', 'VC': 'Saint Vincent and the Grenadines', 'WS': 'Samoa', 'SM': 'San Marino', 'ST': 'Sao Tome and Principe', 'SA': 'Saudi Arabia', 'SN': 'Senegal', 'RS': 'Serbia', 'SC': 'Seychelles', 'SL': 'Sierra Leone', 'SG': 'Singapore', 'SX': 'Sint Maarten', 'SK': 'Slovakia', 'SI': 'Slovenia', 'SB': 'Solomon Islands', 'SO': 'Somalia', 'ZA': 'South Africa', 'GS': 'South Georgia and the South Sandwich Islands', 'SS': 'South Sudan', 'ES': 'Spain', 'LK': 'Sri Lanka', 'SD': 'Sudan', 'SR': 'Suriname', 'SJ': 'Svalbard and Jan Mayen', 'SE': 'Sweden', 'CH': 'Switzerland', 'SY': 'Syrian Arab Republic', 'TW': 'Taiwan', 'TJ': 'Tajikistan', 'TZ': 'Tanzania, United Republic of', 'TH': 'Thailand', 'TL': 'Timor-Leste', 'TG': 'Togo', 'TK': 'Tokelau', 'TO': 'Tonga', 'TT': 'Trinidad and Tobago', 'TN': 'Tunisia', 'TR': 'Turkey', 'TM': 'Turkmenistan', 'TC': 'Turks and Caicos Islands', 'TV': 'Tuvalu', 'UG': 'Uganda', 'UA': 'Ukraine', 'AE': 'United Arab Emirates (the)', 'UM': 'United States Minor Outlying Islands', 'US': 'United States of America', 'UY': 'Uruguay', 'UZ': 'Uzbekistan', 'VU': 'Vanuatu', 'VN': 'Viet Nam', 'VG': 'Virgin Islands', 'VI': 'Virgin Islands', 'WF': 'Wallis and Futuna', 'EH': 'Western Sahara', 'YE': 'Yemen', 'ZM': 'Zambia', 'ZW': 'Zimbabwe', 'AX': 'Åland Islands'}
global file_name
file_name = ''
global out_file
out_file = ''
global single_ip
single_ip = ''
global country_code
country_filter = []

def save_out(data):
    with open(f'{out_file}', 'w') as save_file:
        save_file.write(f'|--------------------------------------------|\n')
        save_file.write(f'|\t\tIP Addresses\t\t     |\n')
        save_file.write(f'|--------------------------------------------|\n')
        for key in data:
            save_file.write(f'\n{cc.get(key)}({key}):\n')
            for item in data.get(key):
                save_file.write(f'\t{item}\n')
        save_file.close()

def build_results():
    if len(single_ip) > 0:
        country_code = ''
        ip = single_ip
        resp = session.get(f'https://ipgeolocation.io/ip-location/{ip}')
        output = resp.text.split('\n')
        for out in range(len(output)):
            if output[out].__contains__("Country Code (ISO 3166-1 alpha-2)"):
                country_code = output[out + 1].split(">")[1].split("<")[0]
        print(f"{cc.get(country_code)} ({country_code}): {ip}")

    if len(file_name) > 0:
        # Multiple IPs from file
        ip_addr = get_file_contents(file_name)
        results = {}
        for ip in ip_addr:
            ip = ip.strip('\n')
            resp = session.get(f'https://ipgeolocation.io/ip-location/{ip}')
            output = resp.text.split('\n')

            for out in range(len(output)):
                if output[out].__contains__("Country Code (ISO 3166-1 alpha-2)"):
                    country_code = output[out + 1].split(">")[1].split("<")[0]
                    if results.get(country_code) is None:
                        ip_list = [ip]
                        results[country_code] = ip_list
                    else:
                        ip_list = results.get(country_code)
                        ip_list.append(ip)
                        results[country_code] = ip_list
        if len(out_file) > 0:
            save_out(results)
        else:
            for key in results.keys():
                print(f"{cc.get(key)}-({key}): {results.get(key)}")

def get_file_contents(file_name):
    with open(f'{file_name}', 'r') as file:
        contents = file.readlines()
        file.close()
    return contents

if __name__ == '__main__':

    msg = textwrap.dedent("""
    IP Country Locator
    
    If you are country locating a list of ip addresses
    from a file then format them accordingly:
    \t192.168.1.1
    \t192.168.1.2
    \t192.168.1.3
    \t192.168.1.4
    """)
    parser = argparse.ArgumentParser(description=msg, usage="%(prog)s [options]", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-iS', metavar='\b, --ip-single', dest="single_ip", type=str, help='\nLocate a single ip address')
    parser.add_argument('-iF', metavar='\b, --ip-file', dest="file_name", type=str, help='\nLocate file of ip addresses')
    #parser.add_argument('-fCC',metavar='\b, --filter-country',dest="country_filter", type=str, help='Filter results by country code')
    parser.add_argument('-oF',metavar='\b, --output-file', dest="out_file", type=str, help='\nOutput file and file location')
    #parser.print_help()
    args = parser.parse_args()
    argv = vars(args)

    for key in argv.keys():
        if key == "single_ip" and argv.get(key) is not None:
            single_ip = argv.get("single_ip")
        if key == "file_name" and argv.get(key) is not None:
            file_name = argv.get("file_name")
        if key == "out_file" and argv.get(key) is not None:
            out_file = argv.get("out_file")

    build_results()



