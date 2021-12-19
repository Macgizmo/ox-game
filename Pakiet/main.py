import datetime
d1 = datetime.date(2019,8,15)
print(d1)
dh1 = datetime.datetime (2019,8,14,5,12,10)
print(dh1)
#%%
import datetime
x1 = datetime.date(2019,1,1)
x2 = datetime.date(2021,8,9)
x3=x2-x1
print(x3)
#%%
import datetime
x1 = datetime.date(1980,2,10)
x2 = datetime.date(2021,12,19)
x4 = x2-x1
print(x4)
# %%
import datetime
x1 = datetime.datetime(2021,12,31,1,1,12)
x2 = datetime.datetime(2021,12,19,3,5,9)
x5 = (x1-x2)
print(x5)
# %%
import datetime
x7=datetime.datetime(2021,12,19)
print(x7 + datetime.timedelta(days=75))
# %%
