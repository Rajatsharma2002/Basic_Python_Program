import re

str='''
hello how are you my email is you@gamil.com what about yours 
mine is me@gmail.com 
wow what a nice email you have . ohh that's nothing my friends has 
more awesome emails like yo@gamil.com and sly@gamil.com
now a days all uses gmail id no one uses any other email like 
previously people uses apun@yahoo.com type of mails 
no that's not true some people still use that kind of mails
like my father does hello@yahoo.com
and some emails also have .in characters like sdu@uni.in
'''

# list=re.finditer(r'\w+@',str)
# list=re.findall(r'\w+@+\S+\w',str)

patt=re.compile(r'\w+@+\S+\w')
list=patt.findall(str)

file=open("Email_collector","a")
j=1
for i in list:
    file.write(f"Email {j} : {i}\n")
    j=j+1
file.close()

f=open("Email_collector","r")
content=f.read()
print(content)




