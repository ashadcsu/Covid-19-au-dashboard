import requests
import bs4
import sys

a=input('')

headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
login_data={
    'user_email' : a,
    'user_password' : '20519304',
    'loginuser': 'Sign In'
}
sys.stdout=open('output.txt','w')
Table=''
# res =requests.get('http://www.cuet.ac.bd/course_registration/')
# soup=bs4.BeautifulSoup(res.text,'lxml')
# hi=soup.select('input')

# print(hi[0])
Result=[]
with requests.Session() as s:
    url="http://www.cuet.ac.bd/course_registration/"
    r=s.get(url,headers=headers)
    r=s.post(url,data=login_data,headers=headers)
    r=s.get("http://www.cuet.ac.bd/course_registration/result_published.php",headers=headers)
    g=bs4.BeautifulSoup(r.text,'lxml')
    Table=g.table
    if Table is not None:
        row=Table.find_all('tr')
        for tr in row:
            td=tr.find_all('td')
            rw=[i.text for i in td]
            Result.append(rw)
    else:
        print("Wrong Password")

Result=Result[1:]
print(Result)
print(Table)