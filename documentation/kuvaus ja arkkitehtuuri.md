# Sovelluksen kuvaus ja -arkkitehtuuri

## Aihekuvaus

Harjoitustyö on yleistä lauta/chan-formaattia löysästi noudattava anonyymi keskustelufoorumi. Foorumilla on kolme vakinaista palstaa, joihin sivun käyttäjät voivat tehdä uusia lankoja, joihin taas voi kirjoittaa viestejä. 

Sivulla on kirjautumismahdollisuus, joka on tarkoitettu ainoastaan järjestelmänvalvojien käyttöön. Järjestelmänvalvojatilin kautta on mahdollista muokata tai poistaa viestejä ja lankoja, ja tarkastella tietoja muista järjestelmänvalvojatileistä. Peruskäyttäjät eivät kirjaudu sivulle millään tavalla ja viesteihin ei yleensä liity käyttäjänimeä tai muita tunnisteita, vaan ainoastaan viestin uniikki id-numero. Kuitenkin jos viesti luodaan järjestelmänvalvojakäyttäjälle kirjautuneena, viestiin tulee mukaan sen luoneen järjestelmänvalvojan käyttäjänimi. Viestissä voidaan 'vastata' toiseen viestiin viittaamalla sen id-numeroon. Järjestelmänvalvojat voivat myös luoda 'superviestejä', jotka tulevat näkyviin jokaiseen luomishetkellä aktiiviseen lankaan.

Vain 20 lankaa per palsta säilytetään kerralla. Kun uusi lanka luodaan, palstan sillä hetkellä vähiten aktiivinen lanka poistetaan lopullisesti. Jokaisessa langassa voi olla maksimissaan 100 viestiä, jonka jälkeen uusia viestejä ei voi luoda lankaan. Foorumilla on myös mahdollisuus tarkastella tilastoja, kuten olemassaolevien lankojen määrää ja aktiivisuutta ja palstojen kokonaisaktiivisuutta. Lisäksi viestejä tai lankoja voi hakea foorumilta hakusanan perusteella.

Peruskäyttäjän toimintoja:
- Langan luominen
- Viestin luominen
- Langan tai viestin hakeminen
- Tilastojen katselu

Järjestelmänvalvojan toimintoja:
- Järjestelmänvalvojatiliin kirjautuminen
- Järjestelmänvalvojan nimellä varustetun viestin tai superviestin luominen
- Langan muokkaus tai poistaminen
- Viestin muokkaus tai poistaminen

## Arkkitehtuuri

Sovellus käyttää tietojen tallentamiseen paikallisessa käytössä SQLite-tietokantaa ja Heroku-palvelimella PostgreSQL-tietokantaa.

### Tietokantakaavio

<img src="https://github.com/Tubaias/tsohalauta/blob/master/documentation/db_diagram.png" width="1280">

### Tietokannan normalisointi

Tietokantatauluja on yhteensä seitsemän kappaletta ja ne ovat kaikki vähintään toisessa normaalimuodossa.  

Taulu _moderator_ ei ole kolmannessa normaalimuodossa, koska sen sarake _username_ on uniikki jokaiselle moderaattorille, jolloin kaikki muut sarakkeet ovat sarakkeen _username_ kautta transitiivisesti riippuvaisia taulun pääavaimesta. Tämä on kuitenkin järkevä toteutus, koska sivulle ei haluta kahta käyttäjää, joilla on sama nimi.  

Myöskään taulut _thread_, _message_ tai _supermessage_ eivät ole kolmannessa normaalimuodossa, koska kaikissa niissä on viestin tai langan luoneen moderaattorin nimeen viittaava sarake _name_, joka on sarakkeen _moderator_id_ kautta transitiivisesti riippuvainen pääavaimesta. Moderaattorin nimi tallennetaan tauluissa, koska tämä vähentää html-sivuille annettavien parametrien määrää huomattavasti ja näin yksinkertaistaa ja nopeuttaa ohjelmakoodia.
