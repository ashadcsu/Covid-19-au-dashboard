from tabula import read_pdf
import sys

sys.stdout=open('output.txt','w')

data=read_pdf('https://www.iedcr.gov.bd/website/images/files/nCoV/Case_dist_15_May_upload.pdf',pages=1)
data=data[0]
data=data[data['District/City'].notnull()]
data=data.loc[:,['District/City','Total']]
print(data)

print(type(data))