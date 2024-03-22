import pandas as pd 
import numpy as np

def generateLinkFromCsv(input_csv,column_num,output_file_txt=None,country_code=None):
    __doc__="This function takes in a csv, optional output text file and country code and returns the directly clickable whatsapp directing links"
    df = pd.read_csv(input_csv)
    array = np.array(df.iloc[:, column_num])
    row = len(array)
    if output_file_txt is None:
        output_file_txt = 'output.txt'
    if country_code is None:
        country_code = '91'
    with open(output_file_txt,"w") as file:
        for i in range(row):
            whatsapp_link = f'https://wa.me/{country_code}' + str(array[i])
            print(whatsapp_link)
            file.write(whatsapp_link + '\n')
    


def generateLinkFromNumber(contact_no,country_code=None):
    if country_code is None:
        country_code = '91'
    whatsapp_link = f'https://wa.me/{country_code}' + str(contact_no)
    print(whatsapp_link)
