DROP TABLE P01_OKRES cascade constraints;

create table P01_OKRES
(
ID number(5),
NAZEV varchar2(64) NOT NULL,
constraint P01_OKRES_PK primary key (id)
);

DROP TABLE P01_OBEC cascade constraints;

create table P01_OBEC
(
ID number(5),
NAZEV varchar2(64) NOT NULL,
ID_OKRES number(5) NOT NULL,
constraint P01_OBEC_PK primary key (ID),
constraint P01_OBEC_FK01 foreign key (ID_OKRES) references P01_OKRES(ID)
);

DROP TABLE P01_CAST_OBCE cascade constraints;

create table P01_CAST_OBCE
(
ID number(5),
NAZEV varchar2(64) NOT NULL,
ID_OBEC number(5) NOT NULL,
constraint P01_CAST_OBCE_PK primary key (ID),
constraint P01_CAST_OBCE_FK01 foreign key (ID_OBEC) references P01_OBEC(ID)
);

DROP TABLE P01_KAT_UZ cascade constraints;

create table P01_KAT_UZ
(
ID number(6),
NAZEV varchar2(64) NOT NULL,
ID_OBEC number(5) NOT NULL,
constraint P01_KAT_UZ_PK primary key (ID),
constraint P01_KAT_UZ_FK01 foreign key (ID_OBEC) references P01_OBEC(ID)
);

DROP TABLE P01_BUDOVA cascade constraints;

create table P01_BUDOVA
(
TYP_CISLA VARCHAR2(1), /* P - popisne, E - evidencni */
CISLO_DOMOVNI number(5), /* cislo popisne nebo evidencni */
ID_CAST_OBCE number(5) NOT NULL,
CIS_LV number(5),
constraint P01_BUDOVA_PK primary key (ID_CAST_OBCE,TYP_CISLA,CISLO_DOMOVNI),
constraint P01_BUDOVA_FK01 foreign key (ID_CAST_OBCE)
references P01_CAST_OBCE(ID),
constraint P01_BUDOVA_CH01 check (TYP_CISLA IN ('E','P')),
constraint P01_BUDOVA_CH02 check (CISLO_DOMOVNI>0)
);

DROP TABLE P01_PARCELA cascade constraints;

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
constraint P01_PARCELA_PK primary key (ID_KU,PARC_TYP,PARC_CIS,PAR_POD),
constraint P01_PARCELA_FK01 foreign key (ID_KU) references P01_KAT_UZ(ID),
constraint P01_PARCELA_CH01 check (PARC_TYP IN ('1','2'))
);

/* ************************************************************************ */

DROP TABLE P01_VLASTNI cascade constraints;

create table P01_VLASTNI
(
ID number(5), 
POD_JM number(2),
POD_CIT number(2),
constraint P01_VLASTNI_PK primary key (ID)
);

DROP TABLE P01_OPSUB cascade constraints;

create table P01_OPSUB
(
ID_LV number(5),
ICO varchar2(15),
RC varchar2(10),
RC_SJM varchar2(10),
JMENO varchar2(10),
PRIJMENI varchar2(15),
TITPJ varchar2(10),
TITZJ varchar2(6),
ADR_OKR varchar2(20),
ADR_OB varchar2(20),
ADR_C_OB varchar2(20),
ADR_POO varchar2(10),
constraint P01_OPSUB_PK primary key (ICO, RC, RC_SJM),
constraint P01_OPSUB_FK foreign key (ID_LV) references P01_VLASTNI(ID)
);

DROP TABLE P01_LV cascade constraints;

create table P01_LV
(
ID_LV number(5),
ID number(5),
LV_ID_KU number(6),
LV_PARC_TYP number(1),
LV_PARC_CIS number(4),
LV_PAR_POD number(3),
LV_TYP_CISLA VARCHAR2(1), 
LV_CISLO_DOMOVNI number(5),
LV_ID_CAST_OBCE number(5) NOT NULL,
constraint P01_LV_PK primary key (ID),
constraint P01_LV_FK1 foreign key (ID_LV) references P01_VLASTNI(ID),
constraint P01_LV_FK2 
foreign key (LV_ID_CAST_OBCE, LV_TYP_CISLA, LV_CISLO_DOMOVNI) 
references P01_BUDOVA(ID_CAST_OBCE,TYP_CISLA,CISLO_DOMOVNI),
constraint P01_LV_FK3 foreign key (LV_ID_KU, LV_PARC_TYP,LV_PARC_CIS,LV_PAR_POD) 
references P01_PARCELA(ID_KU,PARC_TYP,PARC_CIS,PAR_POD)
);
