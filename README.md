# Tsohalauta

Tietokantasovellusharjoitus-kurssia varten toteutettava harjoitustyö.  

https://tsohalankku.herokuapp.com/

## Aihekuvaus

Harjoitustyö on yleistä lauta/chan-formaattia löysästi noudattava anonyymi keskustelufoorumi. Foorumilla on muutama vakinainen palsta, joihin sivun käyttäjät voivat tehdä uusia lankoja, joihin taas voi kirjoittaa viestejä. 

Peruskäyttäjät eivät kirjaudu sivulle millään tavalla ja viesteihin ei liity käyttäjänimeä tai muita tunnisteita, vaan ainoastaan viestin uniikki id-numero. Viestissä voidaan 'vastata' yhteen tai useampaan toiseen viestiin viittaamalla niiden id-numeroihin. Sivulla on kuitenkin kirjautumismahdollisuus, joka on tarkoitettu ainoastaan järjestelmänvalvojien käyttöön. Järjestelmänvalvojatilin kautta on mahdollista muokata tai poistaa viestejä ja lankoja, ja estää lankojen tai viestien luominen tietystä IP-osoitteesta.

Vain tietty ennalta määritetty määrä lankoja säilytetään kerralla. Kun uusi lanka luodaan, sillä hetkellä vähiten aktiivinen lanka poistetaan lopullisesti. Foorumilla on myös mahdollisuus tarkastella tilastoja, kuten olemassaolevien lankojen viestien määrää ja palstojen kokonaisviestimäärää. Lisäksi viestejä tai lankoja voi hakea foorumilta hakusanan perusteella.

Peruskäyttäjän toimintoja:
- Langan luominen
- Viestin luominen
- Langan tai viestin hakeminen
- Tilastojen katselu

Järjestelmänvalvojan toimintoja:
- Järjestelmänvalvojatiliin kirjautuminen
- Langan muokkaus tai poistaminen
- Viestin muokkaus tai poistaminen
- Käyttöeston asettaminen IP-osoitteelle
