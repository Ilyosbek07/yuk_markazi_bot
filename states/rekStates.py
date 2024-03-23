from aiogram.dispatcher.filters.state import State, StatesGroup


class RekData(StatesGroup):
    curer = State()
    group_id = State()
    get_users_args_state = State()
    choice = State()
    picture = State()
    score = State()
    text = State()
    shart = State()
    gift = State()
    add = State()
    delete = State()
    add_secret = State()
    delete_secret = State()
    kbsh = State()
    winners = State()
    score_0 = State()
    test = State()
    send_user = State()
    add_list_plus_channel = State()
    add_list_minus_channel = State()
    add_list_plus = State()
    add_list_minus = State()


class Number(StatesGroup):
    number = State()
    add_user = State()


class DelUser(StatesGroup):
    add = State()
    user = State()
    fix = State()


class SolveTestState(StatesGroup):
    a1 = State()
    a2 = State()
    a3 = State()
    a4 = State()
    a5 = State()
    check = State()


class QuestionsState(StatesGroup):
    a1 = State()
    q2 = State()
    a2 = State()
    q3 = State()
    a3 = State()
    q4 = State()
    a4 = State()
    q5 = State()
    a5 = State()
    check = State()
    admin_check = State()


class AllState(StatesGroup):
    env = State()
    env_remove = State()
class TrackState(StatesGroup):
    region = State()
    district = State()
    to_region = State()
    to_district = State()
    description = State()
    data = State()
    status = State()
    get_order = State()

