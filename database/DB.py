import aiosqlite

dbname = "sharkGarant.db"


async def add_user_id(user_id):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute("INSERT INTO `user` (`user_id`) VALUES (?)", (user_id,))
        return await connection.commit()


async def add_user_idDeal(user_id):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute("INSERT INTO `deal` (`user_id`) VALUES (?)", (user_id,))
        return await connection.commit()


async def update_userName(user_id, name):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `name`=? WHERE `user_id`=?", (name, user_id))
        return await connection.commit()


async def selectName(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `name` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def select_user_id(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `user_id` FROM `user` WHERE `user_id`=?", (user_id,))
        return await cursor.fetchone()


async def select_user_idDeal(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `user_id` FROM `deal` WHERE `user_id`=?", (user_id,))
        return await cursor.fetchone()


async def selectAllUser():
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute(f"SELECT `user_id` FROM `user`")
        result = await cursor.fetchall()
        return [row[0] for row in result]


async def selectTON(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `TON` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def selectUSDT(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `USDT` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def selectBUSD(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `BUSD` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def selectUSDC(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `USDC` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def selectSum(user_id, currency):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute(f"SELECT `{currency}` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def updateTON(user_id, crypto):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `TON`=? WHERE `user_id`=?", (crypto, user_id))
        return await connection.commit()


async def updateUSDT(user_id, crypto):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `USDT`=? WHERE `user_id`=?", (crypto, user_id))
        return await connection.commit()


async def updateBUSD(user_id, crypto):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `BUSD`=? WHERE `user_id`=?", (crypto, user_id))
        return await connection.commit()


async def updateUSDC(user_id, crypto):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `USDC`=? WHERE `user_id`=?", (crypto, user_id))
        return await connection.commit()


async def selectQuantitySell(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `quantitySell` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def selectQuantityBuy(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `quantityBuy` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def selectSellUSD(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `sellUSD` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def selectBuyUSD(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `buyUSD` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def updateCrypto(user_id, crypto):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `crypto`=? WHERE `user_id`=?", (crypto, user_id))
        return await connection.commit()


async def updateSumPaid(user_id, sum):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `sumPaid`=? WHERE `user_id`=?", (sum, user_id))
        return await connection.commit()


async def updateSumDeal(user_id, sum):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `deal` SET `sum`=? WHERE `user_id`=?", (sum, user_id))
        return await connection.commit()


async def updateInvoiceId(user_id, invoiceId):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `invoiceId`=? WHERE `user_id`=?", (invoiceId, user_id))
        return await connection.commit()


async def updateInvoiceUrl(user_id, invoiceUrl):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `invoiceUrl`=? WHERE `user_id`=?", (invoiceUrl, user_id))
        return await connection.commit()


async def selectCrypto(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `crypto` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def selectSumPaid(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `sumPaid` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def selectInvoiceId(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `invoiceId` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def selectInvoiceUrl(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `invoiceUrl` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def update_user_idDeal(user_id, user_idDeal):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `deal` SET `user_idDeal`=? WHERE `user_id`=?", (user_idDeal, user_id))
        return await connection.commit()


async def select_user_id_forDeal(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `user_idDeal` FROM `deal` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def update_currencyDeal(user_id, currency):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `deal` SET `currency`=? WHERE `user_id`=?", (currency, user_id))
        return await connection.commit()


async def select_sum_forDeal(user_id, currency):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute(f"SELECT `{currency}` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def select_currencyDeal(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `currency` FROM `deal` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def updateBalance(user_id, currency, sum):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `{currency}`=? WHERE `user_id`=?", (sum, user_id))
        return await connection.commit()


async def selectSumDeal(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `sum` FROM `deal` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def addDeal(deal_id):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute("INSERT INTO `allDeal` (`deal_id`) VALUES (?)", (deal_id,))
        return await connection.commit()


async def updateDeal(deal_id, user_id, user_idDeal, sum, currency):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(
            f"UPDATE `allDeal` SET `user_id`=?, `user_idDeal`=?, `sum`=?, `currency`=? WHERE `deal_id`=?",
            (user_id, user_idDeal, sum, currency, deal_id))
        return await connection.commit()


async def selectDealBuy(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `deal_id`, `user_idDeal`, `sum`, `currency` FROM `allDeal` WHERE `user_id`=?",
                             (user_id,))
        result = await cursor.fetchall()
        return [[row] for row in result]


async def selectDealSell(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `deal_id`, `user_id`, `sum`, `currency` FROM `allDeal` WHERE `user_idDeal`=?",
                             (user_id,))
        result = await cursor.fetchall()
        return [[row] for row in result]


async def updateNext(user_id, next):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `next`=? WHERE `user_id`=?", (next, user_id))
        return await connection.commit()


async def selectNext(user_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `next` FROM `user` WHERE `user_id`=?", (user_id,))
        result = await cursor.fetchone()
        return result[0]


async def selectFromAllDeal(deal_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `user_idDeal`, `sum`, `currency` FROM `allDeal` WHERE `deal_id`=?", (deal_id,))
        return await cursor.fetchall()


async def selectUserIdFromAllDeal(deal_id):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `user_id`, `sum`, `currency` FROM `allDeal` WHERE `deal_id`=?", (deal_id,))
        return await cursor.fetchall()


async def delateAllDeal(deal_id):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"DELETE FROM `allDeal` WHERE `deal_id` = {deal_id}")
        return await connection.commit()


async def updateQuantityBuy(user_id, quantity):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `quantityBuy`=? WHERE `user_id`=?", (quantity, user_id))
        return await connection.commit()


async def updateQuantitySell(user_id, quantity):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `quantitySell`=? WHERE `user_id`=?", (quantity, user_id))
        return await connection.commit()


async def updateBuyUSD(user_id, sum):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `buyUsd`=? WHERE `user_id`=?", (sum, user_id))
        return await connection.commit()


async def updateSellUSD(user_id, sum):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `user` SET `sellUsd`=? WHERE `user_id`=?", (sum, user_id))
        return await connection.commit()


async def selectAllUserFrom(table):
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute(f"SELECT `user_id` FROM `{table}`")
        result = await cursor.fetchall()
        return [row[0] for row in result]


async def addAdmin(user_id):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute("INSERT INTO `admin` (`user_id`) VALUES (?)", (user_id,))
        return await connection.commit()


async def delateAdmin(user_id):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"DELETE FROM `admin` WHERE `user_id` = {user_id}")
        return await connection.commit()


async def updateUserQuantity(quantity):
    async with aiosqlite.connect(dbname) as connection:
        await connection.execute(f"UPDATE `userQuantity` SET `quantity`=? WHERE `key`=?", (quantity, 1))
        return await connection.commit()


async def selectUserQuantity():
    async with aiosqlite.connect(dbname) as connection:
        cursor = await connection.cursor()
        await cursor.execute("SELECT `quantity` FROM `userQuantity` WHERE `key`=?", (1,))
        result = await cursor.fetchone()
        return result[0]
