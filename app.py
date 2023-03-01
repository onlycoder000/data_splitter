import csv


link_count=0
limiter=1000
dir_path = './export'
with open('import.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        d=int((link_count - (link_count % limiter)) / limiter)
        
        with open('export/'+str(d)+'.csv', mode='a') as open_file:
            open_writer = csv.writer(open_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            open_writer.writerow(row)
        print(d)

        link_count+=1