use flaskdb;

-- select * from device_activate_record where uid=(select id from user where username='abcd55') and 
-- devicetype='jn' order by startTime desc limit 5;

-- select * from basal_record where user_id=(select id from user where username='abcd55') and 
-- (date(time)='2016-05-16' or date(end_time)='2016-05-16') and del_flag!='Y' order by time;
 
 select * from basal_record where user_id=(select id from user where username='abcd55') and 
 ((basal_record.end_time>='2016-05-16 00:00:00' and basal_record.time<'2016-05-16 09:50:43' and pump_sn='108000179') or (basal_record.end_time>='2016-05-16 09:50:51' and basal_record.time<'2016-05-16 14:55:29' and pump_sn='108000115') or (basal_record.end_time>='2016-05-16 14:55:36' and basal_record.time<'2016-05-17 00:00:00' and pump_sn='108000179'));
 
-- desc alarm_record;
-- select * from alarm_record where user_id=(select id from user where username='xfy22') and date(time)=curdate() and type='SA';
-- select * from calib_record where user_id=(select id from user where username='xfy22') and date(time)=curdate();
-- select * from device_activate_record where uid=(select id from user where username='xfy22') and devicetype='ty';

-- select * from calib_record limit 100;
-- select * from alarm_record order by time desc limit 1000;

-- desc json_create_record;
-- select count(*) from json_create_record;

-- select * from user order by created desc limit 5;

-- select * from security_code order by cdt desc limit 5;
-- desc bolus_record;

-- select * from bolus_record;
-- select * from bolus_record where type!='NBM'; 

-- alter table device_token add column del_flag varchar(1);
-- desc device_token;

-- alter table personal_info add column country varchar(8) not null default '';
-- desc personal_info;
-- select user_id,portrait from personal_info where user_id=45;

-- select id,time,type,content from event_record where user_id=(select id from user where username='xfy123') order by time;
 
-- desc diabetes_info;
-- select * from diabetes_info;
-- select user_id,gender from personal_info;

-- select * from diabetes_info;

-- update diabetes_info set type='II型' where type='2';
-- select * from diabetes_info where type=2;
 
-- select id,num,day from sg_day_data where uid=251 order by day desc;
-- select * from index_record;
-- select * from realtime_data order by id desc limit 20;

/* 
select * from user where username='tcld01';
update device_activate_record set devicesn='102000106' where id=101;
select * from device_activate_record where uid=251;
 */
-- select * from index_record;

/*
DROP TABLE IF EXISTS index_record;
CREATE TABLE index_record (
  id int(64) NOT NULL auto_increment ,
  eventNo int(11) NOT NULL, 
  createTime datetime not null,
  indexResult varchar(16),
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
desc index_record;
*/

-- select * from diabetes_info;

-- select * from sg_day_data where uid=(select id from user where username='abcd55') and 
-- day='2016-03-22';

-- select * from event_record where id in ('47-102000054-0006-0001', '47-102000054-0006-0042');

-- select * from event_record where user_id=(select id from user where username='abcd55') and 
-- date(time)>'2016-03-20' order by time;

-- select * from basal_record where user_id=(select id from user where username='abcd55') and 
-- time>'2016-03-10' and del_flag!='Y' and type='BAS' order by time;
-- select * from device_activate_record where uid=(select id from user where username='abcd55') and 
-- devicetype='jn' order by startTime;


-- select * from sg_day_data where uid=(select id from user where username='abcd55') and 
-- day='2016-03-25';
-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd55') and 
-- date(time)='2016-03-25' order by time;

-- select * from sg_day_data where uid=(select id from user where username='abcd55') and 
-- day='2016-03-17';

-- select id,useTime,data from sg_day_data where uid=47 and day in ('2016-03-04', '2016-03-05', '2016-03-06');
-- alter table sg_day_data add column useTime smallint not null default 0;
-- alter table sg_day_data drop column timeUse;
-- desc sg_day_data;

-- select * from event_record where user_id=(select id from user where username='abcd55') and 
-- type='HBA1C' and date(time) in ('2016-03-09', '2016-03-10');

-- select * from monitor_job order by create_time desc limit 10;

-- alter table monitor_job add column data varchar(1024);
-- desc monitor_job;


-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd55') and 
-- date(time)='2016-03-18' order by time;

-- update user_setting set glucose_event_list='按事件,按时间' where glucose_event_list='';
-- select uid,glucose_event_list from user_setting;
-- desc user_setting;

/*
select * from basal_record where user_id=(select id from user where username='abcd55') and 
(date(time)=curdate() or date(end_time)=curdate()) and del_flag='N' order by time;
select * from device_activate_record where uid=(select id from user where username='abcd55') and 
devicetype='jn' order by startTime;
*/

-- select * from sg_day_data where uid=(select id from user where username='abcd55') and 
-- day='2016-03-09';
-- select * from bolus_record where user_id=(select id from user where username='abcd55') and 
-- date(time)>='2016-03-12' order by time;

-- select * from realtime_data where uid=(select id from user where username='abcd55') and 
-- flag='bolus';


-- select * from event_record where user_id=(select id from user where username='abcd55') and 
-- date(time)>'2016-02-08' order by type;

-- select * from user_setting where uid=(select id from user where username='abcd55');
-- delete from sg_day_data where day='2016-03-15';
-- select id,uid,day,num from sg_day_data where day='2016-03-15';

-- select id,uid,day,num from sg_day_data where day='2016-03-15';

-- select id,num,data from sg_day_data where uid=(select id from user where username='xfy123') and day='2016-03-13';
-- select * from device_activate_record where uid=(select id from user where username='xfy123') and 
-- devicetype='ty' order by startTime;
-- select id,uid,day,num from sg_day_data where day=curdate() and uid=(select id from user where username='tcld01');
-- alter table sg_day_data add column num smallint not null default 0;
-- desc sg_day_data;

-- alter table realtime_data modify data text not null;
-- desc realtime_data;
-- select * from realtime_data order by uploadTime desc limit 1;
-- select count(*) from sensor_glucose_record where date(time)=curdate() order by time;
-- select count(*) from sensor_glucose_record_rt where date(time)=curdate() order by time;
-- desc sensor_glucose_record_rt;

-- delete from sg_day_data where day>='2016-03-12';
-- select id,uid,day from sg_day_data where day>='2016-03-12';

-- select id,uid,day from sg_day_data where day>subdate(curdate(), interval 3 day);

-- select id, uid, day,data sn from sg_day_data where uid=(select id from user where username='abcd55') and 
-- day='2016-03-11';
 
-- select * from sensor_glucose_record where id in ('47-102000114-0014-1151');
/*  
DROP TABLE IF EXISTS sg_day_data;
CREATE TABLE sg_day_data (
  id varchar(32) NOT NULL,
  uid int(11) DEFAULT NULL,
  day date not null,
  data text not null,
  sn varchar(1024) not null default '[]',
  updateTime datetime NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
desc sg_day_data;
*/

-- select * from user_status where uid=(select id from user where username='tcld01') and 
-- flag='sensor' order by update_time desc limit 1;

-- select * from user where username='tcld01';
-- select uid,btime1_s from user_setting where uid=(select id from user where username='xfy1');

/*
select * from realtime_data where uid=(select id from user where username='tcld01') and flag='sg' order by uploadTime desc limit 2;
select * from sensor_glucose_record order by time desc limit 2;
select * from sensor_glucose_record_rt;
*/
-- select user_id,birth_date from personal_info where user_id=(select id from user) 
-- select * from user where username='tcld01';
/* 
DROP TABLE IF EXISTS sensor_glucose_record_rt;
CREATE TABLE sensor_glucose_record_rt (
  id varchar(64) NOT NULL,
  user_id int(11) DEFAULT NULL,
  sensor_id varchar(64) DEFAULT NULL,
  session_id varchar(64) DEFAULT NULL,
  time datetime NOT NULL,
  sensor_state varchar(4) NOT NULL,
  glucose_value float NOT NULL DEFAULT '0',
  signal_value float NOT NULL DEFAULT '0',
  rate float NOT NULL DEFAULT '0',
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
desc sensor_glucose_record_rt;
*/

/*
alter table push_job add column pushWay varchar(8) not null default 'user';
alter table push_job add column deviceToken varchar(1024);
desc push_job;
*/
-- select * from push_job;

-- select * from device_token;
-- select * from push_job;
/*
DROP TABLE IF EXISTS visit_record;
CREATE TABLE visit_record (
  id int(64) NOT NULL auto_increment ,
  uid int(11) NOT NULL,
  vuid int(11) NOT NULL,
  visitTime datetime not null,
  event varchar(512) not null default '',
  
  PRIMARY KEY (id),
  FOREIGN KEY (uid) REFERENCES user (id),
  FOREIGN KEY (vuid) REFERENCES user (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

desc visit_record;
*/

-- select uid,wday_list from user_setting;
-- update personal_info set telephone='20153' where user_id=(select id from user where username='abcd11');
-- select user_id,telephone from personal_info where user_id=(select id from user where username='abcd11');

-- select * from user where username='doct01';
-- select user_id,areaCode,telephone,telephoneExt from personal_info where user_id=(select id from user where username='doct01_8594');
/*
alter table personal_info add column areaCode varchar(6);
alter table personal_info add column telephoneExt varchar(6);
desc personal_info;
*/

-- select * from sensor_glucose_record where user_id=(select id from user where username='xfy123')
-- and date(time)=curdate() order by time ;

-- select * from realtime_data where uid=(select id from user where username='tcld01')
-- order by id desc limit 100;
-- desc personal_info;
-- select user_id,areaCode,telephone,telephoneExt from personal_info where user_id=(select id from user where username='xfys12');
-- select * from user where username='tcld01';
-- alter table realtime_data add column param varchar(512);
-- desc realtime_data;

-- select * from calib_record where user_id=(select id from user where username='xfy123') 
-- and date(time)='2016-02-25';

-- select * from basal_record where user_id=(select id from user where username='tcld01') 
-- and date(time)=curdate() order by time ;

-- select * from alarm_record where user_id=(select id from user where username='tcld01') 
-- and date(time)=curdate() order by time ;

-- alter table monitor_job add column eventNo int;
-- desc monitor_job;

/* 
select * from realtime_data where uid=(select id from user where username='tcld01') and flag='sg'
and date(uploadTime)=curdate() order by uploadTime desc limit 100;

select * from monitor_job where uid=(select id from user where username='tcld01') 
and date(create_time)=curdate() order by create_time desc limit 10;
*/

-- select * from user_status where uid=(select id from user where username='tcld01') and 
-- flag='pump' order by update_time desc limit 5;


/*
delete from basal_record where user_id=(select id from user where username='tcld01')
and date(time)=curdate();

select * from basal_record where user_id=(select id from user where username='tcld01')
and date(time)=curdate() order by time;
*/
-- select * from basal_record where user_id=(select id from user where username='abcd55') and 
-- date(time)=curdate() order by time ;
-- select * from push_job;

/* 
DROP TABLE IF EXISTS realtime_data;
CREATE TABLE realtime_data (
  id int(64) NOT NULL auto_increment ,
  uid int(11) NOT NULL,
  uploadTime datetime not null default CURRENT_TIMESTAMP,
  flag varchar(16) not null default '-',
  data varchar(8192) not null default '-',
  PRIMARY KEY (id),
  FOREIGN KEY (uid) REFERENCES user (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

desc realtime_data;
*/

-- select * from user_setting where uid=(select id from user where username='xfy1');

/*
select id,locate('-', id) from calib_record where locate('-', id)=0 order by time;
delete from calib_record where locate('-', id)=0;
select id,locate('-', id) from calib_record where locate('-', id)=12 order by time;
delete from calib_record where locate('-', id)=12;
update calib_record set sensor_id=substr(id, locate('-', id)+1, 9) where sensor_id='0' or sensor_id is null;
select * from calib_record order by time;
*/

-- alter table user_setting add column weight_unit  varchar(8) not null default 'kg';
-- alter table user_setting add column height_unit  varchar(8) not null default 'cm';
-- desc user_setting;

-- select * from device_activate_record where uid=(select id from user where username='person001') order by startTime;
-- select * from sensor_glucose_record where user_id=(select id from user where username='person001') and 
-- time>'2016-02-20 00:00:00' order by time; 

-- select * from calib_record where user_id=(select id from user where username='xfy123') 
-- order by time;

-- alter table user_status add column deviceSN varchar(32) not null default '0';
-- desc user_status;

-- select * from sensor_glucose_record where user_id=(select id from user where username='xfy123') and 
-- date(time)='2016-01-18' order by time; 

-- select * from basal_record where user_id=(select id from user where username='xfy123') and 
-- (date(time)='2016-02-24' or date(end_time)='2016-02-24') and del_flag='N' order by time;

-- select * from device_activate_record where uid=(select id from user where username='xfy123') and devicetype='jn' 
-- order by startTime;
-- select  * from sensor_glucose_record where user_id=(select id from user where username='xfy123') 
-- and date(time)='2016-02-22' and sensor_id='103000120' order by time;
-- select * from user_status where uid=(select id from user where username='xfy123') and flag='sensor' 
-- order by update_time desc limit 10;
-- select * from device_activate_record where uid=(select id from user where username='xfy123') and devicetype='ty';
-- select count(*) from sensor_glucose_record where user_id=(select id from user where username='xfy123');
-- select distinct date(time) from sensor_glucose_record where user_id=(select id from user where username='xfy123') order by time;

-- select * from bolus_record order by time desc limit 10;
-- alter table user_setting add column glucose_event_list varchar(128) not null;

-- select * from basal_record where date(time)=curdate() or date(end_time)=curdate();

-- select * from relation where object=(select id from user where username='test19');
-- select * from relation where subject=(select id from user where username='test19');

-- select * from user where type='M';
-- delete from push_job where id>0;
-- select * from push_job;
-- desc relation_apply;
-- select * from relation_apply where uid=(select id from user where username='abcd55');
-- select * from user where username='xfy1';
-- select * from relation where subject=()
-- select * from relation where subject=(select id from user where username='xfy1');
-- select * from relation where subject=(select id from user where username='abcd55');

-- select * from user where username='xfy3';
-- desc mail;
-- select * from mail where receiver_id=(select id from user where username='xfy1') and 
-- date(time)=curdate();
-- select * from sensor_glucose_record where date(time)=curdate() and 
-- user_id=(select id from user where username='xfy123');
-- desc alarm_record;
-- select * from device_activate_record;

/*
DROP TABLE IF EXISTS device_activate_record;
CREATE TABLE device_activate_record (
  id int(64) NOT NULL auto_increment ,
  uid int(11) NOT NULL,
  devicetype varchar(16) NOT NULL,
  devicesn varchar(32) NOT NULL,
  startTime datetime not null,
  endTime datetime not null,
  action varchar(16) not null,
  PRIMARY KEY (id),
  FOREIGN KEY (uid) REFERENCES user (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
desc device_activate_record;
*/

-- select * from monitor_job where finish_flag!='Y' order by create_time desc limit 20;
-- select * from app_setting;
-- select * from user where id in (9,103,109);
/*
alter table app_setting modify glucoseTargetHigh float not null default 13.33;
alter table app_setting modify glucoseTargetLow float not null default 4.44;
desc app_setting;
*/

/* 
DROP TABLE IF EXISTS app_setting;
CREATE TABLE app_setting (
  id int(64) NOT NULL auto_increment,
  uid int(11) NOT NULL,
  glucoseTargetLow varchar(16) NOT NULL default 4,
  glucoseTargetHigh varchar(16) NOT NULL default 4,
  update_time datetime not null,
  PRIMARY KEY (id),
  FOREIGN KEY (uid) REFERENCES user (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
desc app_setting;
*/

-- select * from user_status where uid=(select id from user where username='test13') and flag='sensor' and 
-- update_time>='2016-01-26 11:00:00' and update_time<='2016-01-27 09:120:00' order by update_time;

-- delete from basal_record where substr(id, 1, locate('-', id)-1)=0;
-- update basal_record set pump_sn=substr(id, locate('-', id)+1, 9) where pump_sn='0' or pump_sn is null;
-- select id, pump_sn from basal_record;

-- update bolus_record set pump_sn=substr(id, locate('-', id)+1, 9) where pump_sn='0' or pump_sn is null;
-- select id, pump_sn from bolus_record;
-- delete from bolus_record where substr(id, 1, locate('-', id)-1)=0;

-- select id, locate('-', id), substr(id, 1, locate('-', id)-1) from bolus_record;

-- delete from bolus_record where id not like '%-%';
-- select * from bolus_record where id not like '%-%';

-- select * from user_status where uid=(select id from user where username='abcd55') 
-- and flag='pump' and update_time>'2016-01-22 17:00:00' and update_time<'2016-01-22 17:16:00'  order by update_time;


-- select * from basal_record where date(time)=subdate(curdate(), interval 1 day);
-- select * from user_status where uid=(select id from user where username='abcd55') order by time;

-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd22') and 
-- date(time)=curdate();
-- select chart_show_list from user_setting;
-- update user_setting set chart_show_list='["运动", "泵", "血糖统计", "食物"]' where chart_show_list='[]';
-- select uid,chart_show_list from user_setting;
-- select uid,wday_list from user_setting;
-- update user_setting set wday_list='["周一", "周二", "周三", "周四", "周五", "周六", "周日"]' where wday_list='[]';
-- select uid,wday_list from user_setting;

-- select uid,quick_report_list from user_setting;
-- update user_setting set quick_report_list='["每日总结", "分段模式", "分时模式", "高低血糖事件", "趋势分析", "优化对比", "日志汇总", "设备设置", "产品依赖性", "糖化血红蛋白记录",]' where quick_report_list='[]';
-- select uid,quick_report_list from user_setting;
/*
desc user_setting;
alter table user_setting modify wday_list varchar(64) not null default '["周一", "周二", "周三", "周四", "周五", "周六", "周日"]';
alter table user_setting modify quick_report_list varchar(128) not null default '["每日总结", "分段模式", "分时模式", "高低血糖事件", "趋势分析", "优化对比", "日志汇总", "设备设置", "产品依赖性", "糖化血红蛋白记录",]';
alter table user_setting modify chart_show_list varchar(32) not null default '["运动", "泵", "血糖统计", "食物"]';
desc user_setting;
*/
-- select quick_report_list from user_setting;
-- update user_setting set quick_report_list='["每日总结", "分段模式", "分时模式", "高低血糖事件", "趋势分析", "优化对比", "日志汇总", "设备设置", "产品依赖性", "糖化血红蛋白记录"]' -- where quick_report_list='["每日总结", "分段模式", "分时模式", "高低血糖事件", "趋势分析", "优化对比", "日志汇总", "设备设置", "产品依赖性", "糖化血红蛋白记录",]';
--  select quick_report_list from user_setting;
-- select * from user;
-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd22') and time>'2015-11-17 00:00:00' and time <'2015-11-24 00:00:00' 
-- order by time;

-- select * from alarm_record;
-- desc alarm_record;
-- alter table alarm_record modify alarm_id int(11) not null;
-- desc alarm_record;

-- alter table alarm_record change pdm_sn device_sn varchar(32) not null;
-- desc alarm_record;
-- select count(*) from job_queue;
-- select * from alarm_record;
-- select uid, chart_show_list from user_setting;
-- desc user_setting;
-- select * from user where id in (143,47,103);
-- select * from sensor_glucose_record where user_id =(select id from user where username='abcd22') and 
-- date(time)='2015-11-13' order by time;
-- select * from alarm_record order by time;
-- select blos_high,blos_low from user_setting where uid=(select id from user where username='abcd22');
-- select * from sensor_glucose_record where user_id =(select id from user where username='abcd22') and 
-- date(time)='2015-11-25' order by time;
-- select count(*) from push_job;
-- desc user_status;
-- select sensor_updatetime from user_status where uid=(select id from user where username='abcd33');
-- show variables like '%time_zone%';
-- select * from bolus_record where user_id=(select id from user where username='abcd33');
-- desc alarm_record;
-- show create table alarm_record;
-- delete from alarm_record where time<'1973-06-15';
--  select * from alarm_record order by time;
-- desc job_queue;
-- select count(*) from job_queue where date(create_time)<'2015-11-26' and finish_flag='N';
-- select count(*) from job_queue;
-- delete from job_queue where date(create_time)<'2015-11-26' and finish_flag='Y';
-- select count(*) from job_queue;
-- select create_time,finish_flag from job_queue where date(create_time)<'2015-11-26';
-- delete from job_queue where date(create_time)<'2015-11-26';
-- select count(*) from job_queue;
-- select uid,create_time,finish_flag from job_queue order by create_time;
-- delete from job_queue where  finish_flag='Y';
-- select uid,create_time,finish_flag from job_queue order by create_time;
-- select * from basal_record where user_id=(select id from user where username='xfy123') and date(time)='2015-11-25' order by time;
-- select * from sensor_glucose_record where user_id=(select id from user where username='xfy123') and date(time)='2015-11-27' order by time;
-- select * from basal_record where user_id=(select id from user where username='abcd22') and 
-- date(time) in (curdate(), subdate(curdate(), 1)) and del_flag='N' order by time;
-- select count(*) from job_queue;
/*
DROP TABLE IF EXISTS monitor_job;
CREATE TABLE monitor_job (
  id int(64) NOT NULL auto_increment ,
  uid int(11) NOT NULL,
  jobid varchar(64) NOT NULL,
  flag varchar(16) NOT NULL default 'NODATA',
  create_time datetime NOT NULL,
  finish_flag varchar(1) not null default 'N',
  PRIMARY KEY (id),
  FOREIGN KEY (uid) REFERENCES user (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

desc monitor_job;
*/
-- alter table monitor_job add column muid int(11);
-- alter table monitor_job add foreign key(muid) references user (id);
-- desc monitor_job;
-- select * from monitor_job;
-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd22') order by time desc limit 2;
-- alter table monitor_job add column param varchar(8192) not null default '';
-- desc monitor_job;
-- delete from monitor_job where id<=4;
-- select * from monitor_job;
-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd22') order by time desc limit 2;
-- alter table monitor_job add column update_flag varchar(1) not null default 'N';
-- desc monitor_job;
-- select * from user_status;
/*
alter table user_status drop primary key ;
alter table user_status add column id int not null primary key auto_increment;
desc user_status;
*/

-- select id,uid from user_status;
/*
alter table user_status add column update_time datetime not null;
alter table user_status add column flag varchar(16) not null default '';
alter table user_status add column status varchar(2048) not null default '';
*/
-- desc user_status;
-- delete from monitor_job where finish_flag='Y';
-- select * from monitor_job;
-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd22') order by time desc limit 2;
--
-- delete from user_status where date(update_time)<curdate();
-- select id,uid,flag,update_time from user_status where uid=(select id from user where username='xfy123');
-- delete from job_queue where finish_flag='Y';
-- select * from job_queue;
-- select * from user_status;
/*
alter table user_status drop column online;
alter table user_status drop column sensor_sn;
alter table user_status drop column sensor_expiretime;
alter table user_status drop column sensor_updatetime;
alter table user_status drop column sensor_state;
alter table user_status drop column sensor_glucose;
alter table user_status drop column sensor_battery;
alter table user_status drop column pump_sn;
alter table user_status drop column pump_expiretime;
alter table user_status drop column pump_updatetime;
alter table user_status drop column pump_leftinsulin;
alter table user_status drop column pump_basal;
alter table user_status drop column pump_bolus;
alter table user_status drop column pump_boluslatest;
alter table user_status drop column pump_iob;
desc user_status;
*/

-- select * from user_status where uid=(22) and date(update_time)='2015-12-01' order by update_time  desc  limit 2;
-- select * from push_job;
-- select * from report_job;
 
-- delete from monitor_job where finish_flag='Y';
-- select * from monitor_job;
-- select * from basal_record where user_id=(select id from user where username='xfy123') and date(time)='2015-12-04' order by time desc;
--  select * from bolus_record where user_id=(select id from user where username='xfy123') and date(time)='2015-12-04' order by time desc;
-- select * from user_setting where uid=109;
-- select id,uid,update_time from user_setting;
-- delete from user_setting where id=19;
-- select id,uid,update_time from user_setting;
-- select * from user where id in (143);
-- show create table user_setting;
-- alter table user_setting add foreign key(uid) references user (id);
-- alter table user_setting modify uid int(11) not null;
-- desc user_setting;
-- desc monitor_job;
-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd22') and 
-- date(time)=curdate() order by time;


-- select * from user_status where uid=(22) and date(update_time)='2015-12-02' order by update_time  desc  limit 10;
-- delete from monitor_job where finish_flag='Y';
-- select * from monitor_job;
-- select id,username from user where username in ('test11', 'test13');
-- select count(*) from sensor_glucose_record;
-- select count(*) from bolus_record;
-- select count(*) from basal_record;
-- select count(*) from report_job;

-- select id,sender_id,receiver_id from mail;
-- select count(*) from sensor_glucose_record where date(time) in ('2015-12-04');
-- select count(*) as security_code_num from security_code;
/*
delete from user_status where update_time<'2015-12-07 00:00:00';
select count(*) from json_create_record;
select count(*) from sensor_glucose_record;
select count(*) from basal_record;
select count(*) from bolus_record;
select count(*) from login_record;
select count(*) from user_status;
*/

-- show tables;
-- select id, uid, flag, update_time from user_status order by update_time desc limit 200;

-- select id, uid, flag, update_time from user_status order by update_time desc limit 200;
-- select * from basal_record where user_id=(select id from user where username='abcd22') and 
-- date(time)=curdate() order by time;

-- select * from bolus_record where user_id=(select id from user where username='abcd22') and 
-- date(time)=curdate() order by time;

-- delete from user_status where date(update_time)<curdate();
-- select count(*) from user_status;

-- select * from user_status where uid=(select id from user where username='xfy123') and flag='sensor' and  
-- date(update_time)=curdate() order by update_time desc limit 2;

-- delete from basal_record where date(time)<'2015-09-11';

-- select * from user_status 
-- alter table basal_record add column end_time datetime;
-- desc basal_record;
-- select * from basal_record order by time desc limit 4;
-- '197-108000089-0003-0002'
-- update basal_record set end_time=date_add(time, interval duration minute) where id='197-108000089-0003-0002';
-- update basal_record set end_time=date_add(time, interval duration minute) where end_time is null;
-- select * from  basal_record where user_id=(select id from user where username='xfy123') order by time desc limit 10;


-- delete from monitor_job where finish_flag='Y';
-- select * from monitor_job;
-- select count(*) from user_setting;
-- alter table user_setting add column device_option varchar(32) not null default 'cgms,pump';
-- desc user_setting;
/*
DROP TABLE IF EXISTS device_activate_record;
CREATE TABLE device_activate_record (
  id int(64) NOT NULL auto_increment ,
  uid int(11) NOT NULL,
  devicetype varchar(16) NOT NULL,
  devicesn varchar(32) NOT NULL,
  update_time datetime not null,
  action varchar(16) not null,
  PRIMARY KEY (id),
  FOREIGN KEY (uid) REFERENCES user (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
desc device_activate_record;
*/

-- select * from device_activate_record;
-- delete from user_status where date(update_time)<curdate();
-- select count(*) from user_status;
-- select * from device_activate_record;
-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd22') and 
-- date(time)=curdate() order by time;
-- delete from sensor_glucose_record where date(time)<'2000-01-01';
-- select * from sensor_glucose_record where user_id in (142,83,91) order by time;

-- select count(*) from sensor_glucose_record;
-- delete from sensor_glucose_record where user_id in (142,83,91) and date(time)='2015-08-28' and id not like '%-%';
-- delete from sensor_glucose_record where id not like '%-%';
-- select * from sensor_glucose_record where user_id in (142,83,91) order by time limit 100;
-- select count(*) from sensor_glucose_record;
-- select id,username from user where id in (142,83,91);
-- select id, user_id, char_length(user_id),substr(id, locate('-', id)+1, 9) from sensor_glucose_record limit 50;
-- select * from sensor_glucose_record order by time desc limit 100;
-- desc sensor_glucose_record;
-- update sensor_glucose_record set sensor_id=substr(id, locate('-', id)+1, 9) where sensor_id='0' or sensor_id is null;
-- select * from sensor_glucose_record order by time asc limit 100;
-- select uid, device_option from user_setting where uid=109;
-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd22') and 
-- date(time)=curdate() order by time;
-- select * from device_activate_record;
-- select count(*) from user;
-- select * from user_status where uid=(select id from user where username='abcd22') and 
-- date(update_time)=curdate() order by update_time desc limit 20;
-- select id, locate('-', substr(id, locate('-', id)+1)) from sensor_glucose_record order by time limit 1000;
-- select uid,wday_list from user_setting;
-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd22') and 
-- date(time)=curdate() order by time;
-- select * from device_activate_record;
-- select id,uid,wday_list from user_setting;
/*
这个SQL语句是在windows的命令行里面执行。windows的系统编码是GBK。
所以这个文件里面的内容会以GBK的方式来解码。因此这个文件应该用GBK编码。
*/
-- update user_setting set wday_list='周一' where id=24;
-- select id,uid,wday_list from user_setting;
-- select * from user where id=73;
-- select id,uid,device_option from user_setting;
-- select * from user where username like '%jie%';
-- select * from mail where receiver_id=(select id from user where username='abcd33') and r_del_flag != 'Y';
-- select * from user_status where uid=(select id from user where username='xfy123') and flag='pump' order by update_time desc limit 100;
-- select * from security_code limit 100;
-- desc sensor_glucose_record;
-- alter table sensor_glucose_record modify time datetime not null;
-- alter table sensor_glucose_record modify sensor_state varchar(4) not null;
-- alter table sensor_glucose_record modify glucose_value float not null default 0;
-- alter table sensor_glucose_record modify signal_value float not null default 0;
-- update sensor_glucose_record set rate=0 where rate is null;
/* 如果字段里面有记录的值为NULL，那么更改字段时把属性改成not null就会报错。
*/
-- alter table sensor_glucose_record modify rate float not null default 0;
-- desc sensor_glucose_record;
-- select id, glucose_value,rate from sensor_glucose_record limit 10;
-- select * from user_status where uid=(select id from user where username='abcd55') and flag='pump' order by update_time desc limit 100;
-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd55') order by time desc limit 5;
-- select * from basal_record where user_id=(select id from user where username='abcd55') and date(time)=curdate() order by time;
-- select count(*) from sensor_glucose_record where date(time)='2015-12-16';
-- select id, chart_show_list from user_setting;
-- alter table user_setting drop column chart_show_list;
-- desc user_setting;
-- select * from device_activate_record;
-- select * from basal_record where user_id=(select id from user where username='xfy123') and date(end_time)=curdate() order by time;
-- update personal_info set portrait='no-avatar.jpg' where portrait='temp.jpeg';
-- select user_id, portrait from personal_info;
-- select * from sensor_glucose_record where user_id=(select id from user where username='xfy123') and date(time)=curdate() order by time desc limit 100;
/*
update relation,user set privilege='R' where privilege='0' and  object in (select id from user where type in ('D', 'P') and id=object);
select rid, privilege from relation;

DROP TABLE IF EXISTS hospital_record;
CREATE TABLE hospital_record (
  id int(64) NOT NULL auto_increment ,
  uid int(11) NOT NULL,
  inHospital varchar(1) not null default 'N',
  patientNo varchar(16) not null default '-',
  bedNo varchar(16) not null default '-',
  updateTime datetime not null,
  PRIMARY KEY (id),
  FOREIGN KEY (uid) REFERENCES user (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

desc hospital_record;
*/
-- select * from report_job limit 100;
-- select count(*) from report_job;
-- desc report_job;
-- delete from report_job where finish_flag='Y';
-- select count(*) from report_job;
-- select * from user_status where uid=(select id from user where username='xfy123') and flag='sensor' order by update_time;
-- select * from sensor_glucose_record where user_id=(select id from user where username='xfy123') and date(time)=curdate() order by time;
-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd55') and date(time)='2015-12-19' order by time;
-- select uid,device_option from user_setting;
-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd55') and date(time)=curdate() order by time;
-- select take_date from dose_record;
-- select * from calib_record where user_id=(select id from user where username='xfy123') and date(time)=curdate() order by time;
-- select * from user_status where uid=(select id from user where username='abcd55') and 
-- date(update_time)=curdate() and flag='pump' order by update_time desc limit 20;
-- select * from bolus_record where date(time)=curdate() order by time;
-- select user_id, time, state from bolus_record;
-- select * from sensor_glucose_record where sensor_state='IC';
-- select user_id, portrait,update_time from personal_info where user_id=(select id from user where username='test13');
-- select * from user_status where uid=(select id from user where username='xfy123') order by update_time desc limit 10;
-- select * from blood_glucose_record limit 100;
-- select count(*) from calib_record;
-- select count(*) from event_record;
-- select * from calib_record where date(time)=curdate();
-- select * from device_activate_record where date(update_time)=curdate();
-- select * from device_activate_record where uid=(select id from user where username='xfy123') and devicetype='ty' order by update_time;
-- select uid,due_date from user_setting;
-- select * from basal_record where user_id=(select id from user where username='xfy123') and date(time) in ('2015-12-04', '2015-12-05') order by time;
-- select * from user_status where uid=(select id from user where username='abcd55') and 
-- date(update_time)=curdate() and flag='sensor' order by update_time desc limit 200;
-- select * from sensor_glucose_record where user_id=(select id from user where username='abcd55') and date(time)=curdate() order by time;
-- desc dose_record;
-- alter table dose_record drop column take_date;
-- alter table dose_record add column remark varchar(1028); 
-- desc dose_record;
-- select * from sensor_glucose_record where sensor_state='IC' limit 100;
-- delete from monitor_job where finish_flag='Y';
-- select id,username from user where username in ('abcd55', 'xfy123');
-- select * from monitor_job where date(create_time)=curdate();
-- select * from user where username='abcd55';
-- select * from event_record where user_id=(select id from user where username='tcld01');
-- select * from event_record where type='INS' limit 100;
-- select * from user_status where uid=(select id from user where username='xfy123') and flag='pump' order by update_time desc limit 10;
-- select * from user where username in ('xfy1', 'xfy123');
-- delete from monitor_job where finish_flag='Y';
-- select * from monitor_job where date(create_time)=curdate();
-- select * from bolus_record where user_id=(select id from user where username='test13') order by time desc limit 10;
-- select * from monitor_job;
-- select * from user_status where uid=(select id from user where username='xfy123') and flag='pump' order by update_time desc limit 2;
/*
 desc hospital_record;
 alter table hospital_record modify patientNo varchar(16) not null default '';
 alter table hospital_record modify bedNo varchar(16) not null default '';
 desc hospital_record;
 */
 /*
 update hospital_record set patientNo='' where patientNo='-';
 update hospital_record set bedNo='' where bedNo='-';
 select * from hospital_record;
 */
-- select user_id,portrait from personal_info where user_id =(select id from user where username='test13');
-- select * from device_token;
-- delete from push_job where date(create_time)<curdate() and finish_flag='Y';
-- select * from push_job order by create_time;
-- desc push_job;
-- show create table push_job;
-- alter table push_job drop column devicetoken;
-- alter table push_job add column pushUid int(11); 
-- alter table push_job add foreign key(pushUid) references user (id);
-- alter table push_job drop foreign key push_job_ibfk_2;
-- alter table push_job drop column pushUid;
-- desc push_job;

-- select * from  diabetes_info where user_id=(select id from user where username='test13');
-- select * from monitor_job where uid=(select id from user where username='test13') and muid in (select id from user where username in ('abcd55', 'xfy123')) 
-- order by create_time desc limit 20;
-- select * from alarm_record limit 1000;
