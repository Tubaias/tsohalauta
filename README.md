# Tsohalauta

Tietokantasovellusharjoitus-kurssia varten toteutettava harjoitustyö.  

[Sovellus Herokussa](https://tsohalankku.herokuapp.com/)  

[User storyt](https://github.com/Tubaias/tsohalauta/blob/master/documentation/userstories.md)  

[Tietokantakaaviohahmotelma](https://github.com/Tubaias/tsohalauta/blob/master/documentation/db_diagram.png)

## Kirjautuminen

Sovelluksessa on tällä hetkellä olemassa järjestelmänvalvojatunnukset "test" salasanalla "test" ja "hello" salasanalla "world". Uusia tunnuksia voi luoda kirjoittamalla haluamansa nimen ja salasanan, ja antamamalla authorization keyn, joka on tällä hetkellä "auth".  
**Huomioi kuitenkin, että salasanat eivät ole tällä hetkellä kryptattuja, joten älä käytä salasanaa jota käyttäisit jossain muualla.**

## Aihekuvaus

Harjoitustyö on yleistä lauta/chan-formaattia löysästi noudattava anonyymi keskustelufoorumi. Foorumilla on muutama vakinainen palsta, joihin sivun käyttäjät voivat tehdä uusia lankoja, joihin taas voi kirjoittaa viestejä. 

Sivulla on kirjautumismahdollisuus, joka on tarkoitettu ainoastaan järjestelmänvalvojien käyttöön. Järjestelmänvalvojatilin kautta on mahdollista muokata tai poistaa viestejä ja lankoja, ja tarkastella tietoja muista järjestelmänvalvojatileistä. Peruskäyttäjät eivät kirjaudu sivulle millään tavalla ja viesteihin ei yleensä liity käyttäjänimeä tai muita tunnisteita, vaan ainoastaan viestin uniikki id-numero. Kuitenkin jos viesti luodaan järjestelmänvalvojakäyttäjälle kirjautuneena, viestiin tulee mukaan sen luoneen järjestelmänvalvojan käyttäjänimi. Viestissä voidaan 'vastata' yhteen tai useampaan toiseen viestiin viittaamalla niiden id-numeroihin. Järjestelmänvalvojat voivat myös luoda 'superviestejä', jotka ilmestyvät näkyviin jokaiseen luomishetkellä aktiiviseen lankaan.

Vain tietty ennalta määritetty määrä lankoja säilytetään kerralla. Kun uusi lanka luodaan, sillä hetkellä vähiten aktiivinen lanka poistetaan lopullisesti. Foorumilla on myös mahdollisuus tarkastella tilastoja, kuten olemassaolevien lankojen viestien määrää ja palstojen kokonaisviestimäärää. Lisäksi viestejä tai lankoja voi hakea foorumilta hakusanan perusteella.

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
