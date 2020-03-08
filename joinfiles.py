def joinfiles(file1,file2,outputfile):
	"合并两个文件后输出"

	list =[]

	a = open(file1)
	f=a.readline()
	while f:
		list.append(f)
		f=a.readline()
	a.close()


	b= open(file2)
	f= b.readline()
	while f:
		list.append(f)
		f=b.readline()
	b.close()
	

	s = ''
	c = open(outputfile,'w')
	c.write(s.join(list))
	c.close()

def joinfiles2(file1,file2,file3):
	list =[]

	a=open(file1)
	f=a.readlines()
	f[-1] = f[-1]+'\n'
	
	b=open(file2)
	f=f+b.readlines()

	c = open(file3,'w')
	c.write(''.join(f))
	c.close()

joinfiles('1.txt','2.txt','3.txt')
joinfiles2('1.txt','2.txt','3.txt')
