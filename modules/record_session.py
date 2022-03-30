from write_csv import create_filename, save_data, read_serial, header
from scan_card import scan_card
import datetime

date = datetime.datetime.now()  #gets current date
datestring = date.strftime("%y%m%d%H%M%S")  #formats date

save_data(create_filename(scan_card(), datestring), header)