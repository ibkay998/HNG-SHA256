import os
import csv, hashlib, json

path = os.getcwd() +'\\csv'
ans = os.listdir(path)

if len(ans) == 0:
    print("input your csv in the csv folder")

for item in ans:
    new_item = item.split('.')[0]
    OUTPUT_FILE = 'output/{}.output.csv'.format(new_item)
    f = open(OUTPUT_FILE, 'w')
    writer = csv.writer(f)
    writer.writerow(['Series Number', 'Filename', 'Descriptor','Gender','UUID', 'Hash'])
    CSV_FILE = 'csv/{}'.format(item)
    with open(CSV_FILE, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        data = [item for item in csv_reader]
        for column in data:
            serial_number = column[0]
            file_name = column[1]
            descriptor = column[2]
            gender = column[3]
            uuid = column[4]
            Chip_007 = {
                'format' : 'CHIP-0007',
                'id' : uuid,
                'name' : file_name,
                'description' : descriptor,
                'minting_tool' : 'Matanmi SuperMint',
                'sensitive_content' : False,
                'series_number' :serial_number,
                'series_total' : data[-1][0],
                "attributes": [
                        {
                            "trait_type": "gender",
                            "value": gender
                        }],
                'collection' : {
                    'name' : file_name,
                    'id' : uuid
                }
            }
            json_file = json.dumps(Chip_007, indent=4)
            with open(f'json/{file_name}.json', 'w') as output:
                output.write(json_file)
            output.close()
            filename = f'json/{file_name}.json'
            sha256_hash = hashlib.sha256()
            with open(filename,"rb") as f:
                for byte_block in iter(lambda: f.read(4096),b""):
                    sha256_hash.update(byte_block)
            hashString = sha256_hash.hexdigest()
            column.append(f'{hashString}')
            writer.writerow(column)
    f.close()




