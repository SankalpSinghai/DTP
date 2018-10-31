import xml.etree.ElementTree as ET
import datetime
import timedelta
import pandas as pd
import sys

now = datetime.date.today()                   #current date          
#print (now)
EndDate = now + datetime.timedelta(days=539)  #end date after 540 days from current date
#print (EndDate)
valid_range = []                       
store = pd.date_range(now, periods=539)       #all 540 days stored in list. 
valid_range.append(store)
#print(valid_range)

def main():

    data = ET.parse('source.xml')
    root = data.getroot()
   # print(root)
    for listingID in root.iter('listingExternalId'):  #getting listingId
        print(listingID.text)
        listingId = listingID.text
   
    begin_date = [] 
    end_date = []
    status = []
    for b_reservation in root.iter('beginDate'):      #list containing beginDate 
       # print(b_reservation.text)
        begin_date.append(b_reservation.text)
    print(begin_date)
    a = begin_date[:1]
    for e_reservation in root.iter('endDate'):         #list containing endDate
        #print(e_reservation.text)
        end_date.append(e_reservation.text)
    print(end_date)

    for Status in root.iter('reservationStatus'):
        status.append(Status.text)
    #print(status)    
    reservations = []
    for date in zip(begin_date, end_date, status):             #zipping beginDate,endDate and status as tuple
        reservations.append(date)
    #print(reservations)
    

    
    
    Output = []
    
    for item1 in reservations:
        for item2 in end_date:
            if item2 in item1:
                print (item1)
                
                
##                for item in item1:
##                 
##                    if item in valid_range:
##                       
##                        print('default')
##                    else:
##                        print('unavailable')
##        




if __name__ == "__main__":
        main();
