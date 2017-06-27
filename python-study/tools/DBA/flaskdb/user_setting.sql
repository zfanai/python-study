 use flaskdb;

 -- 4
alter table user_setting add column glucose_unit varchar(8) not null default 'mmol/L';
alter table user_setting add column hypo float not null default 3.1;
alter table user_setting add column blos_high float not null default 7.8;
alter table user_setting add column blos_low float not null default 3.9;
-- 14
alter table user_setting add column blos_high_before_b float not null default 7.2;
alter table user_setting add column blos_low_before_b float not null default 3.9;
alter table user_setting add column blos_high_after_b float not null default 8.9;
alter table user_setting add column blos_low_after_b float not null default 5.6;
alter table user_setting add column blos_high_before_l float not null default 7.2;
alter table user_setting add column blos_low_before_l  float not null default 3.9;
alter table user_setting add column blos_high_after_l  float not null default 8.9;
alter table user_setting add column blos_low_after_l  float not null default 5.6;
alter table user_setting add column blos_high_before_s  float not null default 7.2;
alter table user_setting add column blos_low_before_s  float not null default 3.9;
alter table user_setting add column blos_high_after_s  float not null default 8.9;
alter table user_setting add column blos_low_after_s  float not null default 5.6;
alter table user_setting add column blos_high_night  float not null default 8.9;
alter table user_setting add column blos_low_night float not null default 5.6;

-- 8
alter table user_setting add column btime1_s varchar(8) not null default '07:00';
alter table user_setting add column btime1_e varchar(8) not null default '08:00';
alter table user_setting add column ltime1_s varchar(8) not null default '12:00';
alter table user_setting add column ltime1_e varchar(8) not null default '13:00';
alter table user_setting add column stime1_s varchar(8) not null default '18:00';
alter table user_setting add column stime1_e varchar(8) not null default '19:00';
alter table user_setting add column etime1_s varchar(8) not null default '23:00';
alter table user_setting add column etime1_e varchar(8) not null default '06:00';

-- 6
alter table user_setting add column afterb_s varchar(8) not null default '01:00';
alter table user_setting add column afterb_e varchar(8) not null default '03:00';
alter table user_setting add column afterl_s varchar(8) not null default '01:00';
alter table user_setting add column afterl_e varchar(8) not null default '03:00';
alter table user_setting add column afters_s varchar(8) not null default '01:00';
alter table user_setting add column afters_e varchar(8) not null default '03:00';

alter table user_setting add column time_range varchar(16) not null default 'Week';
alter table user_setting modify due_date varchar(16) not null default '昨天';
alter table user_setting add column wday_list varchar(64) not null default '[]';

-- 
alter table user_setting add column graph_type_ta varchar(8) not null default '全部';
alter table user_setting add column graph_type_rm varchar(8) not null default '全部';
alter table user_setting add column graph_type_tm varchar(8) not null default '全部';
alter table user_setting add column graph_type_ea varchar(8) not null default '全部';

alter table user_setting add column quick_report_list varchar(128) not null default '[]';
alter table user_setting add column chart_show_list varchar(32) not null default '[]';

alter table user_setting add column time_mode_rog varchar(8) not null default '显示';
alter table user_setting add column time_mode_pie varchar(8) not null default '显示';
alter table user_setting add column ta_version varchar(8) not null default '完整版';
alter table user_setting add column opti_comp varchar(8) not null default '日';
alter table user_setting add column log_sum_report varchar(8) not null default '按项目';
desc user_setting;


