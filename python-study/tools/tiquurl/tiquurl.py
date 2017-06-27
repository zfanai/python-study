#encoding:utf8
import re
import urllib

def trace(msg):
	print "trace:",msg

def geturl(cssfile):
	pass
	fo=open(cssfile)
	bfr=fo.readline()    # 读取一行的数据，包括行尾的回车符。
	imgurlli=[]
	while bfr!="":
		#trace(["readline:", bfr])
		bfr=bfr.strip()
		if len(bfr)<200:
			pass
			#
			#trace(["bfr:", bfr])
			rs="url\(\.\./images/.*\)"
			#rz=re.match(rs, bfr)
			rz=re.findall(rs, bfr)
			#if rz != None:
			if len(rz)!=0:
				#trace(["rz:",rz])
				pass
				for s in rz:
					imgurl=s[7:-1]
					#trace(["imgurl:",imgurl])
					if imgurl not in imgurlli:
						imgurlli.append(imgurl)
						trace(["imgurl:",imgurl])
					#
			#trace(["rz:",rz])
		#
		bfr=fo.readline()
	#
	fo.close()
	
	return imgurlli

def dlimgs(imgurlli):
	pass
	for imgurl in imgurlli:
		#trace(["imgurl:",imgurl])
		urlpre="http://pc.huochepiao.360.cn/"
		tmpurl=urlpre+imgurl
		trace(["tmpurl:",tmpurl])
		filename=imgurl
		#
		urllib.urlretrieve(tmpurl, filename)

if __name__ == "__main__":
	cssfile="index.min.css"
	imgurlli=geturl(cssfile)
	dlimgs(imgurlli)