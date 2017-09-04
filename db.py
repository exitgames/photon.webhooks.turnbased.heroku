import os
import psycopg2
from urllib.parse import urlparse
from flask import _app_ctx_stack

from app import app

def get_app_conn():
	top = _app_ctx_stack.top
	if not hasattr(top, 'pg_conn'):
		top.pg_conn = get_new_conn()

	return top.pg_conn

def get_new_conn():
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	return psycopg2.connect(
		database=url.path[1:],
		user=url.username,
		password=url.password,
		host=url.hostname,
		port=url.port
		)

	
def set_game_state(game_id, state):
	app.logger.info("db: set_game_state(%s, %s)", game_id, state)
	conn = get_app_conn()
	cur = conn.cursor()
	cur.execute(" \
	UPDATE games SET state=%s WHERE game_id=%s; \
	INSERT INTO games (game_id, state) \
		SELECT %s, %s \
		WHERE NOT EXISTS (SELECT 1 FROM games WHERE game_id=%s); \
	   ", (state, game_id, game_id, state, game_id))
	conn.commit()
	return

def game_state_exists(game_id):
	app.logger.info("db: game_state_exists(%s)", game_id)
	conn = get_app_conn()
	cur = conn.cursor()
	cur.execute("SELECT 1 FROM games WHERE game_id=%s;", (game_id,))
	res = cur.fetchone() != None
	app.logger.info("db: game_state_exists = %s", res)
	return res

def get_game_state(game_id):
	app.logger.info("db: get_game_state(%s)", game_id)
	conn = get_app_conn()
	cur = conn.cursor()
	cur.execute("SELECT state FROM games WHERE game_id=%s;", (game_id,))
	res = cur.fetchone()
	state = None
	if res != None:
		state = res[0]
	app.logger.info("db: get_game_state = %s", state)
	return state

def delete_game_state(game_id):
	app.logger.info("db: delete_game_state(%s)", game_id)
	conn = get_app_conn()
	cur = conn.cursor()
	cur.execute("DELETE FROM games WHERE game_id=%s;", (game_id,))
	conn.commit()
	return

def set_user_game(user_id, game_id, actor_nr):
	app.logger.info("db: set_user_game(%s, %s, %d)", user_id, game_id, actor_nr)
	conn = get_app_conn()
	cur = conn.cursor()
	cur.execute(" \
	UPDATE user_games SET actor_nr=%s WHERE user_id=%s AND game_id=%s; \
	INSERT INTO user_games (user_id, game_id, actor_nr) \
		SELECT %s, %s, %s \
		WHERE NOT EXISTS (SELECT 1 FROM user_games WHERE user_id=%s AND game_id=%s); \
		", (actor_nr, user_id, game_id, user_id, game_id, actor_nr, user_id, game_id))
	conn.commit()
	return

	return

def get_user_game_list(user_id):
	app.logger.info("db: get_user_game_list(%s)", user_id)
	conn = get_app_conn()
	cur = conn.cursor()
	cur.execute("SELECT game_id, actor_nr FROM user_games WHERE user_id=%s;", (user_id,))
	res = cur.fetchall()
	app.logger.info("db: get_user_game_list = %s", res)
	return res

		
def delete_user_game(user_id, game_id):
	app.logger.info("db: delete_user_game(%s, %s)", user_id, game_id)
	conn = get_app_conn()
	cur = conn.cursor()
	cur.execute("DELETE FROM user_games WHERE game_id=%s;", (game_id,))
	conn.commit()
	return
	