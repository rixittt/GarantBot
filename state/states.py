
from aiogram.fsm.state import State, StatesGroup
class search(StatesGroup):
    user_id = State()


class deposit(StatesGroup):
    sum = State()


class deal(StatesGroup):
    sum = State()
