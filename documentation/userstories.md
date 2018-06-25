# User storyt

## Peruskäyttäjä
Käyttäjänä voin...
- luoda uuden langan, jolla on otsikko ja jonkinlainen aloitusviesti.

´´´SQL
INSERT INTO thread (date_created, date_modified, name, title, text, activity, board_id, moderator_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)
´´´

- selata laudalla olevia lankoja otsikon perusteella.

´´´SQL
´´´

- lukea langoissa olevia viestejä

´´´SQL
´´´

- kirjoittaa lankoihin uusia viestejä

´´´SQL
INSERT INTO message (date_created, date_modified, name, text, thread_id, moderator_id, reply_target_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?)
´´´

- hakea lankoja tai viestejä hakutekstin perusteella ja tarkastella haun tuloksia.

´´´SQL
´´´

- tarkastella aktiivisimpia foorumilla olevia lankoja.

´´´SQL
´´´

- tarkastella palstojen kokonaisaktiivisuutta.

´´´SQL
´´´

## Järjestelmänvalvoja
Järjestelmänvalvojana voin lisäksi...
- kirjoittaa lankoihin järjestelmänvalvojatilin nimellä varustettuja viestejä.
- kirjoittaa pastoille superviestejä, jotka näkyvät jokaisessa senhetkisessä langassa.
- muokata tai poistaa viestejä.
- muokata tai poistaa lankoja.
