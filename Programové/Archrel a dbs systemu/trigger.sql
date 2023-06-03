drop sequence P01_OPSUB_SEQ;

create sequence P01_OPSUB_SEQ
start with 10 
minvalue 1
increment by 1;

drop trigger Trig;

create trigger Trig
before insert or update
on P01_OPSUB
for each row
declare
  id_rc number(6);
  chyba_v_RC EXCEPTION;
begin
  if inserting and (MOD(:new.RC,11)=0 and length(to_char(:new.RC))=10) or (length(to_char(:new.RC))=9) then
    select P01_OPSUB_SEQ.NEXTVAL into id_rc from DUAL;
    :new.ID:=id_rc;
  else raise chyba_v_RC; 
  end if;
  if updating and (MOD(:new.rc,11)<>0 and length(to_char(:new.RC))=10) or (length(to_char(:new.RC))<9) then
    raise chyba_v_RC; 
  end if;
end;
/
