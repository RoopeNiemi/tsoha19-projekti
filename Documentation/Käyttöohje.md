# Käyttöohje

Ohjelman aiheena on keskustelufoorumi. Ei-kirjautunut käyttäjä voi selailla ja etsiä keskusteluja, ja näyttää yksittäisiä keskusteluja. 
Sivulle mentäessä käyttäjä uudelleenohjataan keskustelujen listaus -sivulle. Yksittäiseen keskusteluun pääsee klikkaamalla hiirellä keskustelun
otsikkoa. Keskusteluja pystyy etsimään listauksen yläpuolella olevan hakutoiminnon avulla. Haku tapahtuu keskusteluun liittyvän tagin tai keskustelun otsikon perusteella. Tulokset listataan eri otsikoiden alle, tagin mukaan ja otsikon mukaan. Tageja ei näy listauksessa mutta ne näkyvät kun avaa yksittäisen keskustelun. 


Uuden käyttäjän voi rekisteröidä oikeasta yläkulmasta Register nappia painamalla. Käyttäjänimen tulee olla vähintään 6 merkkiä pitkä ja salasanan
vähintään 8 merkkiä pitkä. Lisäksi käyttäjänimen tulee olla uniikki. Rekisteröinnin jälkeen käyttäjä siirretään sisäänkirjautumissivulle. Sisäänkirjautumissivulle
pääsee myös Register napin vierestä Login napista. 

Kirjautuneena käyttäjänä pystyy kaiken edellisen lisäksi luomaan uusia keskusteluja (create post nappula keskustelujen listauksen yläpuolella), ja kommentoimaan jo olemassaolevia keskusteluja
(yksittäisen keskustelun alla kommentointilomake). Käyttäjä pystyy poistamaan omia viestejä ja keskusteluja painamalla delete-nappia keskustelun tai viestin vieressä.
Omia viestejä pystyy myös muokkaamaan painamalla edit nappia, joka on delete-napin yläpuolella. Käyttäjä pystyy myös katsomaan omaa profiiliaan (My profile nappi Discussions napin vieressä yläpalkissa). 
Omalla profiilisivulla näkyy oma käyttäjänimi, käyttäjän luomispäivä, ja käyttäjän yhteensä kirjoittamat viestit. Tällä sivulla pystyy myös  poistamaan oman käyttäjän
(delete account profiilin alapuolella). Käyttäjän poistaminen vaatii käyttäjää antamaan salasana. Profiilisivulta pääsee myös vaihtamaan salasanansa (Change password -nappi profiilin
alapuolella). Salasanan vaihtoon vaaditaan vanha salasana ja uuden salasanan pitää olla vähintään 8 merkkiä pitkä, ja se pitää toistaa onnistuneesti jotta salasanan vaihto onnistuu.
Käyttäjä pystyy uloskirjautumaan painamalla Logout nappia yläpalkin oikeassa reunassa.

Admin käyttäjänä pystyy kaiken edellisen lisäksi myös poistamaan minkä tahansa keskustelun, viestin tai jopa käyttäjän. Keskustelujen ja viestien vierellä delete nappia painamalla 
voi poistaa keskustelun tai viestin. Vasemmalla ylhäällä List users -nappia painammalla pääsee käyttäjien listaukseen. Käyttäjän nimeä painamalla pääsee katsomaan käyttäjän tietoja.
Käyttäjien listauksessa käyttäjän oikealta puolelta delete nappia painamalla admin käyttäjä voi poistaa minkä tahansa käyttäjän. Uudet käyttäjät saavat automaattisesti roolin
user. Jos ohjelmaa käyttää lokaalisti, voi admin käyttäjän tehdä luomalla uuden käyttäjän, ja muuttamalla tietokannassa luodun käyttäjän rooliksi 'admin'. 
Komento on jokseenkin seuraavanlainen: "Update Account SET role='admin' WHERE username='luodun käyttäjän nimi'; ".

