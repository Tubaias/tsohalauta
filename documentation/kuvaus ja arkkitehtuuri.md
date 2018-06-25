# Sovelluksen kuvaus ja -arkkitehtuuri

## Sovelluksen kuvaus

### Aihekuvaus

Harjoitustyö on yleistä lauta/chan-formaattia löysästi noudattava anonyymi keskustelufoorumi. Foorumilla on kolme vakinaista palstaa, joihin sivun käyttäjät voivat tehdä uusia lankoja, joihin taas voi kirjoittaa viestejä. 

Sivulla on kirjautumismahdollisuus, joka on tarkoitettu ainoastaan järjestelmänvalvojien käyttöön. Järjestelmänvalvojatilin kautta on mahdollista muokata tai poistaa viestejä ja lankoja, ja tarkastella tietoja muista järjestelmänvalvojatileistä. Peruskäyttäjät eivät kirjaudu sivulle millään tavalla ja viesteihin ei yleensä liity käyttäjänimeä tai muita tunnisteita, vaan ainoastaan viestin uniikki id-numero. Kuitenkin jos viesti luodaan järjestelmänvalvojakäyttäjälle kirjautuneena, viestiin tulee mukaan sen luoneen järjestelmänvalvojan käyttäjänimi. Viestissä voidaan 'vastata' toiseen viestiin viittaamalla sen id-numeroon. Järjestelmänvalvojat voivat myös luoda 'superviestejä', jotka tulevat näkyviin jokaiseen luomishetkellä aktiiviseen lankaan.

Vain 20 lankaa per palsta säilytetään kerralla. Kun uusi lanka luodaan, palstan sillä hetkellä vähiten aktiivinen lanka poistetaan lopullisesti. Jokaisessa langassa voi olla maksimissaan 100 viestiä, jonka jälkeen uusia viestejä ei voi luoda lankaan. Koska viestejä voi olla langassa maksimissaan vain sata ja viestit eivät voi olla kovin pitkiä, lankojen sivutus ei ole tarpeellista.  

Foorumilla on myös mahdollisuus tarkastella tilastoja, kuten olemassaolevien lankojen määrää ja aktiivisuutta ja palstojen kokonaisaktiivisuutta. Lisäksi viestejä tai lankoja voi hakea foorumilta hakusanan perusteella.

### Rajoitteet ja puuttuvat ominaisuudet

Sovelluksen toiminnallisuus on suurimmaksi osin toivotun mukaista, mutta pieniä rajoitteita esiintyy. Esimerkiksi langan aloitusviestiin tai superviesteihin ei voi vastata toisella viestillä ja uusia palstoja tai autorisointiavaimia ei voi luoda sovelluksen sisällä. Tätä varten olisi kenties kannattanut lisätä korkeamman tason hallinnointikäyttäjä, joka pystyisi poistamaan moderaattorikäyttäjiä ja hallinnoimaan muita tietokannan ominaisuuksia.

Sovelluksella oli myös paljon suunniteltuja ominaisuuksia, joiden lisäämiseen ei ollut aikaa. Tällaisia puuttuvia ominaisuuksia ovat esimerkiksi kuvien lisääminen viesteihin, moneen viestiin vastaaminen yhdellä viestillä ja viestin vastauksien näyttäminen viestin kohdalla.

## Arkkitehtuuri

Sovellus käyttää tietojen tallentamiseen paikallisessa käytössä SQLite-tietokantaa ja Heroku-palvelimella PostgreSQL-tietokantaa. Tietokantatauluja on yhteensä seitsemän kappaletta, joista yksi on liitostaulu. Tietokannan luontiin ja hallinnointiin käytetään SQLAlchemy-liitännäistä.

Tietokannan käytön luonteen takia sen tieto on jatkuvasti muuttuvaa. Tämän vuoksi tietokannassa ei käytetä mitään ylimääräisiä indeksejä.

### Tietokantakaavio

<img src="https://github.com/Tubaias/tsohalauta/blob/master/documentation/db_diagram.png" width="1280">

### Tietokannan normalisointi

Kaikki tietokannan taulut ovat vähintään toisessa normaalimuodossa ja taulut _authkey_, _board_ ja _threadsupermessage_ ovat kolmannessa normaalimuodossa.  

Taulu _moderator_ ei ole kolmannessa normaalimuodossa, koska sen sarake _username_ on uniikki jokaiselle moderaattorille, jolloin kaikki muut sarakkeet ovat sarakkeen _username_ kautta transitiivisesti riippuvaisia taulun pääavaimesta. Tämä on kuitenkin järkevä toteutus, koska sivulle ei haluta kahta käyttäjää, joilla on sama nimi.  

Myöskään taulut _thread_, _message_ tai _supermessage_ eivät ole kolmannessa normaalimuodossa, koska kaikissa niissä on viestin tai langan luoneen moderaattorin nimeen viittaava sarake _name_, joka on sarakkeen _moderator_id_ kautta transitiivisesti riippuvainen pääavaimesta. Moderaattorin nimi tallennetaan tauluissa, koska tämä vähentää html-sivuille annettavien parametrien määrää huomattavasti ja näin yksinkertaistaa ja nopeuttaa ohjelmakoodia.

### SQL CREATE TABLE -lauseet

```SQL
CREATE TABLE message (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144), 
        text VARCHAR(500) NOT NULL, 
        thread_id INTEGER NOT NULL, 
        moderator_id INTEGER, 
        reply_target_id INTEGER, 
        PRIMARY KEY (id), 
        FOREIGN KEY(thread_id) REFERENCES thread (id), 
        FOREIGN KEY(moderator_id) REFERENCES moderator (id), 
        FOREIGN KEY(reply_target_id) REFERENCES message (id)
)
```

```SQL
CREATE TABLE thread (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144), 
        title VARCHAR(144), 
        text VARCHAR(1000) NOT NULL, 
        activity INTEGER, 
        board_id INTEGER NOT NULL, 
        moderator_id INTEGER, 
        PRIMARY KEY (id), 
        FOREIGN KEY(board_id) REFERENCES board (id), 
        FOREIGN KEY(moderator_id) REFERENCES moderator (id)
)
```

```SQL
CREATE TABLE "ThreadSuperMessage" (
        thread_id INTEGER, 
        supermessage_id INTEGER, 
        FOREIGN KEY(thread_id) REFERENCES thread (id) ON DELETE CASCADE, 
        FOREIGN KEY(supermessage_id) REFERENCES supermessage (id) ON DELETE CASCADE
)
```

```SQL
CREATE TABLE supermessage (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        text VARCHAR(250) NOT NULL, 
        moderator_id INTEGER, 
        PRIMARY KEY (id), 
        FOREIGN KEY(moderator_id) REFERENCES moderator (id)
)

```

```SQL
CREATE TABLE moderator (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        actions_taken INTEGER, 
        PRIMARY KEY (id)
)
```

```SQL
CREATE TABLE board (
        id INTEGER NOT NULL, 
        tag VARCHAR(3) NOT NULL, 
        PRIMARY KEY (id)
)
```

```SQL
CREATE TABLE authkey (
        id INTEGER NOT NULL, 
        keycode VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
)
```
