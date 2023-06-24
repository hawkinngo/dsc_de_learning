import os
import pandas as pd
import json
from connect_mongo import get_database


def mongo_import(file_name, file_path, db):
    name = file_name.split(".")[0]

    data = pd.read_csv(file_path, header=0)
    data_json = json.loads(data.to_json(orient="records"))

    collection = db[name]
    if collection in db.list_collection_names():
        collection.remove()
    collection.insert_many(data_json)


if __name__ == "__main__":
    db = get_database()["de-learning-db"]
    db_path = os.path.join(os.getcwd(), "temp db", "tmp")

    files = os.listdir(db_path)
    total_file = len(files)
    begin = total_file - int(round(total_file / 3, 0))

    for i in range(begin, total_file):
        file_name = files[i]
        file_path = os.path.join(db_path, file_name)
        print(file_name)
        mongo_import(file_name, file_path, db)
