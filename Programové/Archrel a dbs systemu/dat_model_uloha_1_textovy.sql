DROP TABLE P01_OKRES cascade constraints;
create table P01_OKRES
(
ID number(4),
NAZEV varchar2(64),
constraint P01_OKRES_PK primary key (id)
);

DROP TABLE P01_OBEC cascade constraints;
create table P01_OBEC
(
ID number(5),
NAZEV varchar2(64),
ID_OKRES number(5) NOT NULL,
constraint P01_OBEC_PK primary key (ID),
constraint P01_OBEC_FK01 foreign key (ID_OKRES) references P01_OKRES(ID)
);

DROP TABLE P01_CAST_OBCE cascade constraints;
create table P01_CAST_OBCE
(
ID number(5),
NAZEV varchar2(64),
ID_OBEC number(5) NOT NULL,
constraint P01_CAST_OBCE_PK primary key (ID),
constraint P01_CAST_OBCE_FK01 foreign key (ID_OBEC) references P01_OBEC(ID)
);




DROP TABLE P01_KAT_UZ cascade constraints;
create table P01_KAT_UZ
(
ID number(6),
NAZEV varchar2(64),
ID_OBEC number(5) NOT NULL,
constraint P01_KAT_UZ_PK
  primary key (ID),
constraint P01_KAT_UZ_FK01
  foreign key (ID_OBEC) references P01_OBEC(ID)
);

DROP TABLE P01_BUDOVA cascade constraints;
create table P01_BUDOVA
(
TYP_CISLA VARCHAR2(1), /* P - popisne, E -evidencni*/
CISLO_DOMOVNI number(5), /* cislo popisne nebo evidencni */
ID_CAST_OBCE number(5) NOT NULL,
CIS_LV number(5),
constraint P01_BUDOVA_PK
  primary key (ID_CAST_OBCE,TYP_CISLA,CISLO_DOMOVNI),
constraint P01_BUDOVA_FK01
  foreign key (ID_CAST_OBCE) references P01_CAST_OBCE(ID),
constraint P01_BUDOVA_CH01
  check (TYP_CISLA IN ('E','P')),
constraint P01_BUDOVA_CH02
  check (CISLO_DOMOVNI>0)
);

drop table P01_PARCELA cascade constraints;
create table P01_PARCELA
(
ID_KU number(6),
PARC_TYP number(1),
PARC_CIS number(4),
PAR_POD number(3),
DRUH_POZ number(2),
NEM_VYUZ number(3),
VYMERA number(9),
CIS_LV number(5),
constraint P01_PARCELA_PK
  primary key (ID_KU,PARC_TYP,PARC_CIS,PAR_POD),
constraint P01_PARCELA_FK01
  foreign key (ID_KU) references P01_KAT_UZ(ID),
constraint P01_PARCELA_CH01
  check (PARC_TYP IN ('1','2'))
);

drop table P01_OPSUB cascade constraints;
create table P01_OPSUB
(
ID int,
ICO number(8),
RC number(10),
SJM_PARTNER1 int,
SJM_PARTNER2 int,
PRIJMENI varchar2(128),
JMENO varchar2(64),
TITUL_PRED varchar2(16),
TITUL_ZA varchar2(16),
ADRESA_OKRES number(4) not null,
ADRESA_OBEC number(5) not null,
ADRESA_COBCE number(5) not null,
ADRESA_CPOP number(5) not null,
constraint P01_OPSUB_PK primary key (ID),
constraint P01_OPSUB_FK1 foreign key
  (ADRESA_OKRES) references P01_OKRES(ID),
constraint P01_OPSUB_FK2 foreign key
  (ADRESA_OBEC) references P01_OBEC(ID),
constraint P01_OPSUB_FK3 foreign key (ADRESA_OBEC)
  references P01_OBEC(ID),
constraint P01_OPSUB_FK4 foreign key (ADRESA_COBCE)
  references P01_CAST_OBCE(ID),
constraint P01_OPSUB_FK5 foreign key (SJM_PARTNER1)
  references P01_OPSUB(ID),
constraint P01_OPSUB_FK6 foreign key (SJM_PARTNER2) references P01_OPSUB(ID)
);

drop table P01_LV cascade constraints;
create table P01_LV
(
ID_KU number(6),
ID_LV number(5),
constraint P01_LV_PK primary key (ID_KU,ID_LV),
constraint P01_LV_FK1 foreign key (ID_KU) references P01_KAT_UZ(ID)
);

alter table P01_PARCELA add constraint P01_PARCELA_FK3 foreign key (ID_KU,CIS_LV) references P01_LV(ID_KU,ID_LV);

alter table P01_PARCELA modify CIS_LV not null;

alter table P01_BUDOVA add LV_KU number(6);

alter table P01_BUDOVA add
constraint P01_BUDOVA_FK3 foreign key (LV_KU,CIS_LV) references P01_LV(ID_KU,ID_LV);

alter table P01_BUDOVA modify CIS_LV not null;

alter table P01_BUDOVA modify LV_KU not null;

drop table P01_VLASTNI cascade constraints;
create table P01_VLASTNI
(
ID_KU number(6),
ID_LV number(5),
ID_OPSUB int,
PODIL_CITATEL int,
PODIL_JMENOVATEL int,
constraint P01_VLASTNI_PK primary key(ID_KU,ID_LV,ID_OPSUB),
constraint P01_VLASTNI_FK1 foreign key (ID_KU,ID_LV) references P01_LV(ID_KU,ID_LV),
constraint P01_VLASTNI_FK2 foreign key (ID_OPSUB) references P01_OPSUB(ID)
);
