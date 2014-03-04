import db

conn = db.get_new_conn()
cur = conn.cursor()

print "Creating tables..."
cur.execute(" \
	DROP TABLE IF EXISTS games; \
	DROP TABLE IF EXISTS user_games; \
	CREATE TABLE games ( \
		game_id     varchar, \
		state       varchar, \
		PRIMARY KEY(game_id) \
		); \
	CREATE TABLE user_games ( \
		user_id     varchar, \
		game_id     varchar, \
		actor_nr    integer, \
		PRIMARY KEY(user_id, game_id) \
		); \
	")

conn.commit()
cur.close()
conn.close()

print "... done"