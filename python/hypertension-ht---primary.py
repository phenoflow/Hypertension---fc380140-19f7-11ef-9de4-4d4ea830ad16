# Evengelos Kontopantelis, David Reeves, Jose M Valderas, Stephen Campbell, Tim Doran, 2024.

import sys, csv, re

codes = [{"code":"9OIA.11","system":"readv2"},{"code":"9OIA.00","system":"readv2"},{"code":"G20z.11","system":"readv2"},{"code":"G20..11","system":"readv2"},{"code":"6629.00","system":"readv2"},{"code":"4419H","system":"readv2"},{"code":"401 NC","system":"readv2"},{"code":"3053HT","system":"readv2"},{"code":"4360B","system":"readv2"},{"code":"401 LB","system":"readv2"},{"code":"4120BD","system":"readv2"},{"code":"4380HP","system":"readv2"},{"code":"401 AC","system":"readv2"},{"code":"401 AT","system":"readv2"},{"code":"401 AR","system":"readv2"},{"code":"401 DC","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hypertension-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hypertension-ht---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hypertension-ht---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hypertension-ht---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
