# Tsohalauta

Tietokantasovellusharjoitus-kurssia varten toteutettava harjoitustyö.  

[Sovellus Herokussa](https://tsohalankku.herokuapp.com/)  

[User storyt](https://github.com/Tubaias/tsohalauta/blob/master/documentation/userstories.md)  

[Tietokantakaaviohahmotelma](https://github.com/Tubaias/tsohalauta/blob/master/documentation/db_diagram.png)

## Kirjautuminen

Sovelluksessa on olemassa järjestelmänvalvojatunnukset "test" salasanalla "test" ja "hello" salasanalla "world". Uusia tunnuksia voi luoda kirjoittamalla haluamansa nimen ja salasanan, ja antamamalla authorization keyn "auth".  
**Huomioi kuitenkin, että salasanat eivät ole kryptattuja, joten älä käytä salasanaa jota käyttäisit jossain muualla.**

## Aihekuvaus

Harjoitustyö on yleistä lauta/chan-formaattia löysästi noudattava anonyymi keskustelufoorumi. Foorumilla on kolme vakinaista palstaa, joihin sivun käyttäjät voivat tehdä uusia lankoja, joihin taas voi kirjoittaa viestejä. 

Sivulla on kirjautumismahdollisuus, joka on tarkoitettu ainoastaan järjestelmänvalvojien käyttöön. Järjestelmänvalvojatilin kautta on mahdollista muokata tai poistaa viestejä ja lankoja, ja tarkastella tietoja muista järjestelmänvalvojatileistä. Peruskäyttäjät eivät kirjaudu sivulle millään tavalla ja viesteihin ei yleensä liity käyttäjänimeä tai muita tunnisteita, vaan ainoastaan viestin uniikki id-numero. Kuitenkin jos viesti luodaan järjestelmänvalvojakäyttäjälle kirjautuneena, viestiin tulee mukaan sen luoneen järjestelmänvalvojan käyttäjänimi. Viestissä voidaan 'vastata' toiseen viestiin viittaamalla sen id-numeroon. Järjestelmänvalvojat voivat myös luoda superviestejä, jotka ilmestyvät näkyviin jokaiseen luomishetkellä aktiiviseen lankaan.

Vain 20 lankaa per palsta säilytetään kerralla. Kun uusi lanka luodaan, palstan sillä hetkellä vähiten aktiivinen lanka poistetaan lopullisesti. Foorumilla on myös mahdollisuus tarkastella tilastoja, kuten (including but not limited to) olemassaolevien lankojen viestien määrää ja palstojen kokonaisviestimäärää. Lisäksi viestejä tai lankoja voi hakea foorumilta hakusanan perusteella.

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
