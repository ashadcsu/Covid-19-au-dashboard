import pandas as pd
import io
import requests
url="https://www.iedcr.gov.bd/website/images/files/nCoV/Case_dist_15_May_upload.pdf"
s=requests.get(url).content
c=pd.read_pdf(io.StringIO(s.decode('utf-8')))
print(c)