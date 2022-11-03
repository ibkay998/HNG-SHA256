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
    writer.writerow(["TEAM NAMES","Series Number","Filename","Name","Description","Gender","attributes","UUID"])
    CSV_FILE = 'csv/{}'.format(item)
    #reading the input file
    with open(CSV_FILE, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        data = [item for item in csv_reader]
        for row in data:
            serial_number = row[1]
            file_name = row[2]
            name = row[3]
            description = row[4]
            gender = row[5]
            attributes=row[6]
            attr_pair =attributes.split(";")
            hair = attr_pair[0]
            hair_value = hair.split(":")[1].strip()
            eyes = attr_pair[1]
            eyes_value = eyes.split(":")[1].strip()
            teeth = attr_pair[2]
            teeth_value = teeth.split(":")[1].strip()
            clothing = attr_pair[3]
            clothing_value = clothing.split(":")[1].strip()
            accesories = attr_pair[4]
            accesories_value = accesories.split(":")[1].strip()
            expression = attr_pair[5]
            expression_value = expression.split(":")[1].strip()
            strengths = attr_pair[6]
            strengths_value = strengths.split(":")[1].strip()
            weakness = attr_pair[7]
            weakness_value = weakness.split(":")
            uuid = row[7]
            def sample(trait_type,value):
                return {"trait_type":trait_type,"value":value}
            attr = []
            all = [["gender",gender],["hair",hair_value],["eyes",eyes_value],["teeth",teeth_value],["clothing",clothing_value],["accessories",accesories_value],["expression",expression_value],["strengths",strengths_value],["weakness",weakness_value]]
            for item in all:
                if item[1] != "none":
                    attr.append(sample(item[0],item[1]))
            
            Chip_007 = {
                'format' : 'CHIP-0007',
                'id' : uuid,
                'name' : file_name,
                'description' : description,
                'minting_tool' : 'SuperMinter/2.5.2',
                'sensitive_content' : False,
                'series_number' :serial_number,
                'series_total' : data[-1][0],
                "attributes": attr,

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
            row.append(f'{hashString}')
            writer.writerow(row)
    f.close()




