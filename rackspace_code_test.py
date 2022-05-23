#Rackspace Home Assignment
'''
Assignment: Write a Python program that returns information about the world time zones. The program should meet the below requirements:

Requirements:

- The code should be written as if you intended to put it into production in a critical environment. Please use all tooling and process you would in day-to-day work.
- The program should download a list of all commonly used time zones in JSON format from: https://raw.githubusercontent.com/dmfilipenko/timezones.json/master/timezones.json
- By default the program should parse information from the above JSON and return all time zones in a user-friendly format
- The program should also accept two optional arguments
  --match: If specified, display only information about time zones whose values match the string supplied to this argument
  --offset: If specified, the program will only display time zones matching this offset. Note that this should work for time zones ahead of and behind UTC!
'''


import argparse
import requests

def ret(temp_l):
    if temp_l:
        return '\n'.join(temp_l)
    else:
        return 'No Match Found'

def get_tz_info():
    url = 'https://raw.githubusercontent.com/dmfilipenko/timezones.json/master/timezones.json'
    try:
        resp = requests.get(url)
        return resp.json()
    except Exception as e:
        print(e)

def format_tz_info(tz_data):
    temp_l = []
    for date in tz_data:
        date_tz_str = 'Timezone: {} with Abbreviations: {} with Offset: {} in DST: {} Region: {} and Locations {}'.format(date['value'],date['abbr'],date['offset'],date['isdst'],date['text'],(','.join(date['utc'])))
        temp_l.append(date_tz_str)
    return ret(temp_l)

def match_tz(tz_data,match):
    # Match the abbr else match the value. User can send a abbr or partial value.
    # If passing the value, the string length should be > 4
    temp_l = []
    for date in tz_data:
        if len(match) <= 4:
            if match.lower() == date['abbr'].lower():
                temp_l.append('Timezone: {} and Abbr: {}'.format(date['value'], date['abbr']))
        else:
            if match.lower() in date['value'].lower():
                temp_l.append('Timezone: {} and Abbr: {}'.format(date['value'],date['abbr']))
    return ret(temp_l)

def match_offset(tz_data,offset):
    #Match exact offset and return the matching TZs
    temp_l = []
    for date in tz_data:
        if float(offset) == date['offset']:
            temp_l.append('Timezone: {}, Abbr: {} and Offset: {} '.format(date['value'],date['abbr'],date['offset']))
    return ret(temp_l)

def main():
    parser = argparse.ArgumentParser(description='run python <code> for normal execution \n Run python <code> -m <tz_name> to get specific tz \n Run python <code> -m <offset value> to get matching tz \n For a multiple string input python <code> -m="<offset value> to get matching tz"')
    parser.add_argument("-m","--match", help="Match a TimeZone")
    parser.add_argument("-o", "--offset", help="Get specific offset timezone details")
    args = parser.parse_args()
    tz_data = get_tz_info()

    #Usage: if match or offset args are set, the program will return matching TZs. Else return all TZ info.
    if tz_data:
        if args.match:
            print(match_tz(tz_data,args.match))
        elif args.offset:
            print(match_offset(tz_data,args.offset))
        else:
            print(format_tz_info(tz_data))
    else:
        print("TZ Data not found")

if __name__ == "__main__":
    main()
