Klasa `LinkeList` jest kolekcją obiektów dowolnego typu, spełniającą następujące wymagania:
* przechowuje obiekty w ustalonej kolejnosci
* umożliwa odczyt liczby elementów w kolekcji przy użyciu wbudowanej funkcji `len()`
* umożliwia rozszerzenie kolekcji przez dodanie elementu na jej końcu
* udostępnia obiekt o podanym indeksie, w przypadku niepoprawnego indeksu zgłoszany jest wyjątek `IndexError`
* umożliwia iterowanie po obiektach w kolekcji, np. w petli `for`
* udostępnia indeks obiektu w kolekcji, którego wartość jest równa podanej wartości. W przypadku, gdy w kolekcji nie ma obiektu o podanej wartości, zwracana jest liczba -1

