import multiprocessing
import queue
import threading

from . import consts

input_queue = multiprocessing.Queue()
output_queue = multiprocessing.Queue()
notify_queue = multiprocessing.Queue()

task_queue = queue.Queue()

CONFIG = None

FINISHED_COUNT = 0

# 程序运行
G_RUN = threading.Event()

#
G_OUT_WORKER = threading.Event()

# 退出循环事件
G_RACE_RUN_EVENT = threading.Event()
G_RACE_QUIT_EVENT = threading.Event()

# 是否活跃状态
NO_OPERATION_COUNT = 0

# 游戏模式
MODE = ""

# 段位
DIVISION = ""

# 选车次数
SELECT_COUNT = {
    consts.mp1_zh: 0,
    consts.mp2_zh: 0,
    consts.mp3_zh: 0,
    consts.car_hunt_zh: 0,
    consts.legendary_hunt_zh: 0,
    consts.custom_event_zh: 0,
    consts.career_zh: 0,
}
# 是否选车
SELECT_CAR = {
    consts.mp1_zh: True,
    consts.car_hunt_zh: True,
    consts.legendary_hunt_zh: True,
}

# 比赛次数
RACE_COUNT = {
    consts.mp1_zh: 0,
    consts.mp2_zh: 0,
    consts.mp3_zh: 0,
    consts.car_hunt_zh: 0,
    consts.legendary_hunt_zh: 0,
    consts.custom_event_zh: 0,
    consts.career_zh: 0,
}

# 比赛排名统计
RACE_RANK = {
    consts.mp1_zh: {i: 0 for i in range(1, 9)},
    consts.mp2_zh: {i: 0 for i in range(1, 9)},
    consts.mp3_zh: {i: 0 for i in range(1, 9)},
    consts.car_hunt_zh: {i: 0 for i in range(1, 5)},
    consts.legendary_hunt_zh: {i: 0 for i in range(1, 5)},
    consts.custom_event_zh: {i: 0 for i in range(1, 9)},
    consts.career_zh: {i: 0 for i in range(1, 9)},
}

# 按地图统计
TRACK_RANK = {
    consts.mp1_zh: {},
    consts.mp2_zh: {},
    consts.mp3_zh: {},
    consts.car_hunt_zh: {},
    consts.legendary_hunt_zh: {},
    consts.custom_event_zh: {},
    consts.career_zh: {},
}

# Not Support Track
NOT_SUPPORT_TRACK = []

# Not Recongnized Track
NOT_RECOGNIZED_TRACK = []

# Event
EVENT_UPDATE = False

# 比赛中
RACING = 0
