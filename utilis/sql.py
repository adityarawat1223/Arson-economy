from asyncpg import Pool


async def create_tables(pool: Pool):
    async with pool.acquire() as connection:
        # await connection.execute("DROP TABLE IF EXISTS users") # Uncomment this line if you have the database already created and have old data

        await connection.execute(
            """
            CREATE TABLE IF NOT EXISTS "item_info" (
            "item_id"    INTEGER NOT NULL PRIMARY KEY UNIQUE,
            "item_name"    TEXT,
            "item_description"    TEXT
                
            );
            CREATE TABLE IF NOT EXISTS "user_info" (
            "user_id"	INTEGER NOT NULL UNIQUE,
            "name"	TEXT,
            "money"	INTEGER DEFAULT 0 CHECK(money>=0),
            PRIMARY KEY("user_id")
            );

            CREATE TABLE IF NOT EXISTS "user_inventory" (
            "user_id"    INTEGER NOT NULL,
            "item_id"    INTEGER NOT NULL,
            "count"    INTEGER NOT NULL DEFAULT 0 CHECK(count>=0),
            FOREIGN KEY("item_id") REFERENCES "item_info"("item_id") ON DELETE CASCADE,
            FOREIGN KEY("user_id") REFERENCES "user_info"("user_id") ON DELETE CASCADE
            );
        """
        )

async def add(self,amount,id):
        user = await self.bot.db.fetchval("SELECT money FROM user_info WHERE user_id = $1",id)
        await self.bot.db.execute("UPDATE user_info SET money = $1 WHERE user_id = $2",user+amount,id)

async def get(self,id):
        user = await self.bot.db.fetchval("SELECT money FROM user_info WHERE user_id = $1" ,id)
        return user


async def invent(self,id):
    inventory = await self.bot.db.fetchval("SELECT inv FROM users WHERE id = $1",id)
    return inventory