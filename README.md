# Keskustelufoorumi
Tietokantasovellus-kurssia varten tehty projekti. Aiheena keskustelufoorumi, johon pystyy kirjautumaan sisään, ja sisäänkirjautumisen jälkeen pystyy
listaamaan, lukemaan, kirjoittamaan, kommentoimaan viestiketjuja. Viestiketjuja luodessa pystyy niihin liittämään aiheeseen liittyvän tagin. Viestiketjuja pystyy hakemaan ainakin tagien ja kirjoittajan perusteella. 


Tämän hetken toiminnallisuus: 
Käyttäjän rekisteröinti, sisään -ja uloskirjautuminen. Lisäksi käyttäjä pystyy vaihtamaan salasanansa, ja poistamaan koko käyttäjän. Käyttäjä pystyy tarkastelemaan omaa profiiliaan, profiilisivulla tällä hetkellä käyttäjänimi, aika jolloin käyttäjä luotu, käyttäjän viestien määrä, sekä linkit käyttäjän poistoon sekä salasanan vaihtoon.

Keskusteluketjun aloitus kirjautuneena käyttäjänä. Keskusteluun pystyy liittämään tageja aiheista, joihin keskustelu liittyy (Tällä hetkellä täytyy olla vähintään 1 tagi joka väh. 5 merkkiä pitkä). Kaikkien keskustelujen listaaminen, yksittäisten keskustelujen näyttäminen ja kommentointi. Keskustelujen listaaminen tapahtuu tällä hetkellä viimeisen viestin mukaan (ketju jossa viimeisin viesti on ylimpänä). Ketjun viestien määrä näkyy myös listaussivulla. Käyttäjä pystyy poistamaan omia viestejä ja omia aloitettuja keskusteluja. Keskusteluja pystyy etsimään niiden tagien perusteella (esim. kaikki keskustelut, joiden jossain tagissa merkkijono "ta").

Admin käyttäjä pystyy lisäksi listaamaan kaikki käyttäjät, näyttämään kenen tahansa käyttäjän profiilin (jossa näkyy vain käyttäjänimi, päivä jona luotu, lähetettyjen viestien määrä). Lisäksi admin pystyy poistamaan minkä tahansa käyttäjän, keskustelun tai viestin.


Ohjelmassa on kahdet testikäyttöä varten luodut tunnukset, joista toinen admin käyttäjä toinen normaalikäyttäjä:


admin: 

    käyttäjätunnus: admin1
    salasana: password
    
normaalikäyttäjä:

    käyttäjätunnus: NormalUser1
    salasana: password1
    
Testattaessa ohjelmaa voi myös rekisteröidä uuden käyttäjän ja kirjautua sillä sisään. Käyttäjätunnuksen tulee olla vähintään 6 merkkiä pitkä, salasanan tulee olla vähintään 8 merkkiä pitkä. Lisäksi käyttäjänimen tulee olla uniikki. Muita rajoituksia ei ole.

[Heroku](https://murmuring-fortress-85968.herokuapp.com).

[User stories](https://github.com/RoopeNiemi/tsoha19-projekti/blob/master/Documentation/Userstories.md)

[Tietokantakaavio](https://github.com/RoopeNiemi/tsoha19-projekti/blob/master/Documentation/databaseschema.md)
