# Keskustelufoorumi
Tietokantasovellus-kurssia varten tehty projekti. Aiheena keskustelufoorumi, johon pystyy kirjautumaan sisään, ja sisäänkirjautumisen jälkeen pystyy
listaamaan, lukemaan, kirjoittamaan, kommentoimaan viestiketjuja. Lisäksi tarkoitus lisätä toiminnallisuus etsiä jonkin, esim aiheen tai kirjoittajan nimen perusteella.


Tämänhetkinen versio löytyy 
[täältä](https://murmuring-fortress-85968.herokuapp.com/auth/login).
Tämän hetken toiminnallisuus: 
Käyttäjän rekisteröinti, sisään -ja uloskirjautuminen. Lisäksi käyttäjä pystyy vaihtamaan salasanansa, ja poistamaan koko käyttäjän. Käyttäjä pystyy tarkastelemaan omaa profiiliaan, profiilisivulla tällä hetkellä käyttäjänimi, aika jolloin käyttäjä luotu, käyttäjän viestien määrä, sekä linkit käyttäjän poistoon sekä salasanan vaihtoon.

Käyttäjätunnuksen tulee olla vähintään 6 merkkiä pitkä, salasanan tulee olla vähintään 8 merkkiä pitkä. Lisäksi käyttäjänimen tulee olla uniikki (uniikin käyttäjän tapauksessa virheen hallintaa ei vielä ole, tulee vain error jos käyttäjä on jo olemassa). Muita rajoituksia ei ole.

Kaikkien keskustelujen listaaminen, yksittäisten keskustelujen näyttäminen ja kommentointi. Keskustelujen listaaminen tapahtuu tällä etkellä viimeisen viestin mukaan (ketju jossa viimeisin viesti on ylimpänä). Ketjun viestien määrä näkyy myös listaussivulla. 
