9 otázek, max 100b

## 1
- Rozdíly mezi CISC a RISC procesory, popsat RISC
  - Ktery znich vyzaduje vetsi podporu prekladace?
  - Premenovavanie registrov v RISC, aku to ma vyhodu? (proč má RISC tolik registrů?)
  - Jak RISC procesory řeší odložené skoky?
- Pipelining, co to je, vlastnosti.
- ANDES - co to je, proč vznikl. Jaky problem resi?
- Optimalizácia prístupu do pamäte, ako vieme z hľadiska prekladača optimalizovať prístupy?**x**
- Vlastnosti hlavnej pamati.

## 2 
- SIMD, MIMD popsat, rozdil mezi nimi. Kam byste zařadili cluster
- Sdilena a distibuovana pamet, rozdiely, spolecne vlastnosti.**x**
- Zneplatnění vs update cache
- Pamate, ake su typy cache vypadky v jednoprocesoroch a viacprocesorovych pc.
- Co to je koherence paměti, jak se zajišťuje, jaké jsou na to způsoby.
- Cache mapovatelne adresare typy + popis.

- čo rozumiete pod pojmom rošíriteľnosž a zrýchlenie?
- Co rozumíte pod pojmem zrychlení a přínos.
__Propojovacı́ sı́tě__
- Popíšte rôzne parametre sietí. čo je bisection width? Vysvetlite a načrtnite príklad na obrázku
  - Jaké jsou charakteristiky propojení paralelních systému, co to znamená bisection width.
  - Vlastnosti propojení u sítí + dvourozměrné (jaké znáte + jejich vlastnosti)

- Jak ukryjeme zpoždění u propojovacích sítí, nějaká změna modelu nebo co...
__Pamet__
- Jak schovat pomalou pamet pomoci slabe konzistence?
- optimalizace přístupu do paměti
- Skrytie opozdenia pomocou prefetch a producentom iniciovanej komunikacie.
__Synchronizace__
- test-and-test-n-set instrukce
- popíšte rozdiel test&set + test&test&set a k čomu slúži + problémy s tým spojené
- test_and_set a test_and_test_and_set a algoritmus, jak se dá vyřešit problém těchto instrukcí (asi -tím byla myšlena fronta procesů),

## 3
- Optimalizace cyklů, Jsou optimalizace závislé na programovacím jazyce?
- Jaké jsou optimalizace cyklů z hlediska datové závislosti. 
- Jednoduche optimalizacie kodu (nie cyklov) pre paralelne pc.
- optimalizace cyklů + nějaké problémy s tím

## 4
- Profilery. uvest jejich druhy a co byste od kazdeho z techto druhu ocekavali (heslovite)?
  (asi proc/block oriented, pocet volani, cas, vypadky pameti, …)
- Vysvetlite k čomu slúžia SPEC kernel a čo to je v kontexte benchmarku
- Na jakém principu stavějí benchmarky SPEC?
- Co to je kernel ve SPEC benchmarku a proč se rozděluje SPEC do kernelů.

## 5,6
- (Skupinová) Komunikace v PVM
- PVM a sprava procesu

- Co je to komunikator v MPI a co řeší za problém z PVM (globalni tagy, ktere delaji problem pri definici nezavislych knihoven -> clashing)
- MPI jeho vlastnosti hlavne ohledne zasilani zprav. Jake moznosti nabizi pro zasilani zprav.

- MPI a blokující/neblokující volání a závislost s využitím bufferů **x**
- MPI point-to-point komunikácia, vysvetlite + popisy v závislosti na bufferi
- Co jsou to kolektivní operace v MPI a proč je MPI zavádí? Uveďte příklady kolektivních operací.
**************************************************************************
## Zbytek
- Co je to CUDA, popis vyznam hierachie vlaken a pamati.
- Rozdíl mezi CPU a GPU

