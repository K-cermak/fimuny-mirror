Poupravena a sprehlednena verze puvodnich Laborek z PB151. Markdown. Edition 2017.

# 50

###Asembler: přiřazovací příkaz
Napište program v asembleru: Definujte proměnné 'x6c' a 'y60' o velikosti bajtu. Proměnným můžete a nemusíte definovat obsah. Při testování správnosti řešení si bude IS sám obsahy do proměnných vkládat. Proveďte přiřazení
y60 := x6c
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec93'.

```
x6c	db 		; definuj bajtovou promennou
y60	db
	lda 	x6c 	; nacti z pameti do registru A
	sta	y60 	; nacti z registru do pameti
konec93 HLT
```
___

# 51

###Asembler: vložení konstanty do registru
Napište program v asembleru: Vložte konstantu 236 do registru H.
Pseudoinstrukcí DB s návěštím 'konstc5' vložte do paměti hodnotu 236. Instrukcí LDA pak vložte obsah adresy konstc5 do registru A a následně instrukcí MOV zkopírujte obsah registru A do registru H.

Program ukončete instrukcí HLT, kterou označíte návěštím 'konece3'.

```
konstc5	db	236
	lda	konstc5
	MOV	h, a 	; registry: zkopiruj z A do H
konece3 HLT
```
___

# 52

###Asembler: přesuny mezi registry
Napište program v asembleru: Definujte bajtovou proměnnou vzor891. Obsah proměnné vzor891 zkopírujte do všech registrů A, B, C, D, E, H, L vyjma registru E.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec03'.

```
vzor891 db
	lda	vzor891
	MOV	B,A 	; tady zacina kopirovani
	MOV	C,A
	MOV	D,A
	MOV	H,A
	MOV	L,A
konec03 HLT
```
___

# 53

###Asembler: zvýšení hodnoty registru o jedničku (inkrementace)
Napište program v asembleru: Definujte bajtovou proměnnou 'udajaa'. Zkopírujte obsah proměnné 'udajaa' do registru E a zvyšte obsah registru E o jedničku (inkrementujte obsah registru).
Program ukončete instrukcí HLT, kterou označíte návěštím 'konecce'.

```
udajaa	db
	lda	udajaa
	MOV	e, a
	inr	e 	; e := e+1
konecce	HLT
```
___

# 54

###Asembler: zvýšení hodnoty proměnné o jedničku
Napište program v asembleru: Definujte bajtovou proměnnou 'udajfd'. K obsahu proměnné 'udajfd' přičtěte jedničku.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec6b'.

```
udajfd	db
	lda	udajfd 	; nacti promennou do A
	inr	a 	; A := A+1
	sta	udajfd 	; A do pameti
konec6b HLT
```
___

# 55

###Asembler: sčítání bajtových hodnot
Napište program v asembleru: Definujte bajtové proměnné 'suma15', 'scit16' a 'scitc0'. K obsahu proměnné 'suma15' přičtěte obsahy dalších dvou proměnných. Případné přeplnění neřešte.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec23'.

```
suma15	db 		; definice promennych
scit16	db
scitc0	db
	lda	scit16 	; nacti promennou 1
	mov     b, a 	; zkopiruj ji do B
	lda     scitc0 	; nacti promennou 2
	add     b 	; pricti B k A (v A je ted soucet prvnich 2 promennych)
	mov     b, a 	; prepis soucet do b
	lda     suma15 	; nacti do A promennou pro soucet (prazdna)
	add     b 	; pricti k ni B (soucet)
	sta     suma15 	; uloz soucet do pameti
konec23	HLT
```
___

# 56

###Asembler: inverze bitů obsahu registru
Napište program v asembleru: Definujte bajtovou proměnnou 'cislod9'. Obsah proměnné 'cislod9' zkopírujte do registru H. Obsahu registru H invertujte hodnotu všech bitů.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec40'.

puvodni verze z fi.muny.cz
```
cislod9	db 		; definice promenne 1
cislo	db	255 	; definice promenne 2 s primym prirazenim hodnoty
	lda	cislod9	; nacti promennou 1 do A
	mov	h, a 	; zkopiruj ji do H
	lda	cislo 	; nacti promennou 2 do A
	xra	h 	; proved XOR obsahu v [] a A
	mov	h, a
konec40	HLT
```

jina varianta, bez zbytecnosti :)
```
cislod9	db
	lda	cislod9
	mov	h, a
	cma 		; doplnek registru A
	mov	h, a
konec40	HLT
```
___

# 57

###Asembler: změna znaménka bajtové proměnné
Napište program v asembleru: Definujte bajtovou proměnnou 'cislob3'. Obsahu proměnné 'cislob3' změňte znaménko. Tzn. z hodnoty např. 5 vytvořte -5. Zobrazujete čísla ve dvojkovém doplňkovém kódu.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konecae'.

```
cislob3	db
	lda	cislob3
	cma
	inr 	a 	; ted je v A (¬A)+1
	sta 	cislob3
konecae	hlt
```
___

# 58

###Asembler: nastavování příznaků SF (sign) a ZF (zero)
Napište program v asembleru: Definujte bajtovou proměnnou 'cislo43'. Nastavte příznaky SF a ZF příznakového registru tak, aby odpovídaly hodnotě obsahu proměnné 'cislo43'. Tzn. SF nastavte na 1, pokud je hodnota 'cislo43' záporná, ZF nastavte na 1, pokud je hodnota 'cislo43' nulová atd. Příznaky nastavují aritmetické operace podle výsledku operace. Použijte např. přičtení hodnoty 0. (pozn.: vyuzito)
Program ukončete instrukcí HLT, kterou označíte návěštím 'konecac'.

```
cislo43	db
	mvi 	b, 0 	; prirazeni 0, priznaky Z=1, S=1
	lda	cislo43
	add	b
konecac	HLT
```
___

# 59

###Asembler: nastavení příznaku CF (carry, z nejvyssiho radu) a vynulování AF (auxiliary carry, prenos mezi 3. a 4. bitem)
Napište program v asembleru: Definujte bajtovou proměnnou 'cislob2' a přiřaďte jí počáteční hodnotu 0e1h. K hodnotě proměnné 'cislob2' přičtěte takovou hodnotu, která způsobí nastavení CF=1 a AF=0.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec67'.

```
cislob2	db	0e1h
pricti	db	e0h 	; napoveda - mrkni na binarni tvar
	lda	pricti
	mov	b, a
	lda	cislob2
	add	b
konec67	hlt
```
___

# 60

###Asembler: vynulování příznaku CF a nastavení AF (viz predtim)
Napište program v asembleru: Definujte bajtovou proměnnou 'cislo5d' a přiřaďte jí počáteční hodnotu 9eh. K hodnotě proměnné 'cislo5d' přičtěte takovou hodnotu, která způsobí nastavení CF=0 a AF=1.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec4b'.

```
cislo5d	db	9eh
cislo	db	ch
	lda	cislo
	mov	b, a
	lda	cislo5d
	add	b
konec4b HLT
```
___

# 61

###Asembler: nastavení příznaku parity
Napište program v asembleru: Nastavte příznak parity PF=1.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec23'.

```
argh	db	7	; z cisel kolem 10: max 7, liche
abcd	db	10 	; z cisel kolem 10: min 10, sude
	lda	argh
	mov	b, a
	lda	abcd
	add	b
konec23	hlt
```
___

# 62

###Asembler: testování shody
Napište program v asembleru: Definujte bajtové proměnné 'x71f' a 'y7c5'. Porovnejte hodnoty proměnných 'x71f' a 'y7c5' a pokud se shodují, zvyšte obsah registru E o jedničku.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec88'.

```
x71f	db
y7c5	db
	lda	x71f
	mov	b, a
	lda	y7c5
	cmp	b 	; srovnej B s A
	jnz	konec88	; pokud Z=0, prejdi na konec
	inr	e 	; e := e+1
konec88	hlt
```
___

# 63

###Asembler: testování neshody
Napište program v asembleru: Definujte bajtové proměnné 'x7c9' a 'y856'. Porovnejte hodnoty proměnných 'x7c9' a 'y856' a pokud se neshodují, zvyšte obsah registru L o jedničku.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec23'.

```
x7c9	db
y856	db
	lda	x7c9
	mov	c, a
	lda	y856
	cmp	c
	jz	konec23
	inr	l
konec23	HLT
```
___

# 64

###Asembler: detekce přeplnění při sčítání celých čísel bez znaménka

####Výklad
*Čísla bez znaménka jsou celá kladná čísla s rozsahem zobrazení <0;2n-1>, kde n je počet bitů, ve kterých je číslo uloženo. Např. v bajtu ukládáme čísla bez znaménka v intervalu <0;255>. Přeplnění je stav, kdy výsledek aritmetické operace např. sčítání spadá mimo rozsah zobrazení. Pokud ukládáme neznaménková čísla v bajtech, nesmí být výsledek větší než 255. Výsledek větší než 255 se projeví nastavením příznaku Carry Flag (CF).
Proto testování přeplnění v případě aritmetiky s čísly bez znaménka se provádí testováním hodnoty příznaku CF.*

Napište program v asembleru: Definujte bajtové proměnné 'xe23' a 'yd57'. Předpokládejte, že v proměnných jsou uložena čísla bez znaménka. Obsah proměnných sečtěte a rozhodněte, zda došlo k přeplnění. Pokud došlo k přeplnění, zastavte program instrukcí HLT označenou návěštím 'ovrflw7'. Pokud k přeplnění nedošlo, zastavte program instrukcí HLT označenou návěštím 'konece1'.

```
xe23	db
yd57	db
	lda	xe23
	mov	b, a
	lda	yd57
	add	b
	jnc 	konece1	; pokud neni overflow, t.j. CF=0, skoc na konec
ovrflw7 HLT
konece1	HLT
```
___

# 65

###Asembler: detekce přeplnění při odčítání celých čísel bez znaménka
####Výklad
*Testování přeplnění v případě aritmetiky s čísly bez znaménka se provádí testováním hodnoty příznaku CF.
Pro odčítání použijte instrukci ```SUB registr```, která od registru A odečte obsah uvedeného registru.*

Napište program v asembleru: Definujte bajtové proměnné 'x637' a 'y962'. Předpokládejte, že v proměnných jsou uložena čísla bez znaménka. Odečtěte obsahy 'x637' - 'y962' a rozhodněte, zda došlo k přeplnění. Pokud došlo k přeplnění, zastavte program instrukcí HLT označenou návěštím 'ovrflw4'. Pokud k přeplnění nedošlo, zastavte program instrukcí HLT označenou návěštím 'konec5e'.

```
x637	db
y962	db
	lda	y962
	mov	b, a
	lda	x637
	sub	b
	jnc	konec5e
ovrflw4	hlt
konec5e	hlt
```
___

# 66

###Asembler: testování ostře menší než (znaménkem výsledku)
Napište program v asembleru: Definujte bajtové proměnné 'x057' a 'yaa9'. Porovnejte hodnoty proměnných 'x057' a 'yaa9' pomocí testování znaménka výsledku po odečtení hodnot proměnných. Předpokládejte, že proměnné obsahují čísla se znaménkem v dvojkovém doplňkovém kódu. Pokud jsou obsahy x057 < yaa9, vložte do registru E hodnotu 1, jinak vložte do registru E hodnotu 2.
Pro testování správnosti řešení se použijí čísla v intervalu <-64;63>, aby při odečtení jakýchkoli dvou čísel nemohlo dojít k přeplnění a nebylo chybně ovlivněno znaménko výsledku.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec78'.

```
x057	db
yaa9	db
	lda	yaa9
	mov	b, a
	lda	x057
	cmp	b
	jm 	ano 	; pokud je vysledek zaporny, skoc na ano
ne	mvi	e, 2 	; tady neni nutna navest "ne"
	jmp	konec78	; skoc na konec
ano 	mvi	e, 1
konec78 HLT
```
___

# 67

###Asembler: testování menší nebo rovno (znaménkem výsledku)
Napište program v asembleru: Definujte bajtové proměnné 'x116' a 'ye24'. Porovnejte hodnoty proměnných 'x116' a 'ye24' pomocí testování znaménka výsledku po odečtení hodnot proměnných. Předpokládejte, že proměnné obsahují čísla se znaménkem v dvojkovém doplňkovém kódu. Pokud jsou obsahy x116 ≤ ye24, invertujte všechny bity registru L, jinak ponechte obsah registru L beze změny.
Pro testování správnosti řešení se použijí čísla v intervalu <-64;63>, aby při odečtení jakýchkoli dvou čísel nemohlo dojít k přeplnění a nebylo chybně ovlivněno znaménko výsledku.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec78'.

```
x116	db
ye24	db
	lda	x116
	mov	c, a
	lda	ye24
	cmp	c
	jm	konec78
bud	mov	a, l
	cma
	mov	l, a
konec78	HLT
```
___

# 68

###Asembler: testování ostře větší než (znaménkem výsledku)
Napište program v asembleru: Definujte bajtové proměnné 'xdab' a 'y02e'. Porovnejte hodnoty proměnných 'xdab' a 'y02e' pomocí testování znaménka výsledku po odečtení hodnot proměnných. Předpokládejte, že proměnné obsahují čísla se znaménkem v dvojkovém doplňkovém kódu. Pokud jsou obsahy xdab > y02e, změňte znaménko čísla ve dvojkovém doplňkovém kódu v registru B, jinak ponechte obsah registru B beze změny.
Pro testování správnosti řešení se použijí čísla v intervalu <-64;63>, aby při odečtení jakýchkoli dvou čísel nemohlo dojít k přeplnění a nebylo chybně ovlivněno znaménko výsledku.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec11'.

```
xdab	db
y02e	db
	lda	xdab
	mov	c, a
	lda	y02e
	cmp	c
	jp	konec11
alebo:	mov	a, b
	cma
	inr	a
	mov	b, a
konec11	HLT
```
___

# 69

###Asembler: testování větší nebo rovno (znaménkem výsledku)
Napište program v asembleru: Definujte bajtové proměnné 'x714' a 'y9c0'. Porovnejte hodnoty proměnných 'x714' a 'y9c0' pomocí testování znaménka výsledku po odečtení hodnot proměnných. Předpokládejte, že proměnné obsahují čísla se znaménkem v dvojkovém doplňkovém kódu. Pokud jsou obsahy x714 ≥ y9c0, zvyšte obsah registru C o hodnotu 144 (na případné přeplnění neberte ohled), jinak ponechte obsah registru C beze změny.
Pro testování správnosti řešení se použijí čísla v intervalu <-64;63>, aby při odečtení jakýchkoli dvou čísel nemohlo dojít k přeplnění a nebylo chybně ovlivněno znaménko výsledku.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec71'.

```
x714	db
y9c0	db
zvys	db	144
	lda	zvys
	mov	d, a
	lda	y9c0
	mov	b, a
	lda	x714
	cmp	b
	jm	konec71
; alebo:
	mov 	a, c
	ADD	d
	mov	c, a
konec71	HLT
```
___

# 70

###Asembler: detekce přeplnění při sčítání celých čísel se znaménkem
Detekce přeplnění při aritmetice ve dvojkovém doplňkovém kódu je implementována je až ve vyšších procesorech. Pro řešení tohoto úkolu použijte rozšířený režim emulátoru ADV OF.
Napište program v asembleru: Zapněte rozšířený režim emulátoru pseudoinstrukcí	```adv of```.
Definujte bajtové proměnné 'xd5a' a 'y8fc'. Předpokládejte, že v proměnných jsou uložena čísla se znaménkem ve dvojkovém doplňkovém kódu. Obsah proměnných sečtěte a rozhodněte, zda došlo k přeplnění. Pokud došlo k přeplnění, zastavte program instrukcí HLT označenou návěštím 'ovrflw9'. Pokud k přeplnění nedošlo, změňte znaménko proměnné 'xd5a' a zastavte program instrukcí HLT označenou návěštím 'konec98'.

```
	adv of
xd5a	db
y8fc	db
	lda	xd5a
	mov	b, a
	lda	y8fc
	add	b
	jo	ovrflw9
nebud	lda	xd5a
	cma	a
	inr	a
	sta	xd5a
	jmp	konec98
ovrflw9	HLT
konec98	HLT
```
___

# 71

###Asembler: porovnání velikosti čísel bez znaménka
Plnohodnotné porovnávání velikosti čísel (bez rizika ovlivnění výsledku případným přeplněním vzniklým při odčítání) je složitější problematika. Implementována je až ve vyšších procesorech.
Pro řešení tohoto úkolu použijte rozšířený režim emulátoru ADV OF.
Napište program v asembleru: Zapněte rozšířený režim emulátoru pseudoinstrukcí	```adv of```.
Definujte bajtové proměnné 'x0a9' a 'y4bb'. Použijte instrukci podmíněného skoku ze sady instrukcí rozšířeného režimu a porovnejte neznaménkově hodnoty proměnných ```x0a9 < y4bb```.
Předpokládejte, že proměnné obsahují celá kladná čísla bez znaménka.
Pokud jsou obsahy proměnných v požadované relaci, ukončete program instrukcí HLT s návěštím 'anoe8'. Pokud nesplňují požadovanou relaci, ukončete program instrukcí HLT s návěštím 'nee8'.


```
	adv of
y4bb	db
x0a9	db
	lda	y4bb
	mov	b, a
	lda	x0a9
	cmp	b
	jnb	nee8
anoe8	HLT
nee8	HLT
```
___

# 72

###Asembler: porovnání velikosti čísel se znaménkem
Plnohodnotné porovnávání velikosti čísel se znaménkem (bez rizika ovlivnění výsledku případným přeplněním vzniklým při odčítání) je složitější problematika a vyžaduje implementaci detekce přeplnění v příznaku OF (Overflow Flag). Implementována je až ve vyšších procesorech.
Pro řešení tohoto úkolu použijte rozšířený režim emulátoru ADV OF.
Napište program v asembleru: Zapněte rozšířený režim emulátoru pseudoinstrukcí ```adv of```
Definujte bajtové proměnné 'xc7f' a 'y1bd'. Použijte instrukci podmíněného skoku ze sady instrukcí rozšířeného režimu a porovnejte znaménkově hodnoty proměnných ve dvojkovém doplňkovém kódu ```xc7f ≤ y1bd```
Předpokládejte, že proměnné obsahují celá čísla se znaménkem ve dvojkovém doplňkovém kódu.
Pokud jsou obsahy proměnných v požadované relaci, nastavte obsah registru H na hodnotu 1 a ukončete program instrukcí HLT s návěštím 'ano04'. Pokud nesplňují požadovanou relaci, nastavte obsah registru H na hodnotu 2 a ukončete program instrukcí HLT s návěštím 'ne04'.

```
	adv of
y1bd	db
xc7f	db
	lda	y1bd
	mov	b, a
	lda	xc7f
	cmp	b
	jle	var1
var2	mvi	H,2
	jmp	ne04
var1	mvi	H,1
	jmp	ano04
ano04	HLT
ne04	HLT
```
___

# 73

###Asembler: použití registrů H, L a M
####Výklad
*Procesor Intel 8080 disponuje zvláštním 8bitovým registrem M. Pokud vložíte hodnotu do registru M, zapíše se do paměti na adresu uloženou ve dvojici registrů H a L (vyšší bajt adresy v H a nižší v L). Podobně pokud čtete obsah registru M, přečtete obsah bajtu z paměti z adresy uložené v registru H a L.
Registr M používáte stejně, jako používáte registry B, C, D, E, H, L. Např. v instrukci MOV M,B.
Vyzkoušejte si instrukci LXI pro plnění dvojice registrů 16bitovou konstantou. Používá se např.
	```LXI B,65535	; Naplní dvojici registrů B,C 16bitovou konstantou 65535
	LXI D,65535	; Naplní dvojici registrů D,E 16bitovou konstantou 65535
	LXI H,65535	; Naplní dvojici registrů H,L 16bitovou konstantou 65535
	LXI SP,65535	; Naplní registr SP 16bitovou konstantou 65535
	```*
Napište program v asembleru:
1. Naplňte dvojici registrů H a L 16bitovou hodnotou 2240. Zkopírujte obsah registru B do registru M (tj. do paměti na adresu 2240).
2. Dále naplňte dvojici registrů H a L 16bitovou hodnotou 33991. Zkopírujte obsah registru M do registru C (tj. zkopírujte obsah adresy 33991 do registru C).
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec84'.

```
	LXI	H, 2240	; nacti 16 bitu do H, L
	MOV	M, B
	LXI	H, 33991
	MOV	C, M
konec84	HLT
```
___

# 74

###Asembler: sčítání 16bitových čísel
####Výklad
*Pro sčítání čísel, které jsou širší (jsou uloženy na více bitech) než je procesorem běžně zpracovávaná šířka dat, bývá k dispozici dvojice instrukcí **ADD** a **ADC**. Instrukce **ADD** klasicky sečte dva bajty a případný přenos vloží do příznaku CF (Carry Flag). Instrukce **ADC** sečte dva bajty a ještě k nim přičte hodnotu příznaku CF; a také případný přenos vloží do příznaku CF. Vícebajtové hodnoty pak sčítáme po jednotlivých bajtech. Nejprve sečteme instrukcí ADD bajty nejnižších řádů a dostaneme součet a přenos. Pak instrukcí ADC sečteme dvojici vyšších bajtů s přičtením přenosu z nejnižšího bajtu. Pokud by byly sčítance více než dvoubajtové, operaci s instrukcí ADC opakujeme pro všechny vyšší bajty.
Vizte schéma použití instrukcí ADD a ADC na tomto obrázku (obrázek popisuje 16bitový procesor, proto se nesčítá po bajtech).
V operační paměti jsou vícebajtová slova uložena ve tvaru Little-Endian, tzn. na nižší adrese bajt nižšího řádu.*

Napište program v asembleru: Definujte bajtové proměnné 'xlow3f', 'xhigh3f', 'ylow3f', 'yhigh3f', 'zlow3f', 'zhigh3f'. Dvojici proměnných 'xlow3f' a 'xhigh3f' musíte umístit bezprostředně vedle sebe ve správném pořadí (Little-Endian). Stejně tak dvojici proměnných 'ylow3f' a 'yhigh3f'; a dvojici proměnných 'zlow3f' a 'zhigh3f'.
Sečtěte 16bitové číslo umístěné ve dvojici proměnných 'xlow3f', 'xhigh3f' s 16bitovým číslem umístěným ve dvojici proměnných 'ylow3f', 'yhigh3f'. Výsledné 16bitové číslo vložte do dvojice proměnných 'zlow3f', 'zhigh3f'.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec46'.
Testovací hodnoty budou přiřazovány takové, aby nedošlo k přeplnění.

```
xlow3f	db 		; definice promennych
xhigh3f	db
ylow3f	db
yhigh3f	db
zlow3f	db
zhigh3f	db
	lda	xlow3f 	; nacitani a posuny
	mov	b, a
	lda	xhigh3f
	mov	c, a
	lda	ylow3f
	mov	d, a
	lda	yhigh3f
	mov	e, a
	lda	zlow3f
	mov	h, a
	lda	zhigh3f
	mov	l, a
	lda	xlow3f
	add	d
	sta	zlow3f
	lda	xhigh3f
	adc	e
	sta	zhigh3f
konec46	HLT
```
___

# 75

###Asembler: operace prováděné v cyklu
Napište program v asembleru: Definujte bajtovou proměnnou 'kolikb4'. V paměti od adresy, která je jako 16bitové číslo uložena v registrech H, L, naplňte tolik bajtů, kolik je uloženo v bajtové proměnné 'kolikb4', hodnotou 161.
Tzn., že na adresu dle H, L pomocí registru M vložíte do paměti hodnotu 161. Pak adresu v registrech H, L zvýšíte o jedničku (nutno použít ADD a ADC; instrukce INR nenastavuje CF). A celý cyklus opakujete tolikrát, kolikrát je uloženo v bajtové proměnné 'kolikb4'.
Vlastní program musíte umístit od začátku operační paměti do prvních 100 bajtů. Při kontrole programu se do H, L budou vkládat náhodná čísla větší než 100.
Pokud 'kolikb4' obsahuje 0, pak se nesmí nastavit žádný obsah.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec48'.

```
kolikb4	db
i	db	1
a1	db	0
a3	db	161
	lda	i
	mov	b, a
	mov	c, a
	lda	a1
	mov	d, a
	mvi	e, 1
	lda	kolikb4
skok	cmp	b
	jm 	konec48
; blok
	dcr	a
	sta	kolikb4
	lda	a3
	mov	m,a
	dad	d
	lda	kolikb4
	jmp 	skok
konec48	HLT
```
___

# 76

###Asembler: záměna obsahů registrů pomocí zásobníku
Napište program v asembleru: Nastavte vrchol zásobníku na adresu 18332. Pomocí operací PUSH a POP vzájemně zaměňte obsahy registrů H, L s registry B, C.
Mj. se kontroluje, zda všechny 4 zaměňované hodnoty byly vloženy do zásobníku od dna zásobníku.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konecfa'.

```
	LXI	SP, 18332
	PUSH	H
	PUSH	B
	POP	H
	POP	B
konecfa	HLT
```
___

# 77

###Asembler: použití volání podprogramu
Napište program v asembleru: Definujte bajtové proměnné 'wd39', 'x5ed', 'yf42', 'ze5b'. Od proměnné 'wd39' odečtěte obsahy proměnných 'x5ed', 'yf42', 'ze5b'; tj. spočítejte wd39-x5ed-yf42-ze5b. Výsledek dejte do registru B.
Zaveďte podprogram s návěštím 'odecti0', který změní znaménko obsahu registru A, přičte k A obsah registru B a zkopíruje součet z registru A do registru B. Podprogram musíte kvůli principu fungování emulátoru umístit až na konec programu, protože emulátor hledá první výkonnou instrukci a na tu předá řízení. Váš program by nefungoval, kdyby emulátor začal voláním podrogramu.

Aplikujte toto schéma programu:

1. definujte proměnné 'wd39', 'x5ed', 'yf42', 'ze5b',
2. do registru B vložte obsah proměnné 'wd39',
3. do registru A vložte obsah proměnné 'x5ed',
4. zavolejte podprogram 'odecti0',
5. do registru A vložte obsah proměnné 'yf42,
6. zavolejte podprogram 'odecti0',
7. do registru A vložte obsah proměnné 'ze5b,
8. zavolejte podprogram 'odecti0',
9. ukončete program instrukcí HLT, kterou označíte návěštím 'konec23',
10. definujte podprogram 'odecti0', který změní znaménko obsahu registru A, přičte k A obsah registru B a zkopíruje součet z registru A do registru B.
Program ukončete instrukcí HLT, kterou označíte návěštím 'konec23'.
Případné přeplnění neřešte. Registr SP nenastavujte, tzn. nechte uplatnit implicitní hodnotu 0.

```
wd39	db
x5ed	db
yf42	db
ze5b	db
	lda	wd39
	mov	b, a
	lda	x5ed
	call	odecti0
	lda	yf42
	call	odecti0
	lda	ze5b
	call	odecti0
konec23	HLT
odecti0:CMA
	inr	a
	add	b
	mov	b, a
	RET
```
