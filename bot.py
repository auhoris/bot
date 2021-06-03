from aiogram import Bot, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN_BOT
from test import Test
import keyboard as kb
from make_file import make_file
from count_yes import count_yes

# TODO:  <03-06-21, yourname> #
# 1) Cчетчик
# 2) Добавить неск вопросов
# 3) По возможности разобраться с cancel

storage = MemoryStorage()
bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["test"], state=None)
async def enter_test(message: types.Message):
    await message.answer(
        "Вы начали тестирование.\n"
        "Вы согласны на обработку персональных данных?",
        reply_markup=kb.one_time_answer)
    await Test.INFO.set()


@dp.message_handler(state=Test.INFO)
async def answer_personal_data(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "Нет":
        await message.reply('Завершаем опрос.\n',
                            reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    await message.answer("ФИО: ")
    await Test.next()


@dp.message_handler(state=Test.FIO)
async def answer_info(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["FIO"] = answer
    await message.answer("Ваша почта: ")
    await Test.next()


@dp.message_handler(state=Test.EMAIL)
async def answer_email(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["Email"] = answer
    await message.answer("Форма организации: ")
    await Test.next()


@dp.message_handler(state=Test.ORG_FORM)
async def answer_org_from(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["Org_form"] = answer
    await message.answer("Имя организации: ")
    await Test.next()


@dp.message_handler(state=Test.ORG_NAME)
async def answer_org_name(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["Org_name"] = answer
    await message.answer("Должность: ")
    await Test.next()


@dp.message_handler(state=Test.POS)
async def answer_position(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["Position"] = answer
    await message.answer("Номер телефона: ")
    await Test.next()


@dp.message_handler(state=Test.PHONE)
async def answeer_phone(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["Phone"] = answer
    await message.answer(
        "Вопрос №1\nЕсть ли место, где вы храните информацию для принятия решений?",
        reply_markup=kb.answer_kb)
    await Test.next()


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
    await message.answer("Вопрос №13\n" "Вы агрегируете данные?")
    await Test.next()


@dp.message_handler(state=Test.Q13)
async def answer_q13(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer13"] = answer
    await message.answer("Вопрос №14\n" "Обрабатываете ли Вы эти данные?")
    await Test.next()


@dp.message_handler(state=Test.Q14)
async def answer_q14(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer14"] = answer
    await message.answer(
        "Вопрос №15\n"
        "Входит ли оценка в функциональные обязанности кого-то из участников организации?"
    )
    await Test.next()


@dp.message_handler(state=Test.Q15)
async def answer_q15(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer15"] = answer
    await message.answer(
        "Вопрос №16\n"
        "У вас есть \"План оценки социального эффекта / воздействия на общество (impact)\", который определяет, каким образом, в какие сроки и кем будет собрана доказательная информация (evidence)?"
    )
    await Test.next()


@dp.message_handler(state=Test.Q16)
async def answer_q16(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer16"] = answer
    await message.answer(
        "Вопрос №17\n"
        "Сотрудники, отвечающие за сбор данных, получают поддержку, которая обеспечивает регулярное поступление достоверной доказательной информации?"
    )
    await Test.next()


@dp.message_handler(state=Test.Q17)
async def answer_q17(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer17"] = answer
    await message.answer(
        "Вопрос №18\n"
        "Вы собираете подтверждающую информацию \"до\" и \"после\" того, как ваши благополучатели смогут наблюдать изменения, возникающие в результате нашей работе?"
    )
    await Test.next()


@dp.message_handler(state=Test.Q18)
async def answer_q18(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer18"] = answer
    await message.answer(
        "Вопрос №19\n"
        "Чтобы выяснить, какие изменения (и почему) происходят в практике ваших благополучателей, вы сопоставляете информацию разного типа?"
    )
    await Test.next()


@dp.message_handler(state=Test.Q19)
async def answer_q19(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer19"] = answer
    await message.answer(
        "Вопрос №20\n"
        "Вы можете объяснить, каким образом результаты вашей работы связаны с решением комплексных экономических, социальных и экологических проблем?"
    )
    await Test.next()


@dp.message_handler(state=Test.Q20)
async def finish_test(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer20"] = answer
    await message.answer("Спасибо за ваши ответы!\n", reply_markup=kb.end_kb)
    data = await state.get_data()
    c_of_yes = count_yes(data)
    await message.answer(f"{c_of_yes}/20 ответов 'Да'\n")
    make_file(data)
    await state.finish()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(
        "Привет!\nЭтот бот предназначен для опроса. Выберите одну из опций\n",
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


@dp.message_handler(state='*', commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за ваши ответы!\n")
    await state.finish()


# @dp.message_handler(state='*', commands='cancel')
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
# async def cancel_handler(message: types.Message, state: FSMContext):
#     """
#     Allow user to cancel any action
#     """
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#     await state.finish()
#     await message.reply('Завершаем опрос.\n',
#                         reply_markup=types.ReplyKeyboardRemove())

if __name__ == '__main__':
    executor.start_polling(dp)
