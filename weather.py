import pandas as pd
path=r'C:\Users\DANG THANG\Documents\học python\pandas\weather_data.csv'
df=pd.read_csv(path)
#df['Date_Time']=pd.to_datetime(df.Date_Time) #Phân tách object thành string
#print(df)
#print(df.Date_Time.dt.month)#Lấy phần tử trong string Date_Time

#print(df.Date_Time)

'''df['Date_Time']=pd.to_datetime(df.Date_Time)
df['Date_Time_month']=df.Date_Time.dt.month
print(df)''' #biến đổi phần tử trong Date_time và xuất ra cột mới (Date_time_month)

'''df.sort_values(by='Temperature_C',inplace=True)
print(df)''' # Sắp xếp giá trị theo hướng tăng dần

'''df.drop(labels='Date_Time',axis=0,inplace=False)
print(df) #loại bỏ cột(1) theo chỉ định, nếu là dòng thì axis=0'''

'''df.dropna(subset="Date_Time",axis=1,inplace=True)
print(df)''' #loại bỏ dòng(0) hoặc cột(1) bị null số liệu

df.dropna(subset="Date_Time",inplace=True)
print(df.info())


