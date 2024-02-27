import requests
base_url="https://newsapi.org/v2/everything?"
access_key=input("Enter the access key... ")
query=input("Enter the news topic... ")
from_date=input("Enter the date in YY-DD-MM format... ")
sort_by=input("The popularity of topic... ")
def news(b,q,f,s,a):
  url= b+"q="+q+"&from="+f+"&sort_By="+s+"&apiKey="+a
  response=requests.get(url)
  data=response.json()
  if response.status_code != 200 :
    print(f"ERROR {response.status_code}")
  else:
    print(data)
news(base_url,query,from_date,sort_by,access_key)
