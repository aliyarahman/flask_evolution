from app import db, models

# Add two sample users
angie = models.User(1,"Angie", "Rollins", "arollins")
jason = models.User(2,"Jason", "Towns", "jtowns")
db.session.add(angie)
db.session.add(jason)
db.session.commit()


# Add two sample posts. We did a commit first, above, so that the user ids for the users would already be in the database, since one of the fields re$
angie_post = models.Post("Woke up on the freedom side", "What side are you on, my people?", 1)
jason_post = models.Post("CSTEM for all", "Educational equity around CSTEM is a significant factor impacting the demographic makeup of today's tech labor force")
db.session.add(angie_post)
db.session.add(jason_post)
db.session.commit()

