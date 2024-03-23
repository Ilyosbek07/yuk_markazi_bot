from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER, password=config.DB_PASS, host=config.DB_HOST, database=config.DB_NAME
        )

    async def execute(
            self, command, *args, fetch: bool = False, fetchval: bool = False, fetchrow: bool = False,
            execute: bool = False
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        phone varchar(55),
        score INT DEFAULT 0,
        oldd varchar(3),
        telegram_id BIGINT NOT NULL UNIQUE,
        user_args varchar(55)
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_admins(self):
        sql = """
        CREATE TABLE IF NOT EXISTS admins (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_tests(self):
        sql = """
        CREATE TABLE IF NOT EXISTS tests (
        id SERIAL PRIMARY KEY,
        question varchar(255),
        answer_1 varchar(33),
        answer_2 varchar(33),
        answer_3 varchar(33),
        answer_4 varchar(33),
        day varchar(33)
        );
        """
        await self.execute(sql, execute=True)

    async def create_table_chanel(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Channel (
        id SERIAL PRIMARY KEY,
        chanelll VARCHAR(301) NOT NULL,
        url varchar(301) NOT NULL,
        channel_name TEXT NULL
                );
        """
        await self.execute(sql, execute=True)

    async def create_table_add_list_chanel(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Add_List_Channel (
        id SERIAL PRIMARY KEY,
        url varchar(301) NOT NULL
                        );
        """
        await self.execute(sql, execute=True)

    async def create_table_add_list(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Add_List (
        id SERIAL PRIMARY KEY,
        url varchar(301) NOT NULL,
        button_name varchar(301) NOT NULL
                        );
        """
        await self.execute(sql, execute=True)

    async def create_table_request_join_chanel(self):
        sql = """
        CREATE TABLE IF NOT EXISTS request_join_chanel (
        id SERIAL PRIMARY KEY,
        channel_id VARCHAR(301) NOT NULL,
        url varchar(301) NOT NULL,
        channel_name TEXT NULL
                );
        """
        await self.execute(sql, execute=True)

    async def create_table_requested_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS requested_users (
        id SERIAL PRIMARY KEY,
        url_1 varchar(11),
        url_2 varchar(11),
        url_3 varchar(11),
        url_4 varchar(11),
        url_5 varchar(11),
        url_6 varchar(11),
        url_7 varchar(11),
        url_8 varchar(11),
        url_9 varchar(11),
        telegram_id BIGINT NOT NULL UNIQUE
                );
        """
        await self.execute(sql, execute=True)

    async def create_table_chanel_element(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Elementt (
        id SERIAL PRIMARY KEY,
        photo TEXT NULL,
        gifts TEXT NULL,
        game_text TEXT NULL,
        shartlar TEXT NULL,
        limit_score INT DEFAULT 1,
        winners INT DEFAULT 20,
        group_id TEXT NULL
                );
        """
        await self.execute(sql, execute=True)

    async def create_orders(self):
        sql = """
        CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        status VARCHAR(255),
        from_region VARCHAR(255),
        from_district VARCHAR(255),
        to_region VARCHAR(255),
        to_district VARCHAR(255),
        district VARCHAR(255),
        description TEXT NULL,
        curyer_id BIGINT,
        customer_id BIGINT
                );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)])
        return sql, tuple(parameters.values())

    async def testtt(self, url):
        sql = "INSERT INTO testtttttttt (url) VALUES($1) returning *"
        return await self.execute(sql, url, fetchrow=True)

    async def sel(self):
        sql = "SELECT * FROM testtttttttt"
        return await self.execute(sql, fetchrow=True)

    async def add_order(self, from_region, from_district, to_region, to_district,status, customer_id, description):
        sql = "INSERT INTO orders (from_region, from_district, to_region, to_district,status, customer_id, description) VALUES($1, $2, $3, $4, $5, $6, $7) returning *"
        return await self.execute(sql, from_region, from_district, to_region, to_district,status, customer_id, description,
                                  fetchrow=True)

    async def add_user(self, full_name, telegram_id, username, phone, oldd, user_args):
        sql = "INSERT INTO users (full_name, telegram_id, username, phone, oldd, user_args) VALUES($1, $2, $3, $4, $5, $6) returning *"
        return await self.execute(sql, full_name, telegram_id, username, phone, oldd, user_args, fetchrow=True)

    async def fix_user(self, full_name, telegram_id, username, phone, score):
        sql = "INSERT INTO users (full_name, telegram_id, username, phone,score) VALUES($1, $2, $3, $4,$5) returning *"
        return await self.execute(sql, full_name, telegram_id, username, phone, score, fetchrow=True)

    async def add_userrr(self, full_name, telegram_id, username, phone, score):
        sql = (
            "INSERT INTO users (full_name, telegram_id, username, phone, score) VALUES($1, $2, $3, $4, $5) returning *"
        )
        return await self.execute(sql, full_name, telegram_id, username, phone, score, fetchrow=True)

    async def add_userr(self, full_name, telegram_id, username, score):
        sql = "INSERT INTO users (full_name, telegram_id, username, score) VALUES($1, $2, $3,$4) returning *"
        return await self.execute(sql, full_name, telegram_id, username, score, fetchrow=True)

    async def add_json_file_user(self, full_name, username, phone, telegram_id, score, oldd):
        sql = "INSERT INTO users (full_name, username, phone, telegram_id, score,oldd) VALUES($1, $2, $3,$4,$5,$6) returning *"
        return await self.execute(sql, full_name, username, phone, telegram_id, score, oldd, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def select_top_users(self, lim_win):
        sql = f"SELECT * FROM Users WHERE score IS NOT NULL ORDER BY score DESC LIMIT {lim_win}"
        return await self.execute(sql, fetch=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_score(self, score, telegram_id):
        sql = "UPDATE Users SET score=$1 WHERE telegram_id=$2"
        return await self.execute(sql, score, telegram_id, execute=True)

    async def update_user_oldd(self, oldd, telegram_id):
        sql = "UPDATE Users SET oldd=$1 WHERE telegram_id=$2"
        return await self.execute(sql, oldd, telegram_id, execute=True)

    async def update_user_args(self, user_args, telegram_id):
        sql = "UPDATE Users SET user_args=$1 WHERE telegram_id=$2"
        return await self.execute(sql, user_args, telegram_id, execute=True)

    async def update_all_users_args(self, args):
        sql = "UPDATE Users SET user_args=$1"
        return await self.execute(sql, args, execute=True)

    async def update_user_args_oldd(self, oldd, user_args, phone, telegram_id):
        sql = "UPDATE Users SET oldd=$1, user_args=$2, phone=$3 WHERE telegram_id=$4"
        return await self.execute(sql, oldd, user_args, phone, telegram_id, execute=True)

    async def update_user_phone(self, phone, score, telegram_id):
        sql = "UPDATE Users SET phone=$1, score=$2 WHERE telegram_id=$3"
        return await self.execute(sql, phone, score, telegram_id, execute=True)

    # async def update_user_score(self, score, telegram_id):
    #     sql = "UPDATE Users SET score=$1 WHERE telegram_id=$2"
    #     return await self.execute(sql, score, telegram_id, execute=True)

    async def update_users_all_score(self):
        sql = "UPDATE Users SET score=0"
        return await self.execute(sql, execute=True)

    async def delete_users(self, telegram_id):
        sql = "DELETE FROM Users WHERE telegram_id=$1"
        await self.execute(sql, telegram_id, execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

    async def drop_orders(self):
        await self.execute("DROP TABLE orders", execute=True)

    async def select_chanel(self):
        sql = "SELECT * FROM Channel"
        return await self.execute(sql, fetch=True)

    async def select_add_list_channels(self):
        sql = "SELECT * FROM Add_List_Channel"
        return await self.execute(sql, fetch=True)

    async def select_add_list(self):
        sql = "SELECT * FROM Add_List"
        return await self.execute(sql, fetch=True)

    async def select_chanel_add_list(self):
        sql = "SELECT * FROM Add_List_Channel"
        return await self.execute(sql, fetch=True)

    async def select_add_list(self):
        sql = "SELECT * FROM Add_List"
        return await self.execute(sql, fetch=True)

    async def add_chanell(self, chanelll, url, channel_name):
        sql = "INSERT INTO Channel (chanelll, url,channel_name) VALUES($1, $2,$3) returning *"
        return await self.execute(sql, chanelll, url, channel_name, fetchrow=True)

    async def add_channel_for_add_list(self, url):
        sql = "INSERT INTO Add_List_Channel (url) VALUES($1) returning *"
        return await self.execute(sql, url, fetchrow=True)

    async def add_add_list(self, url, button_name):
        sql = "INSERT INTO Add_List (url, button_name) VALUES($1,$2) returning *"
        return await self.execute(sql, url, button_name, fetchrow=True)

    async def get_chanel(self, channel):
        sql = f"SELECT * FROM Channel WHERE chanelll=$1"
        return await self.execute(sql, channel, fetch=True)

    async def get_add_list_chanel(self, url):
        sql = f"SELECT * FROM Add_List_Channel WHERE url=$1"
        return await self.execute(sql, url, fetch=True)

    async def get_add_list(self, url):
        sql = f"SELECT * FROM Add_List WHERE url=$1"
        return await self.execute(sql, url, fetch=True)

    async def drop_Chanel(self):
        await self.execute("DROP TABLE Channel", execute=True)

    async def delete_channel(self, chanel):
        sql = "DELETE FROM Channel WHERE chanelll=$1"
        await self.execute(sql, chanel, execute=True)

    async def delete_add_list_channel(self, url):
        sql = "DELETE FROM Add_List_Channel WHERE url=$1"
        await self.execute(sql, url, execute=True)

    async def delete_add_list(self, url):
        sql = "DELETE FROM Add_List WHERE url=$1"
        await self.execute(sql, url, execute=True)

    async def add_photo(self, photo):
        sql = "INSERT INTO Elementt (photo) VALUES($1) returning *"
        return await self.execute(sql, photo, fetchrow=True)

    async def add_gift(self, gift):
        sql = "INSERT INTO Elementt (gifts) VALUES($1) returning *"
        return await self.execute(sql, gift, fetchrow=True)

    async def add_shartlar(self, shartlar):
        sql = "INSERT INTO Elementt (shartlar) VALUES($1) returning *"
        return await self.execute(sql, shartlar, fetchrow=True)

    async def add_group_id(self, group_id):
        sql = "INSERT INTO Elementt (group_id) VALUES($1) returning *"
        return await self.execute(sql, group_id, fetchrow=True)

    async def add_text(self, game_text):
        sql = "INSERT INTO Elementt (game_text) VALUES($1) returning *"
        return await self.execute(sql, game_text, fetchrow=True)

    async def update_photo(self, photo):
        sql = "UPDATE Elementt SET photo=$1 WHERE id=1"
        return await self.execute(sql, photo, execute=True)

    async def update_limit_score(self, limit_score):
        sql = "UPDATE Elementt SET limit_score=$1 WHERE id=1"
        return await self.execute(sql, limit_score, execute=True)

    async def winners(self, winners):
        sql = "UPDATE Elementt SET winners=$1 WHERE id=1"
        return await self.execute(sql, winners, execute=True)

    async def update_game_text(self, game_text):
        sql = "UPDATE Elementt SET game_text=$1 WHERE id=1"
        return await self.execute(sql, game_text, execute=True)

    async def update_gift(self, gift):
        sql = "UPDATE Elementt SET gifts=$1 WHERE id=1"
        return await self.execute(sql, gift, execute=True)

    async def update_shartlar(self, shartlar):
        sql = "UPDATE Elementt SET shartlar=$1 WHERE id=1"
        return await self.execute(sql, shartlar, execute=True)

    async def update_group_id(self, group_id):
        sql = "UPDATE Elementt SET group_id=$1 WHERE id=1"
        return await self.execute(sql, group_id, execute=True)
    async def confirm_order_status(self, id):
        sql = "UPDATE orders SET status='confirm' WHERE id=$1"
        return await self.execute(sql, id, execute=True)
    async def cancel_order_status(self, id):
        sql = "UPDATE orders SET status='cancel' WHERE id=$1"
        return await self.execute(sql, id, execute=True)

    async def get_elements(self):
        sql = f"SELECT * FROM Elementt WHERE id=1"
        return await self.execute(sql, fetch=True)

    async def drop_elements(self):
        await self.execute("DROP TABLE Elementt", execute=True)

    async def add_requested_users(self, telegram_id):
        sql = "INSERT INTO requested_users (telegram_id) VALUES($1) returning *"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def get_requested_users(self, telegram_id):
        sql = f"SELECT * FROM requested_users WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetch=True)

    async def update_url_1(self, url_1, telegram_id):
        sql = "UPDATE requested_users SET url_1=$1 WHERE telegram_id=$2"
        return await self.execute(sql, url_1, telegram_id, execute=True)

    async def update_url_2(self, url_2, telegram_id):
        sql = "UPDATE requested_users SET url_2=$1 WHERE telegram_id=$2"
        return await self.execute(sql, url_2, telegram_id, execute=True)

    async def update_url_3(self, url_3, telegram_id):
        sql = "UPDATE requested_users SET url_3=$1 WHERE telegram_id=$2"
        return await self.execute(sql, url_3, telegram_id, execute=True)

    async def update_url_4(self, url_4, telegram_id):
        sql = "UPDATE requested_users SET url_4=$1 WHERE telegram_id=$2"
        return await self.execute(sql, url_4, telegram_id, execute=True)

    async def update_url_5(self, url_5, telegram_id):
        sql = "UPDATE requested_users SET url_5=$1 WHERE telegram_id=$2"
        return await self.execute(sql, url_5, telegram_id, execute=True)

    async def update_url_6(self, url_6, telegram_id):
        sql = "UPDATE requested_users SET url_6=$1 WHERE telegram_id=$2"
        return await self.execute(sql, url_6, telegram_id, execute=True)

    async def update_url_7(self, url_7, telegram_id):
        sql = "UPDATE requested_users SET url_7=$1 WHERE telegram_id=$2"
        return await self.execute(sql, url_7, telegram_id, execute=True)

    async def update_url_8(self, url_8, telegram_id):
        sql = "UPDATE requested_users SET url_8=$1 WHERE telegram_id=$2"
        return await self.execute(sql, url_8, telegram_id, execute=True)

    async def update_url_9(self, url_9, telegram_id):
        sql = "UPDATE requested_users SET url_9=$1 WHERE telegram_id=$2"
        return await self.execute(sql, url_9, telegram_id, execute=True)

    async def drop_requested_users(self):
        await self.execute("DROP TABLE requested_users", execute=True)

    # Join Request Channel DB codes
    async def select_req_j_chanel(self):
        sql = "SELECT * FROM request_join_chanel"
        return await self.execute(sql, fetch=True)

    async def add_req_j_channel(self, channel_id, url, channel_name):
        sql = "INSERT INTO request_join_chanel (channel_id, url,channel_name) VALUES($1, $2,$3) returning *"
        return await self.execute(sql, channel_id, url, channel_name, fetchrow=True)

    async def get_req_j_chanel(self, channel_id):
        sql = f"SELECT * FROM request_join_chanel WHERE channel_id=$1"
        return await self.execute(sql, channel_id, fetch=True)

    async def drop_req_j_Chanel(self):
        await self.execute("DROP TABLE request_join_chanel", execute=True)

    async def delete_req_j_channel(self, channel_id):
        sql = "DELETE FROM request_join_chanel WHERE channel_id=$1"
        await self.execute(sql, channel_id, execute=True)

    async def add_test_question(self, question, answer_1, answer_2, answer_3, answer_4, day):
        sql = "INSERT INTO tests (question, answer_1, answer_2, answer_3, answer_4, day) VALUES($1,$2,$3,$4,$5,$6) returning *"
        return await self.execute(sql, question, answer_1, answer_2, answer_3, answer_4, day, fetchrow=True)

    async def get_tests(self):
        sql = f"SELECT * FROM tests"
        return await self.execute(sql, fetch=True)

    async def drop_test(self):
        await self.execute("DROP TABLE tests", execute=True)

    async def add_solved_date(self, solved_date, telegram_id):
        sql = "INSERT INTO is_solved (solved_date, telegram_id) VALUES($1,$2) returning *"
        return await self.execute(sql, solved_date, telegram_id, fetchrow=True)

    async def get_user_solve(self, solved_date, telegram_id):
        sql = f"SELECT * FROM is_solved WHERE solved_date=$1 AND telegram_id=$2"
        return await self.execute(sql, solved_date, telegram_id, fetch=True)

    async def drop_is_solved(self):
        await self.execute("DROP TABLE is_solved", execute=True)

    async def add_admin(self, telegram_id):
        sql = "INSERT INTO admins (telegram_id) VALUES($1) returning *"
        return await self.execute(sql, telegram_id, fetchrow=True)

    async def select_all_admins(self):
        sql = "SELECT * FROM admins"
        return await self.execute(sql, fetch=True)

    async def delete_admins(self, telegram_id):
        sql = "DELETE FROM admins WHERE telegram_id=$1"
        await self.execute(sql, telegram_id, execute=True)

    async def drop_admins(self):
        await self.execute("DROP TABLE admins", execute=True)

    async def get_user(self, telegram_id):
        sql = f"SELECT * FROM users WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetch=True)

    async def get_all_args_users(self, user_args):
        sql = f"SELECT * FROM users WHERE user_args=$1"
        return await self.execute(sql, user_args, fetch=True)
