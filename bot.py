from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN_BOT
from test import Test
import keyboard as kb

storage = MemoryStorage()
bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["test"], state=None)
async def enter_test(message: types.Message):
    await message.answer(
        "Вы начали тестирование.\n"
        "Вопрос №1. \n\n"
        "Есть ли место, где вы храните информацию для принятия решений?",
        reply_markup=kb.answer_kb)
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer1"] = answer

    await message.answer("Вопрос №2\n" "Все сотрудники могут её просмотреть?")
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer2"] = answer
    await message.answer("Вопрос №3\n"
                         "Используете ли Вы онлайн-хранилища данных")
    await Test.next()


@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer3"] = answer
    await message.answer(
        "Вопрос №4\n"
        "Используете ли Вы сайты/приложения для распределения задач?")
    await Test.next()


@dp.message_handler(state=Test.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer4"] = answer
    await message.answer(
        "Вопрос №5\n"
        "Храните ли Вы данные о результатов всех проектов за последние 3-2 года работы?"
    )
    await Test.next()


@dp.message_handler(state=Test.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer5"] = answer
    await message.answer(
        "Вопрос №6\n"
        "Есть ли у вашей организации зафиксированное и записанное видение миссии организации?"
    )
    await Test.next()


@dp.message_handler(state=Test.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer6"] = answer
    await message.answer("Вопрос №7\n"
                         "Рисует ли он картину вашего идеального мира?")
    await Test.next()


@dp.message_handler(state=Test.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer7"] = answer
    await message.answer("Вопрос №8\n"
                         "Описание миссии короткое и его легко понять?")
    await Test.next()


@dp.message_handler(state=Test.Q8)
async def answer_q8(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer8"] = answer
    await message.answer("Вопрос №9\n" "Описание реалистично и достижимо?")
    await Test.next()


@dp.message_handler(state=Test.Q9)
async def answer_q9(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer9"] = answer
    await message.answer(
        "Вопрос №10\n"
        "Все проекты организации соответствуют заявленной миссии?")
    await Test.next()


@dp.message_handler(state=Test.Q10)
async def answer_q10(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer10"] = answer
    await message.answer(
        "Вопрос №11\n"
        "Вы собираете первичную статистику в рамках реализации проектов и программ (посещения, обращения, др)?"
    )
    await Test.next()


@dp.message_handler(state=Test.Q11)
async def answer_q11(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer11"] = answer
    await message.answer(
        "Вопрос №12\n"
        "Вы отслеживаете путь благополучателей и изменения, которые происходят в их жизни благодаря Вашей организации?"
    )
    await Test.next()


@dp.message_handler(state=Test.Q12)
async def answer_q12(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer12"] = answer
    await message.answer("Вопрос №13\n" "Обрабатываете ли Вы эти данные?")
    await Test.next()


@dp.message_handler(state=Test.Q13)
async def finish_test(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer13"] = answer
    await message.answer("Спасибо за ваши ответы!\n", reply_markup=kb.end_kb)
    data = await state.get_data()
    await state.finish()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(
        "Привет!\n",
        "Этот бот предназначен для опроса. Выберите одну из опций\n",
        reply_markup=kb.info_kb)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(
        "Этот бот предназначен для опроса. Напишите /test и ответьте на вопросы.",
        reply_markup=kb.info_kb)


@dp.message_handler()
async def any_message(message: types.Message):
    await message.answer(
        "Вы уже прошли опрос. Если хотите пройти заново - перезапустите бота\n"
    )


if __name__ == '__main__':
    executor.start_polling(dp)
