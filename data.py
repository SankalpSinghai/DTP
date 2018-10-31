import xmltodict
import xml.etree.ElementTree as ET 
import json                        #json file is target file
from datetime import datetime
from datetime import timedelta
import time                        #calculate time of execution
start=time.time()                  
now = datetime.now().date()
#print(now)
EndDate = now + timedelta(days=539) #540 days from current date
#print(EndDate)
reservations=[]
try:
	tree = ET.parse('C:\\Users\\SankalpSinghai\\Desktop\\DTP\\source.xml')
	root = tree.getroot()
except:
	print("source file not found")
	exit(2)

#to retrieve start date and end date 
for item in root.findall('bookingUpdateDetails'):
	for items in item.findall('reservations'):
		for reservation in items.findall('reservation'):
			beginDate = reservation.find('beginDate').text
			beginDate = datetime.strptime(beginDate, "%Y-%m-%d").date()
			reservations.append(beginDate)
			#print(beginDate)
			endDate = reservation.find('endDate').text
			endDate = datetime.strptime(endDate, "%Y-%m-%d").date()
			#print(endDate)			
			reservations.append(endDate)
reservations=sorted(reservations)
print(reservations)


target_json={"listing_id":root[1][1].text, "operations":[ ]}                           #creating json file

for i in range(len(reservations)-1):
    if(now>reservations[i+1]):
        del reservations[i,i+2]
    elif(now>reservations[i] or now<reservations[i+1] and EndDate<reservations[i]):
        reservations[i]=now
        target_json["operations"].append({"dates":str(reservations[i])+ ':' +str(reservations[i+1]),"availability":"unavailable"})
    elif(EndDate<reservations[i] or EndDate<reservations[i+1]):
        continue
    else:
        target_json["operations"].append({"dates":str(reservations[i])+ ':' +str(reservations[i+1]),"availability":"unavailable"})
print(target_json)
try:
    with open('C:\\Users\\SankalpSinghai\\Desktop\\DTP\\target.json', 'w') as file:
        json.dump(target_json,file)
except:
	print("target file not found")
	exit(2)

end=time.time()
print("execution time is"+str(end-start))
