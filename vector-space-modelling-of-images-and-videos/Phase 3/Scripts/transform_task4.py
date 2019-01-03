import csv
import os
import xml.etree.ElementTree
import time

from pymongo import MongoClient


def main():
    start = time.time()
    connection = MongoClient('localhost', 27017)
    db = connection.MWDB_devset

    collection = db.locations_images

    location_num_file = input("Enter devset_topics file path ")
    type(location_num_file)

    location_file = input("Enter directory ")
    type(location_file)
    # location_num_file = r"C:\Users\palla\OneDrive\Documents\MWDB\Phase 1 Project\devset\desctxt\desctxt\devset_topics.xml"

    loc_num_file = open(location_num_file, "r", encoding="utf-8")

    location_nums = []
    root = xml.etree.ElementTree.parse(loc_num_file).getroot()
    for item in root.findall('topic'):
        a = {}
        a['number'] = item.find('number').text
        a['title'] = item.find('title').text
        location_nums.append(a)

    # location_file = r"C:\Users\palla\OneDrive\Documents\MWDB\Phase 1 Project\devset\descvis\descvis\img"
    for name in os.listdir(location_file):

        with open(location_file + '\\' +name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                data = {}
                file_name = name.split()
                data['locationName'] = file_name[0]
                data['model'] = file_name[1].split(".")[0]
                for item in location_nums:
                    if data['locationName'] == item['title']:
                        data['number'] = int(item['number'].strip('\"'))
                details = {}
                details['image_id'] = row[0].strip('\"')
                val_list = []
                for item in range(1, len(row)):
                    val_list.append(float(row[item]))
                details['values'] = val_list
                data['details'] = details
                collection.insert_one(data)
                # print(data)
    end = time.time()
    print("Execution Time", end - start)


main()