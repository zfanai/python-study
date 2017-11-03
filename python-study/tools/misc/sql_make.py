#encoding:utf8

def func1():
    lines=[]
    with open('user.txt', 'rb') as fo:
        lines=fo.readlines()
    def get_uid(x):
        s=x.split()
        try:
            return int(s[0])
        except Exception,e:
            pass
        return None
    uids=map(lambda x: get_uid(x), lines)
    uids=filter(lambda x:x, uids)
    print 'uids:', uids 
    
    tpl='''
-- %(uid)s
select * from pdm_sg where user_id=%(uid)s order by pdm_data_id, time;
select * from pdm_basal where user_id=%(uid)s order by pdm_data_id, time;
select * from pdm_bolus where user_id=%(uid)s order by pdm_data_id,time;
    '''

    tpl = '''
    -- %(uid)s
    select * from sensor_glucose_record where user_id=%(uid)s order by time;
    select * from basal_record where user_id=%(uid)s order by time;
    select * from bolus_record where user_id=%(uid)s order by time;
        '''
    
    rv=map(lambda x:tpl%{'uid':x}, uids)
    print rv[0]
    sql_str=''.join(rv)
    
    with open('out.sql', 'wb') as fo:
        fo.write(sql_str)
    
if __name__=='__main__':
    func1()