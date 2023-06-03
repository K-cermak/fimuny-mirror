// odkaz na pastebin: http://pastebin.com/4T4mB3eL

/*
ZADANI ULOHY - zkouskovy priklad z 11. 1. 2012

Napiste zdrojovy kod v jazyce C++ pro spustitelny program (tj. vcetne funkce main),
ktery bude obsahovat funkci raiseIfIntersect(). Funkce raiseIfIntersect() nalezne
alespon jeden sdileny shodny prvek. Vyjimka bude obsahovat popis, ktera sdilena
polozka byla nalezena. Pokud zadna sdilena polozka nalezena neni, funkce skonci bez vyjimky.

- Hlavicka funkce a zpusob jeji implementace je na vasi volbe, bude ale dodrzovat doporucene
postupy probirane v ramci semestru (tj. mate volnost v implementaci, ale kod musi byt slusne napsan).

- Kontejner bude do funkce predan referenci.

- Kod ve funkci main ukaze vhodnym zpusobem pouziti funkce raiseIfIntersect() na
kontejnerech obsahujici alespon 20 polozek tak, aby jednou doslo k volani vyjimky a podruhe nikoliv.

- Vyjimka bude zachycena a vypsana ve funkci main.

- Kontejner bude v zakladni verzi obsahovat celociselne polozky. Dalsi 3 body budou udelene v pripade,
ze bude kod funkce raiseIfIntersect() implementovan jako sablona.

- Program nesmi obsahovat memory leaks.

- V komentarich diskutujte zpusob implementace.

- Drobne preklepy a detaly branici prekladu nebudou penalizovany - dulezity je kotektni princip
implementace (vyuzijte komentaru pro snizeni nejasnosti). Tj. i neprelozitelny program muze ziskat
plny pocet bodu, pokud bude principialne spravny.
*/

/*
POZNAMKA

V kodu jsou nektere veci nad ramec zadani, slouzi k procviceni a uloha je obsahovat nemusi.
Tento kod je v komentari oznacen prefixem B:
*/

#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm> // B: STL algoritmy
#include <stdexcept> // vyjimky (dedime z runtime_error)

// nadefinovani vlastni vyjimky
class SameException : public std::runtime_error {
public:
	SameException(const std::string name = "", const std::string& reason = "Byly nalezeny dve shodne polozky: ") : std::runtime_error(reason+name) {};
	~SameException() throw() {}
};

// B: functor (pricitac neceho)
template <typename T>
class Adder {
private:
	T m_value;
public:
	Adder(T value) : m_value(value) {}
	void set(T value) {m_value = value;}
	T operator () (T value) {
		return m_value + value;
	}
};

// B: vypisovac obsahu kontejneru pro for_each algoritmus
template <typename T>
void print(T value) {
	std::cout << value << " ";
}

// funkce na vyhozeni vyjimky, pokud kontejnery obsahuji minimalne jednu stejnou polozku
template <typename T>
void raiseIfIntersect(std::vector<T>  &v1, std::vector<T> &v2) {
	typename std::vector<T>::iterator it1, it2;
	for(it1 = v1.begin(); it1 != v1.end(); it1++) {
		for(it2 = v2.begin(); it2 != v2.end(); it2++) {
			if(*it1 == *it2) {
				std::stringstream ss;
				ss << *it1;
				throw SameException(ss.str());
			}
		}
	}
}

int main(void) {

//	//B: prevod string -> int
//	std::string text = "10";
//	int a;
//
//	std::stringstream ss;
//	ss << text;
//	ss >> a;
//	std::cout << a << std::endl;

	std::vector<float> v1, v2;

	// inicializace kontejneru (tak, at neobsahuji stejne polozky)
	for(int i = 1; i <= 20; i++) {
		v1.push_back(i);
	}
	for(int i = 21; i <= 40; i++) {
		v2.push_back(i);
	}

	// pokud kontejnery neobsahuji dve shodne polozky, vyjimka se nevyhodi
	try {
		raiseIfIntersect<float>(v1, v2);
	} catch (SameException& ex) {
		std::cout << ex.what() << std::endl;
	}

	// B: pouziti functoru
	Adder<float> add(35);
	// B: zmena polozek prvniho kontejneru (aby kontejnery obsahovaly stejne polozky)
	// pozn. misto nasledujiciho radku lze jednoduse pouzit napr. v1.push_back(21);
	transform(v1.begin(), v1.end(), v1.begin(), add);

	// pokud kontejnery obsahuji dve shodne polozky, vyjimka se vyhodi
	try {
		raiseIfIntersect<float>(v1, v2);
	} catch (SameException& ex) {
		std::cout << ex.what() << std::endl;
	}

	// B: vypis obsahu kontejneru
	std::cout << std::endl;
	for_each(v1.begin(), v1.end(), print<float>);
	std::cout << std::endl;
	for_each(v2.begin(), v2.end(), print<float>);
	std::cout << std::endl;

	return 0;
}
