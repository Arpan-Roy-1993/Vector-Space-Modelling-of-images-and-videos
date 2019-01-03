from pymongo import MongoClient


def main():
    connection = MongoClient('localhost', 27017)
    db = connection.MWDB_devset

    collection = db.images
    pathInput = input("Enter the file path to be stored to the database ")
    type(pathInput)

    file = open(pathInput, "r", encoding="utf-8")
    lines = file.readlines()
    file.close()
    count = 0
    for line in lines:
        data = {}
        chunks = line.split()
        data['imageID'] = chunks[0].replace(u'\ufeff', '')
        n = 4
        a = []
        count += 1
        for i in range(1, len(chunks), n):
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