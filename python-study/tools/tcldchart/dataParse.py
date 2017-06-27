#encoding:utf8
import json
import datetime

class Debug(object):
    def trace(self, msg):
        print 'trace:',msg
debug=Debug()

# 分析分段模式数据
def func1():
    fo=open('47_20160321140141_v5td.json')
    strJson=fo.read(-1)
    fo.close()
    pmData=json.loads(strJson, encoding='utf8')
    debug.trace(['period_glucose len:', len(pmData['period_glucose'])])
    debug.trace(['period_glucose len:', len(pmData['period_glucose'][1]['sensor_glucose'])])
    zaoData=pmData['period_glucose'][0]['sensor_glucose']
    #wuData=pmData['period_glucose'][1]['sensor_glucose']
    for dayData in zaoData:
        # 每个阶段还有3个小阶段。
        debug.trace(['==========day num:', len(dayData)])
        #debug.trace(dayData[2])
        for periodData in dayData:
            for item in periodData:
                item[0]=datetime.datetime.fromtimestamp(item[0]).strftime('%Y-%m-%d %H:%M:%S')
                debug.trace(item)
    #a=[None,1,2]
    #json.dumps(a, )
    #strA=json.dumps(a, ensure_ascii=False)
    #debug.trace(strA)

def func2():
    fo=open('pm-rv.json')
    strJson=fo.read(-1)
    fo.close()
    rv=json.loads(strJson, encoding='utf8')
    
    dn=5
    for i in range(0,8):
        sg=[]
        print '\r\n\r\n period index %d'%i
        #i=2  # 阶段
        for j in range(0, dn):
            tmpSG=rv[i*dn+j]
            sg += tmpSG
            for item in tmpSG:
                item[0]=datetime.datetime.fromtimestamp(item[0]).strftime('%Y-%m-%d %H:%M:%S')
                debug.trace(item)
    
# 传感器每日的数据。
def func3():
    fo=open('03-25.json')
    strJson=fo.read(-1)
    fo.close()
    sgData=json.loads(strJson, encoding='utf8')
    #debug.trace(['period_glucose len:', len(pmData['period_glucose'])])
    #debug.trace(['period_glucose len:', len(pmData['period_glucose'][1]['sensor_glucose'])])
    #zaoData=pmData['period_glucose'][0]['sensor_glucose']
    for item in sgData:
        #debug.trace(len(dayData))
        #debug.trace(dayData[2])
        #for item in dayData[2]:
        
        item[1]=datetime.datetime.fromtimestamp(item[1]).strftime('%Y-%m-%d %H:%M:%S')
        debug.trace(item)
        
# 
def func4():
    # 47-20160316135604-298.json
    fo=open('47-20160316141814-990.json')
    strJson=fo.read(-1)
    fo.close()
    sgData=json.loads(strJson, encoding='utf8')
    debug.trace(['sgData len:', len(sgData)])
    #pn=len()
    #for pdata in sgData:
    #    debug.trace(['day num:', len(pdata)])
    #    for ddata in pdata:
    #        debug.trace(['sg num:', len(ddata)])
    #sgList=sgData[1][0]
    #for item in sgList:
    #    item[0]=datetime.datetime.fromtimestamp(item[0]).strftime('%Y-%m-%d %H:%M:%S')
    #    debug.trace(item)
    #for pdata in sgData:
    #    debug.trace(['data num:', len(pdata)])
    # 
    for d in range(5):
        sgList=sgData[d*9+3]
        for item in sgList:
            item[0]=datetime.datetime.fromtimestamp(item[0]).strftime('%Y-%m-%d %H:%M:%S')
            debug.trace(item)
        debug.trace('============')


# 分析分时模式的统计数据。
def func5():
    # 47-20160316135604-298.json
    fo=open('47-20160321105220-397.json')
    strJson=fo.read(-1)
    fo.close()
    sgData=json.loads(strJson, encoding='utf8')
    debug.trace(['sgData len:', len(sgData)])
    #pn=len()
    # 
    vlist=[]
    for item in sgData[10]:
        item[0]=datetime.datetime.fromtimestamp(item[0]).strftime('%Y-%m-%d %H:%M:%S')
        if item[4]=='C':
            vlist.append(item[1])
        #debug.trace(item)
        #debug.trace('============')
    #
    vlist.sort()
    debug.trace(['vlist:', vlist])
    size=len(vlist)
    q1=vlist[size/4]
    q3=vlist[size*3/4]
    debug.trace(['q1,q3:', q1, q3])

# char_pm.js 早餐绘图的数据    
def func6():
     # 47-20160316135604-298.json
    fo=open('chart_pm.json')
    strJson=fo.read(-1)
    fo.close()
    sgData=json.loads(strJson, encoding='utf8')
    debug.trace(['sgData len:', len(sgData)])
    for dayData in sgData:
        for periodData in dayData:
            for item in periodData['sgv']:
                item[0]=datetime.datetime.fromtimestamp(item[0]).strftime('%Y-%m-%d %H:%M:%S')
                debug.trace(item)

# 风险指数数据。
def func7():
     # 47-20160316135604-298.json
    fo=open('risk-data.json')
    strJson=fo.read(-1)
    fo.close()
    riskData=json.loads(strJson, encoding='utf8')
    debug.trace(['riskData len:', len(riskData)])
    lowRisk,hishRisk,dataNum=riskData[:]
    debug.trace(['lowRisk len:', len(lowRisk)])
    debug.trace(['hishRisk len:', len(hishRisk)])
    debug.trace(['dataNum len:', len(dataNum)])
    # 
    lowList=[]
    highList=[]
    for i in range(0,720):
        #lowRisk[i]=[i,lowRisk[i]/dataNum[i]]
        #hishRisk[i]=[i,hishRisk[i]/dataNum[i]]
        if lowRisk[i]/dataNum[i]>1.8:lowList.append(i)
        if hishRisk[i]/dataNum[i]>1.8:highList.append(i)
    debug.trace(['lowList, highList:', lowList, highList])
 
# 3-17号SG数据
def func7():
     # 47-20160316135604-298.json
    fo=open('4-10.json')
    strJson=fo.read(-1)
    fo.close()
    sgData=json.loads(strJson, encoding='utf8')
    for item in sgData:
        item[1]=datetime.datetime.fromtimestamp(item[1]).strftime('%Y-%m-%d %H:%M:%S')
        debug.trace(['item:', item])
        
# 3-17号SG数据
def func8():
     # 47-20160316135604-298.json
    fo=open('47-PM-1.json')
    strJson=fo.read(-1)
    fo.close()
    sgData=json.loads(strJson, encoding='utf8')
    vlist1=[]
    for psg in sgData:
        for item in psg:
            item[0]=datetime.datetime.fromtimestamp(item[0]).strftime('%Y-%m-%d %H:%M:%S')
            debug.trace(['item:', item])
            vlist1.append(item[1])
        debug.trace(['++++++++++++++++++++++++++'])
    
    debug.trace(['============='])    
    fo=open('47-PM-2.json')
    strJson=fo.read(-1)
    fo.close()
    sgData=json.loads(strJson, encoding='utf8')
    vlist2=[]
    for psg in sgData:
        for item in psg:
            item[0]=datetime.datetime.fromtimestamp(item[0]).strftime('%Y-%m-%d %H:%M:%S')
            debug.trace(['item:', item])
            vlist2.append(item[1])
        debug.trace(['++++++++++++++++++++++++++'])
    # 
    #debug.trace(['vlist:', len(vlist1), len(vlist2), vlist1, vlist2])
        
# 分析分时模式的统计数据。
def func9():
    # 47-20160316135604-298.json
    fo=open('47-20160321105220-397.json')
    strJson=fo.read(-1)
    fo.close()
    sgData=json.loads(strJson, encoding='utf8')
    debug.trace(['sgData len:', len(sgData)])
    #pn=len()
    # 
    vlist=[]
    for item in sgData[13]:
        #for item in hourData:
        item[0]=datetime.datetime.fromtimestamp(item[0]).strftime('%Y-%m-%d %H:%M:%S')
        if item[4]=='C':
            vlist.append(item[1])
        debug.trace(item)
    debug.trace(['vlist:', vlist])
    debug.trace('============')

# 
if __name__ == '__main__':
    func9()
    