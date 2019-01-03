from pymongo import MongoClient

import xml.etree.ElementTree

def main():
    connection = MongoClient('localhost', 27017)
    db = connection.MWDB_devset

    collection = db.locations
    location_num_file = input("Enter devset_topics file path ")
    type(location_num_file)

    location_file = input("Enter devset_textTermsPerPOI.wFolderNames file path ")
    type(location_file)
    loc_num_file = open(location_num_file, "r", encoding="utf-8")


    location_nums = []
    root = xml.etree.ElementTree.parse(loc_num_file).getroot()
    for item in root.findall('topic'):
        a = {}
        a['number'] = item.find('number').text
        a['title'] = item.find('title').text
        location_nums.append(a)


    file = open(location_file, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    count = 0
    for line in lines:
        data = {}
        split_into_two = line.split('\"', 1)
        data['locationName'] = split_into_two[0].split(" ", 1)[0]
        data['locationQuery'] = split_into_two[0].split(" ", 1)[1].rstrip()
        rest_of_line = split_into_two[1]
        n = 4
        a = []
        count += 1
        chunks = rest_of_line.split()
        for item in location_nums:
            # print(item)
            if data['locationName'] == item['title']:
                data['number'] = int(item['number'].strip('\"'))
        for i in range(0, len(chunks), n):
            details = {}
            details['term'] = chunks[i].strip('\"')
            details['TF'] = int(chunks[i+1].strip('\"'))
            details['DF'] = int(chunks[i+2].strip('\"'))
            details['TF-IDF'] = float(chunks[i+3].strip('\"'))
            a.append(details)
        data['details'] = a
        collection.insert_one(data)

    print(count)
main()