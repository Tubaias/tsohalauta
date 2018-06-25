# User storyt

Tärkeimmät user storyt eli käyttäjätarinat ja niihin liittyvät SQL-kyselyt.

## Peruskäyttäjä
Käyttäjänä voin...
- luoda uuden langan, jolla on otsikko ja jonkinlainen aloitusviesti.

```SQL
INSERT INTO thread (date_created, date_modified, name, title, text, activity, board_id, moderator_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)
```

- selata laudalla olevia lankoja otsikon ja aktiivisuuden perusteella.

```SQL
SELECT thread.id, thread.date_created, thread.date_modified, thread.name, thread.title, 
thread.text, thread.activity, thread.board_id, thread.moderator_id 
FROM thread 
WHERE thread.board_id = ? 
ORDER BY thread.activity DESC
```

- lukea langoissa olevia viestejä ja superviestejä.

```SQL
SELECT supermessage.id, supermessage.date_created, supermessage.date_modified, supermessage.name, 
supermessage.text, supermessage.moderator_id 
FROM supermessage, "threadsupermessage" 
WHERE ? = "threadsupermessage".thread_id AND supermessage.id = "threadsupermessage".supermessage_id
```

```SQL
SELECT message.id, message.date_created, message.date_modified, message.name, message.text, 
message.thread_id, message.moderator_id, message.reply_target_id
FROM message 
WHERE message.thread_id = ? ORDER BY message.id
```
- kirjoittaa lankoihin uusia viestejä

```SQL
INSERT INTO message (date_created, date_modified, name, text, thread_id, moderator_id, reply_target_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?)
```
- hakea lankoja hakutekstin perusteella ja tarkastella haun tuloksia.

```SQL
SELECT thread.id, thread.date_created, thread.date_modified, thread.name, thread.title, thread.text, 
thread.activity, thread.board_id, thread.moderator_id
FROM thread 
WHERE thread.title LIKE ?
```

```SQL
SELECT thread.id, thread.date_created, thread.date_modified, thread.name, thread.title, thread.text,
thread.activity, thread.board_id, thread.moderator_id
FROM thread 
WHERE thread.text LIKE ?
```

- hakea viestejä hakutekstin perusteella ja tarkastella haun tuloksia.

```SQL
SELECT message.id, message.date_created, message.date_modified, message.name, message.text,
message.thread_id, message.moderator_id, message.reply_target_id
FROM message 
WHERE message.text LIKE ?
```

- tarkastella aktiivisimpia foorumilla olevia lankoja.

```SQL
SELECT Thread.id, Thread.title, Thread.activity AS activity, COUNT(Message.id) AS messages 
FROM Thread
LEFT JOIN Message ON Message.thread_id = Thread.id
GROUP BY Thread.id
HAVING COUNT(Message.id) > 0
ORDER BY activity DESC, messages DESC
LIMIT 10
```

- tarkastella palstojen kokonaisaktiivisuutta.

```SQL
SELECT Board.id, Board.tag, SUM(Thread.activity) AS activity
FROM Board
LEFT JOIN Thread ON Thread.board_id = Board.id
GROUP BY Board.id
ORDER BY activity DESC
```

## Järjestelmänvalvoja
Järjestelmänvalvojana voin lisäksi...

- kirjautua järjestelmänvalvojatilille.

```SQL
SELECT moderator.id, moderator.date_created, moderator.date_modified, moderator.username,
moderator.password, moderator.actions_taken
FROM moderator 
WHERE moderator.username = ? 
AND moderator.password = ?
```

- kirjoittaa lankoihin järjestelmänvalvojatilin nimellä varustettuja viestejä.

```SQL
INSERT INTO message (date_created, date_modified, name, text, thread_id, moderator_id, reply_target_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?)
```

- kirjoittaa pastoille superviestejä, jotka näkyvät jokaisessa senhetkisessä langassa.

```SQL
INSERT INTO supermessage (date_created, date_modified, name, text, moderator_id) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```

```SQL
INSERT INTO "ThreadSuperMessage" (thread_id, supermessage_id) VALUES (?, ?)
```

- muokata tai poistaa viestejä.

```SQL
UPDATE message SET date_modified=CURRENT_TIMESTAMP, text=? WHERE message.id = ?
```

```SQL
DELETE FROM message WHERE message.id = ?
```

- muokata tai poistaa lankoja.

```SQL
UPDATE thread SET date_modified=CURRENT_TIMESTAMP, title=?, text=? WHERE thread.id = ?
```


```SQL
DELETE FROM thread WHERE thread.id = ?
```
