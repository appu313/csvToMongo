import pandas as pd
import random
import string
from random import randint
from collections import OrderedDict 
import bcrypt

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
    
def getHash(passwd):
	salt = bcrypt.gensalt()
	return bcrypt.hashpw(passwd, salt = bcrypt.gensalt())
	
def compareHash(passwd, hashed):
	return bcrypt.checkpw(passwd, hashed)

name_dict = OrderedDict()


name_dict['first_name']= []
name_dict['last_name']= []
name_dict['mobile']=[]
name_dict['email']=[]
name_dict['password']=[]
name_dict['tokens']=""
name_dict['otp']=[]
name_dict['ethAcct']=[]
name_dict['otpStartTime']=[]

#strVal = b's$cret12'
#hash = getHash(strVal )
#compareHash("appu",hash)


for i in range(50):
	#new_row = {}
	name_dict['first_name'].append(randomString(5))
	name_dict['last_name'] .append(randomString(7))
	name_dict['mobile'] .append("+91" + str(random_with_N_digits(10)))
	name_dict['email'] .append(randomString(7) + "@gmail.com")
	name_dict['password'] .append(randomString(7))
	#name_dict['tokens'] .append( "")
	name_dict['otp'] .append("0")
	name_dict['ethAcct'] .append("0")
	name_dict['otpStartTime'] .append("0")

df = pd.DataFrame(name_dict)
print (df)

df.to_csv('file_name.csv',index=False)
'''
hashed = getHash('appu'.encode('utf'))
print(hashed)
print(compareHash('appu'.encode('utf'), hashed))'''
