CREATE TABLE  vojaci (
	id_vojak number CONSTRAINT pk_id_vojak PRIMARY KEY,
	jmeno varchar2(30) NOT NULL,
	hodnost varchar2(15) NOT NULL
);

CREATE TABLE naboje (
	id_naboje NUMBER PRIMARY KEY,
	nazev varchar(20) not null, 
	pocetkusu NUMBER DEFAULT 0
);

CREATE TABLE zbrane (
	id_zbrane NUMBER PRIMARY KEY,
	id_naboje CONSTRAINT fk_id_naboje REFERENCES naboje(id_naboje),
	nazev VARCHAR2(25) NOT NULL,
	typ_zbrane varchar(15) check(typ_zbrane in ('pistole','autocna_zbran','brokovnice','puska'))
);

CREATE SEQUENCE vypujcka_seq INCREMENT BY 1 START WITH 1   NOCACHE NOCYCLE /;

CREATE TABLE vypujcka (
	id_vypujcka NUMBER PRIMARY KEY,
	id_vojaka CONSTRAINT fk_id_vojaka REFERENCES vojaci(id_vojak) NOT NULL,
	id_zbrane UNIQUE CONSTRAINT fk_id_zbrane REFERENCES zbrane(id_zbrane),
	cas DATE DEFAULT SYSDATE
);


/**trigger**/ /**pridava auto id k vypujce  -  je to mozna az moc jednoduchy trigger ale prosel**/
create or replace trigger vypujcka_autoid 
before insert
 on vypujcka 
 for each row 
 begin select vypujcka_seq.nextval 
 into :new.id_vypujcka from dual; end; 
 /
 


/** vojaci **/
INSERT INTO vojaci VALUES(1,'Prokop Buben','desatnik');
INSERT INTO vojaci(id_vojak,jmeno,hodnost) VALUES(2,'Tomas Dobry','vojin');
INSERT INTO vojaci VALUES(3,'Frantisek Maly','porucik');
INSERT INTO vojaci VALUES(4,'Aneta Mlcochova','general');
INSERT INTO vojaci VALUES(5,'Dalibor Novak','plukovnik');

/** naboje **/
INSERT INTO naboje VALUES(1,'xka 9mm', 5000);
INSERT INTO naboje VALUES(2,'brokX54', 400);
INSERT INTO naboje VALUES(3,'rtt 7mm', 2500);
INSERT INTO naboje VALUES(4,'pka 9mm', 400);

/** zbrane **/
INSERT INTO zbrane VALUES(1,1,'AK-47','autocna_zbran');
INSERT INTO zbrane VALUES(2,1,'M-16','autocna_zbran');
INSERT INTO zbrane VALUES(3,2,'SPAS','brokovnice');
INSERT INTO zbrane VALUES(4,3,'CZ 75','pistole');
INSERT INTO zbrane VALUES(5,4,'M95','puska');   
INSERT INTO zbrane VALUES(6,4,'M95','puska');   
INSERT INTO zbrane VALUES(7,3,'CZ 75','pistole');                                                                                                   

/** vypujcka **/

INSERT INTO vypujcka (id_vojaka,id_zbrane,cas) VALUES (1,1,'31-AUG-12');
INSERT INTO vypujcka (id_vojaka,id_zbrane,cas) VALUES (2,2,'25-SEP-13');
INSERT INTO vypujcka (id_vojaka,id_zbrane,cas) VALUES (3,4,'16-OCT-13');
INSERT INTO vypujcka (id_vojaka,id_zbrane,cas) VALUES (4,5,'03-OCT-12');
INSERT INTO vypujcka (id_vojaka,id_zbrane,cas) VALUES (4,6,'03-OCT-12');

/** select **/ 

/** pocet vojaku beze zbrane **/
Select count(id_vojak) as pocet_vojaku_bez_zbrane from vojaci where id_vojak not in (select id_vojaka from vypujcka);

/** vybere jmeno vojaka a pocet pridelenych zbrani vypis seradi podle poctu zbrani sestupne **/
SELECT vojaci.jmeno,COUNT(vypujcka.id_vojaka) AS PocetZbrani FROM Vojaci LEFT JOIN Vypujcka
ON Vypujcka.id_vojaka=vojaci.id_vojak
GROUP BY jmeno ORDER BY PocetZbrani DESC;

/** jmeno zbrane, pocet naboju, ktera neni pujcena a ma na sklade vice nez 300 naboju a jedna se o brokovnici**/
Select zbrane.nazev, naboje.pocetkusu FROM zbrane LEFT JOIN naboje
ON zbrane.id_naboje=naboje.id_naboje 
where id_zbrane in (SELECT id_zbrane FROM zbrane where id_zbrane not in (Select id_zbrane from vypujcka) and typ_zbrane = 'brokovnice') and pocetkusu>300;

/** jmeno a pocet zbrani u vojaku, kteri maji vice nez jednu zbran**/
SELECT Vojaci.jmeno, COUNT(vypujcka.id_vojaka) AS NumberOfOrders FROM vypujcka
INNER JOIN vojaci
ON vypujcka.id_vojaka=vojaci.id_vojak
GROUP BY jmeno
HAVING COUNT(vypujcka.id_vypujcka) > 1;


/**kurzor **/ /**vybere vsechny vojaky s hodnosti general a ulozi do zvlastni tabulky, nic lepsiho me nenapadlo O:-) 
sice to proslo ale chtelo by to asi lepsi priklad**/
Create table temp (id number, jmeno varchar(30), hodnost varchar(30) );
DECLARE
  CURSOR voj IS
    SELECT id_vojak, jmeno, hodnost FROM vojaci  where hodnost = 'general';
      v_id_vojak number;
      v_jmeno varchar2(30);
      v_hodnost varchar2(30);
BEGIN
  OPEN voj;
  LOOP
    FETCH voj INTO v_id_vojak, v_jmeno, v_hodnost;
    EXIT WHEN voj%NOTFOUND;
   
 INSERT INTO temp VALUES (v_id_vojak, v_jmeno, v_hodnost);
    COMMIT;
  END LOOP;
  CLOSE voj;
END;
/


SELECT * FROM temp ORDER BY hodnost DESC;



/** drop tables**/
DROP TABLE vojaci CASCADE CONSTRAINTS;
DROP TABLE naboje CASCADE CONSTRAINTS;
DROP TABLE zbrane CASCADE CONSTRAINTS;
DROP SEQUENCE vypujcka_seq;                      
DROP TABLE vypujcka CASCADE CONSTRAINTS;
