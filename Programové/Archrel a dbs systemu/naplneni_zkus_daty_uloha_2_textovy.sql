insert into p01_okres values (1,'Vyskov');
insert into p01_okres values (2,'Brno mesto');
insert into p01_okres values (3,'Blansko');

insert into p01_obec values (1,'Vyskov',1);
insert into p01_obec values (2,'Ivanovice na Hane',1);
insert into p01_obec values (3,'Drnovice',1);
insert into p01_obec values (4,'Brno',2);
insert into p01_obec values (5,'Blansko',3);

insert into p01_cast_obce values (1,'Vyskov',1);
insert into p01_cast_obce values (2,'Dedice',1);
insert into p01_cast_obce values (3,'Ivanovice na Hane',2);
insert into p01_cast_obce values (4,'Drnovice',3);
insert into p01_cast_obce values (5,'Kralovo pole',4);
insert into p01_cast_obce values (6,'Zabovresky',4);
insert into p01_cast_obce values (7,'Blansko',5);

insert into p01_kat_uz values (1,'Vyskov',1);
insert into p01_kat_uz values (2,'Dedice',1);
insert into p01_kat_uz values (3,'Ivanovice na Hane',2);
insert into p01_kat_uz values (4,'Drnovice',3);
insert into p01_kat_uz values (5,'Kralovo pole',4);
insert into p01_kat_uz values (6,'Zabovresky',4);
insert into p01_kat_uz values (7,'Blansko',5);

insert into p01_opsub values (1,NULL,7401084669,NULL,NULL,'Riha','Zdenek','Mgr.','',1,1,2,498);
insert into p01_opsub values (2,NULL,7903084959,NULL,NULL,'Vesely','Karel','','',2,4,5,125);
insert into p01_opsub values (3,NULL,8156031224,NULL,NULL,'Stastna','Eva','','',2,4,5,125);
insert into p01_opsub values (4,NULL,NULL,2,3,'','','','',2,4,5,125);
insert into p01_opsub values (5,NULL,8001103484,NULL,NULL,'Svub','Petr','','',2,4,5,100);

alter table p01_parcela disable constraint P01_PARCELA_FK3 ;

insert into p01_parcela values (2,1,2215,2,1,1,20,1);
insert into p01_parcela values (1,1,2000,1,1,1,30,1);
insert into p01_parcela values (1,1,5678,1,1,1,34,2);
insert into p01_parcela values (5,1,1234,5,1,1,128,1);

insert into p01_lv values (2,1);
insert into p01_lv values (1,1);
insert into p01_lv values (1,2);
insert into p01_lv values (5,1);

alter table p01_parcela enable constraint P01_PARCELA_FK3 ;

insert into p01_vlastni values (2,1,1,1,2);
insert into p01_vlastni values (2,1,4,1,2);
insert into p01_vlastni values (1,1,1,1,1);
insert into p01_vlastni values (1,2,1,1,3);
insert into p01_vlastni values (1,2,5,1,3);
insert into p01_vlastni values (1,2,3,1,3);
insert into p01_vlastni values (5,1,4,1,1);
