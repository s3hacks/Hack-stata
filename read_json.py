import json
import collections

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    'United States': 'US',
    'Mexico': 'MX',
}



#print a['location']

locations = {}
locations = collections.OrderedDict()
list_popular_x = [0] * 1000
list_popular_y = [0] * 1000

def get_json_line(number):
    a = open("file.json", "r").readlines()[number-1]
    a = json.loads(a)
    return a


def popularity(a):
   global locations
   for i,j in locations.items():
       locations[i] = 0
   for each in  a['data']['projectdata']:
    temp = [location for location in each['locations'] if not location == None]
    if temp ==[]:
        pass
    else:
        temp = temp[0].strip()
        temp = temp.split(",")
        for i,location in enumerate(temp):
            location = location.strip()
            if location in us_state_abbrev.keys():
                temp[i] = us_state_abbrev[location]
            else:
                temp[i] = location

        temp = ",".join(temp)
        temp = temp.strip()
        if (not temp in locations.keys() ):
            locations[temp] = 1
        else:
            locations[temp] = locations[temp] + 1

def  get_x_axis_popular():
    count = 0
    for i,j in locations.items():
        list_popular_x[count] = j;
        list_popular_y[count] = i;
        count = count + 1



a = get_json_line(1)
popularity(a)
get_x_axis_popular()

print locations
print list_popular_y
print list_popular_x
print a['name']






