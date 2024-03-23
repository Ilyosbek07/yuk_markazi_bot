import json

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import bot, db, dp


@dp.message_handler(Command("fix_score"))
async def fix_score(message: types.Message):
    await message.answer("Fix Boshlandi!")
    fix_list = []
    f = open("users.json", "r")
    data = json.loads(f.read(), strict=False)
    user_score = 0
    user_username = "---"
    phone = "---"
    for user in data:
        if user["score"]:
            user_score = int(user["score"])
        if user["username"]:
            user_username = user["username"]
        if user["phone"]:
            phone = user["phone"]
        try:

            db_user = await db.get_user(telegram_id=int(user["tg_id"]))
            print("---")
            print(db_user[0][4])
            print(user_score)
            fix_user_score = user_score - int(db_user[0][4])
            print(fix_user_score)
            fix_list.append({"tg_id": user["tg_id"], "score": fix_user_score})

        except Exception as err:
            fix_list.append({"tg_id": user["tg_id"], "score": user_score, "full_name": "user", "phone": "---"})
            continue
    f.close()
    with open("fix_score.json", "w") as outfile:
        json.dump(fix_list, outfile)
    document = open("fix_score.json")
    await bot.send_document(message.from_user.id, document=document)


@dp.message_handler(Command("jsonFile"))
async def jsonnn(message: types.Message):
    await message.answer("Filega yozish Boshlandi!")
    user_list = []
    userss = await db.select_all_users()
    for user in userss:
        user_dict = {}
        user_dict["full_name"] = user[1]
        user_dict["username"] = user[2]
        user_dict["phone"] = user[3]
        user_dict["score"] = user[4]
        user_dict["tg_id"] = user[6]
        user_list.append(user_dict)
    with open("users.json", "w") as outfile:
        json.dump(user_list, outfile)
    document = open("users.json")
    await bot.send_document(message.from_user.id, document=document)


@dp.message_handler(Command("read_file"))
async def json_reader(message: types.Message):
    await message.answer("Boshlandi!!!!!")
    f = open("users.json", "r")
    data = json.loads(f.read(), strict=False)
    user_score = 0
    user_username = "---"
    phone = "---"
    oldd = "---"
    for user in data:
        if user["score"]:
            user_score = int(user["score"])
        if user["username"]:
            user_username = user["username"]
        if user["phone"]:
            phone = user["phone"]
        if user["oldd"]:
            oldd = user["oldd"]
        try:
            user = await db.add_json_file_user(
                telegram_id=user["tg_id"],
                username=user_username,
                full_name=user["full_name"],
                phone=phone,
                score=user_score,
                oldd=oldd,
            )
        except Exception as err:
            pass
    f.close()


@dp.message_handler(Command("read_fix_file"))
async def read_fix_file(message: types.Message):
    await message.answer("Boshlandi!!!!!")
    f = open("fix_score.json", "r")
    data = json.loads(f.read(), strict=False)
    for user in data:
        try:
            server_user = await db.get_user(telegram_id=user["tg_id"])
            fix_score = server_user[0][4] + user["score"]
            await db.update_user_score(
                score=fix_score,
                telegram_id=user["tg_id"],
            )
        except Exception as err:
            await db.fix_user(
                telegram_id=user["tg_id"], score=user["score"], username="---", phone="old", full_name="user"
            )
    await message.answer("tugadi")
    f.close()
