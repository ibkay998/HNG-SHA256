import os
import csv, hashlib, json

#get the current working directory and add the path csv
path = os.getcwd() +'\\csv'
#get all csvs in path
all_csv = os.listdir(path)

for item in all_csv:
    #removes the .csv from the file name
    new_item = item.split('.')[0]
    #the output file
    OUTPUT_FILE = 'output/{}.output.csv'.format(new_item)
    #code to write into the output file
    f = open(OUTPUT_FILE, 'w')
    writer = csv.writer(f)
    writer.writerow(['Series Number', 'Filename', 'Descriptor','Gender','UUID', 'Hash'])
    CSV_FILE = 'csv/{}'.format(item)
    #reading the input file
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
                'minting_tool' : 'SuperMinter/2.5.2',
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




