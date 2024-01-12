import requests
import datetime

username="rajmehta"
tocken="rrrrrrrrrrrrrrrrrr"
graphid="graph1"



P_ENDPOINT="https://pixe.la/v1/users"
user_para={
    "token":tocken,
    "username":username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"


}




graph_endpoint=f"{P_ENDPOINT}/{username}/graphs"

g_para={
    "id":graphid,
    "name":"Coding Graph",
    "unit":"hours",
    "type":"int",
    "color":"ajisai"

}

header={
    "X-USER-TOKEN":tocken
}
today=datetime.datetime(year=2023,month=12,day=27)
date=today.strftime("%Y%m%d")
print(date)

pixel_endpoint=f"{P_ENDPOINT}/{username}/graphs/{graphid}"

pixel_para={
    "date":input("Enter a date in yyyymmdd form:"),
    "quantity":input("Enter the number of hours:"),


}
response=requests.post(url=pixel_endpoint,json=pixel_para,headers=header)
print(response.text)

u_endpoint = f"{P_ENDPOINT}/{username}/graphs/{graphid}/{date}"

u_para={
    "quantity":"3"
}

response = requests.put(url=u_endpoint,json=u_para,headers=header)
print(response.text)

