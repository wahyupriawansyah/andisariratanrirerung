import geometribob

def main():
	#s adalah persen
	#t adalah nilai 
	#v adalah harga barang
	s = 50
	t = 50
	v = 100000
	persen = geometribob.menghitungpersen(s,t)
	
	print("\nMenghitung persen ")
	print("\nhasil : ",persen)
	
	discount = geometribob.menghitungdiscoun(s,v)
	
	print("\nmenghitung harga dari discount")
	print("\nHasil : ",discount)
	
	#mengitung trapesium
	a =10
	b =40
	t =60
	
	trapesium = geometribob.menghitungtrapesium(a,b,t)
	print("\nMenghitung luas Trapesium ")
	print("hasil : ",trapesium)
	

	 
if __name__=="__main__":
	main()
