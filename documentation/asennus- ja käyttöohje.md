# Asennus- ja käyttöohje

## Sovelluksen asentaminen lokaaliin käyttöön

Ajaaksesi sovelluksen lokaalisti tarvitset tuoreen Python 3 -version, jonka voi ladata [täältä](https://www.python.org/downloads/).
Tulet myös tarvitsemaan jonkun tavan suorittaa Bash-komentoja, 
ja [SQLiten](https://www.sqlite.org/download.html), jotta voit lisätä tietokantaan alustavat tiedot.

Aloita [kloonaamalla](https://help.github.com/articles/cloning-a-repository/) tai lataamalla sovellus koneellesi ja tämän jälkeen
aja sovelluksen hakemistossa komento:

```
python3 -m venv venv
```
Tämä luo sovelluksen hakemistoon Python-virtuaaliympäristön, joka täytyy riippuvuuksia asentaessa ja sovellusta ajaessa ottaa
käyttöön komennolla:

```
source venv/bin/activate
```
Suorita edellämainittu komento ja sen jälkeen asenna sovelluksen riippuvuudet komennolla:

```
pip install -r requirements.txt
```
Sovelluksen voi nyt ajaa komennolla:

```
python run.py
```
Kun sovellus on käynnissä, sitä voi käyttää missä tahansa selaimessa kirjoittamalla osoitekenttään _localhost:5000_ .

---

Sovellus luo ensimmäisellä käynnistyskerralla uuden tietokannan, johon pitää SQLiten avulla lisätä hieman lähtötietoja. 
Tämä tehdään suorittamalla _application_ -kansiossa komento:

```
sqlite3 database.db
```
Komento avaa tietokannan käsittelyyn, jonka jälkeen voidaan lisätä esimerkiksi yksi palsta nimellä _a_ ja 
yksi authorisaatioavain _auth_ komennoilla:

```
INSERT INTO thread (tag) VALUES ('a');
```

```
INSERT INTO authkey (keycode) VALUES ('auth');
```
Sovellus on nyt täysin valmis käytettäväksi.

## Peruskäyttäjätoimintojen käyttöohje

### Navigointipalkki

Jokaisessa sovelluksen näkymässä on ylälaidassa navigointipalkki, jonka avulla sovelluksen eri näkymiin pääsee nopeasti.
Etusivulle voi palata painamalla navigointipalkin tekstiä _TsohaLankku_ ja sivuun liittyviä statistiikkoja pääsee katselemaan 
painamalla tekstiä _View statistics_.  

Viestejä tai lankoja voi hakea hakusanan perusteella kirjoittamalla hakutekstin
navigointipalkissa olevaan laatikkoon, rajaamalla haun kohteen valitsimesta ja painamalla nappia _Search_.  

Lisäksi navigointipalkissa on linkit järjestelmänvalvojakäyttäjälle kirjautumiseen ja uuden tällaisen käyttäjän luomiseen.  

### Lankojen tarkastelu ja luominen

Sovelluksen etusivulla on listaus olemassaolevista palstoista, joiden nimeä painamalla voi siirtyä tarkastelemaan pastalla
olemassaolevia lankoja. Langat on järjestetty niiden nykyisen aktiivisuuden mukaan, joten ensimmäisenä näytettävät langat ovat
sillä hetkellä aktiivisimmat.  

Uuden langan voi luoda painamalla nappia _Create a new thread_, joka avaa langan luontiin käytettävän lomakkeen, johon sitten kirjoitetaan langan haluttu otsikko ja aloitusteksti langalle ja painetaan _Create thread_. Uusi lanka on nyt tarkasteltavissa valitulla palstalla.  

Vain 20 lankaa per palsta säilytetään kerralla, joten rajan ylittyessä sillä hetkellä vähiten aktiivinen lanka poistetaan lopullisesti.

### Viestien tarkastelu ja luominen

Lankoja tarkastellessa voi painaa langan kohdalla olevaa nappia _> to thread_, joka näyttää langan ja kaikki siinä olevat viestit.  

Suoraan langan aloitustekstin alla näytetään ensin vihreällä taustalla merkityt 'superviestit', jotka ovat järjestelmänvalvojan luomia ja näkyvät useassa langassa kerralla.  

Normaaleilla viestillä on sininen tausta, ja ne voivat vastata toisiin viesteihin, jolloin viestin tekstin yläpuolella on linkki toiseen viestiin tekstillä _>>[viestin id]_. Tätä linkkiä painamalla ikkuna kohdistuu viestiin, johon vastattiin ja viestin tausta värjääntyy punaiseksi. Lisäksi jokaisen viestin vasemmassa yläkulmassa on nappi _info_, jota painamalla voi siirtyä tarkastelemaan viestin tietoja yksityiskohtaisesti.  

Uuden viestin voi luoda kirjoittamalla haluamansa tekstin sivun ylälaidassa (mutta navigointipalkin alla) olevaan tekstilaatikkoon ja painamalla _Post message_. Toiseen viestiin voi vastata painamalla sen oikeassa ylälaidassa olevaa tekstiä _No. [viestin id]_, kirjoittamalla sen jälkeen haluamansa tekstin ja painamalla _Post message_.
