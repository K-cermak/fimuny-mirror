alter table P01_OPSUB disable constraint P01_OPSUB_PK cascade;

insert into p01_opsub values
(4,NULL,7401084680,NULL,NULL,'Riha','Zdenek','Mgr.','',1,1,2,498);

insert into p01_opsub values
(4,NULL,7401084669,NULL,NULL,'Riha','Zdenek','Mgr.','',1,1,2,498);

insert into p01_opsub values
(6,NULL,7401084669,NULL,NULL,'Riha','Zdenek','Mgr.','',1,1,2,498);

insert into p01_opsub values
(6,NULL,7401084669,NULL,NULL,'Riha','Zdenek','Mgr.','',1,1,2,498);

-- P03 - a) 
select ID
  from P01_OPSUB,
   (select ID ID_DOUBLE
     from P01_OPSUB
     group by ID having count(*)>1) duplikaty
  where id=duplikaty.id_double;

-- P03 - b)
(select id, rowid from p01_opsub)
minus
(SELECT id,MIN(rowid) AS rad FROM P01_OPSUB GROUP BY id);

-- P03 - c)
delete from P01_OPSUB where rowid = ANY ((select rowid from 
P01_OPSUB) minus (SELECT MIN(rowid) AS rad FROM P01_OPSUB GROUP BY   
id));

-- P03 - d)
alter table P01_OPSUB enable constraint P01_OPSUB_PK;
