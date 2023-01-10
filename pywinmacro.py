#-*-coding:'euc-kr'
"""
Author : Byunghyun Ban
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
"""

import win32api
import win32con
import win32gui
import pyperclip

# ���̺귯������ ����� Ű���� �̸� �����մϴ�.
KEYMAP = {
    # ���� Ű
    "esc": 0x1B,  "window": 0x5B,
    "control": 0x11,    "alt": 0x12,  "kor_eng": 0x15,
    "print_screen": 0x2C,    "scroll_lock": 0x91,   "pause_break": 0x13,

    # ��� Ű
    "f1": 0x70,    "f2": 0x71,    "f3": 0x72,    "f4": 0x73,
    "f5": 0x74,    "f6": 0x75,    "f7": 0x76,    "f8": 0x77,
    "f9": 0x78,    "f10": 0x79,    "f11": 0x7A,    "f12": 0x7B,

    # ȭ��ǥ Ű
    "left_arrow": 0x25,    "right_arrow": 0x27,
    "up_arrow": 0x26,    "down_arrow": 0x28,

    # Ž�� Ű
    "insert": 0x2D,    "home": 0x24,    "page_up": 0x21,
    "delete": 0x2E,    "end": 0x23,     "page_down": 0x22,

    # �Է� Ű (����)
    "backspace": 0x08,  "enter": 0x0D,  "shift": 0x10,
    "tab": 0x09,    "caps_lock": 0x14,  "spacebar": 0x20,

    # �Է� Ű (����)
    "0": 0x30,    "1": 0x31,    "2": 0x32,    "3": 0x33,    "4": 0x34,
    "5": 0x35,    "6": 0x36,    "7": 0x37,    "8": 0x38,    "9": 0x39,

    # �Է� Ű (���ĺ�)
    "a": 0x41,    "b": 0x42,    "c": 0x43,    "d": 0x44,    "e": 0x45,
    "f": 0x46,    "g": 0x47,    "h": 0x48,    "i": 0x49,    "j": 0x4A,
    "k": 0x4B,    "l": 0x4C,    "m": 0x4D,    "n": 0x4E,    "o": 0x4F,
    "p": 0x50,    "q": 0x51,    "r": 0x52,    "s": 0x53,    "t": 0x54,
    "u": 0x55,    "v": 0x56,    "w": 0x57,    "x": 0x58,    "y": 0x59,  "z": 0x5A,

    # �Է� Ű (Ư������)
    ";": 0xBA,    "=": 0xBB,    ",": 0xBC,    "-": 0xBD,    ".": 0xBE,
    "/": 0xBF,    "`": 0xC0,    "[": 0xDB,    "\\": 0xDC,    "]": 0xDD,
    "'": 0xDE,

    # ���е�
    "num_lock": 0x90, "numpad_/": 0x6F, "numpad_*": 0x6A,
    "numpad_-": 0x6D, "numpad_+": 0x6B, "numpad_.": 0x6E,
    "numpad_7": 0x67, "numpad_8": 0x68, "numpad_9": 0x69,
    "numpad_4": 0x64, "numpad_5": 0x65, "numpad_6": 0x66,
    "numpad_1": 0x61, "numpad_2": 0x62, "numpad_3": 0x63,
    "numpad_0": 0x60,
}


# �빮�� Ư�����ڸ� ���� ��ųʸ��Դϴ�.
UPPER_SPECIAL = {
    "!": 1,    "@": 2,    "#": 3,    "$": 4,    "%": 5,    "^": 6,
    "&": 7,    "*": 8,    "(": 9,    ")": 0,    "_": "-",   "~": '`',    "|": '\\',
    "{": "[",   "}": "]",    ":": ";",    '"': "'", "?": "/", "<": ",", ">": "."
}


# ���콺�� Ư����ġ�� �̵���Ű�� �Լ�
def move_mouse(location):
    # location �� �Է¹޾� �� ��ġ�� ���콺�� �̵���ŵ�ϴ�.
    win32api.SetCursorPos(location)


# ���콺�� ���� ��ǥ�� ���ϴ� �Լ�
def get_mouse_position():
    # ���콺 Ŀ���� ���� ��ġ�� ����մϴ�.
    # ��ũ�θ� �����ϴ� ��������, �ֿܼ��� �ҷ��ͼ� ���� �����մϴ�.
    return win32gui.GetCursorPos()


# ������ ��ġ�� ���콺 Ŀ���� �̵��ϰ� ���� ��ư�� Ŭ���ϴ� �Լ�
def click(location):
    # ���콺�� �̵���ŵ�ϴ�.
    move_mouse(location)
    # ���� ��ư�� Ŭ���մϴ�.
    l_click()


# ������ ��ġ�� ���콺 Ŀ���� �̵��ϰ� ������ ��ư�� Ŭ���ϴ� �Լ�
def right_click(location):
    # ���콺�� �̵���ŵ�ϴ�.
    move_mouse(location)
    # ���� ��ư�� Ŭ���մϴ�.
    r_click()


# ����Ŭ��
def double_click(location):
    # ���콺�� �̵���ŵ�ϴ�.
    move_mouse(location)
    # ���� ��ư�� Ŭ���ϴ� �Լ��� �� �� ȣ���մϴ�.
    l_click()
    l_click()


# Ű�� �� �� �����ٰ� ���� �Լ��Դϴ�.
def key_press_once(key):
    # Ű�� �����ϴ�.
    key_on(key)
    # Ű�� ���ϴ�.
    key_off(key)


# ���� �Է� (Ŭ�����忡 ���� �� �ٿ��ֱ�)
# �ѱ��� ��쿡�� ����ϼ���. �ѱ��� ���¼� ���ذ� ����Ͽ� �׷����ϴ�.
def type_in(string):
    # Ŭ�����忡 ��Ʈ���� ����ֽ��ϴ�.
    pyperclip.copy(string)
    # Ctrl v�� �ٿ��ֱ� �մϴ�.
    ctrl_v()


# ����, ����, Ư�����ڷ� �� ��Ʈ���� �ٷ� �Է��ϴ� �Լ��Դϴ�.
def typing(string):
    for el in string:
        if el.isupper():
            key_on("shift")
            key_press_once(el.lower())
            key_off("shift")
        elif el in UPPER_SPECIAL:
            key_on("shift")
            key_press_once(UPPER_SPECIAL[el])
            key_off("shift")
        else:
            key_press_once(el)


# Ű�� ��� ������ �ֵ��� �ϴ� �Լ��Դϴ�.
def key_on(key):
    # �������� KEYMAP�� ������ ������ �����մϴ�.
    global KEYMAP
    # �Է¹��� ���� �ҹ��ڷ� ��ȯ�մϴ�.
    key = str(key)
    if key.isupper:
        key = key.lower()
    try:
        # Ű�ʿ��� Ű �ڵ带 �̾ƿɴϴ�.
        key_code = KEYMAP[key.lower()]
        win32api.keybd_event(key_code, 0, 0x00, 0)
    except KeyError:
        # Ű�ʿ� ���õ��� ���� Ű�� ��û�߽��ϴ�. �����޽����� ����մϴ�.
        print(key + " is not an available key input.")
        # ���α׷��� �����մϴ�.
        exit(1)


# ������ Ű�� ���� �ϴ� �Լ��Դϴ�.
def key_off(key):
    # �������� KEYMAP�� ������ ������ �����մϴ�.
    global KEYMAP
    # �Է¹��� ���� �ҹ��ڷ� ��ȯ�մϴ�.
    key = str(key)
    if key.isupper:
        key = key.lower()
    try:
        # Ű�ʿ��� Ű �ڵ带 �̾ƿɴϴ�.
        key_code = KEYMAP[key.lower()]
        win32api.keybd_event(key_code, 0, 0x02, 0)
    except KeyError:
        # Ű�ʿ� ���õ��� ���� Ű�� ��û�߽��ϴ�. �����޽����� ����մϴ�.
        print(key + " is not an available key input.")
        # ���α׷��� �����մϴ�.
        exit(1)


# ���콺�� ���� �ڸ����� ���� ��ư�� Ŭ���ϴ� �Լ�
def l_click():
    # ���콺 ���� ��ư�� �����ϴ�.
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # ���콺 ���� ��ư�� ���ϴ�.
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# ���콺�� ���� �ڸ����� ������ ��ư�� Ŭ���ϴ� �Լ�
def r_click():
    # ���콺 ������ ��ư�� �����ϴ�.
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    # ���콺 ������ ��ư�� ���ϴ�.
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


# ���콺 ��ũ���� �ø��� �Լ�
def mouse_upscroll(number=1000):
    x, y = get_mouse_position()
    # �� ĭ�̳� �ø��� number�� �Է¹޽��ϴ�.
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, x, y, number, 0)

# ���콺 ��ũ���� ������ �Լ�
def mouse_downscroll(number=1000):
    x, y = get_mouse_position()
    # �� ĭ�̳� ������ number�� �Է¹޽��ϴ�. �⺻�� �� ĭ �����ϴ�.
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, x, y, -1*number, 0)


# �巡�׵�� �Լ�
def drag_drop(frm, to):
    # ��ǥ���� �Է¹޽��ϴ�.
    x1, y1 = frm
    x2, y2 = to
    # Ŭ�� ������������ Ŀ���� �ű�ϴ�.
    move_mouse(frm)
    # ���� ��ư�� Ŭ���մϴ�.
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # Ŭ���� ������ ä�� ���콺 ��ġ�� �̵���ŵ�ϴ�.
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x2-x1, y2-y1, 0, 0)
    # ���콺 ��ư�� ���ϴ�.
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# Ư�� ��ǥ�� ������ 16������ �о� ���� �Լ��Դϴ�.
def get_color(location):
    # ��ǥ�� ���մϴ�.
    x, y = location
    # win32gui���� ������ �� ����, 16������ ��ȯ�Ͽ� �����մϴ�.
    return hex(win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y))


# Ctrl C (����)
def ctrl_c():
    # Ctrl�� �����ϴ�.
    key_on("control")
    # c�� �����ϴ�.
    key_on("c")
    # �� Ű�� ��� ���ϴ�.
    key_off("control")
    key_off("c")


# Ctrl V (�ٿ��ֱ�)
def ctrl_v():
    # Ctrl�� �����ϴ�.
    key_on("control")
    # v�� �����ϴ�.
    key_on("v")
    # �� Ű�� ��� ���ϴ�.
    key_off("control")
    key_off("v")


# Ctrl A (��� ����)
def ctrl_a():
    # Ctrl�� �����ϴ�.
    key_on("control")
    # a�� �����ϴ�.
    key_on("a")
    # �� Ű�� ��� ���ϴ�.
    key_off("control")
    key_off("a")


# Ctrl F (ã��)
def ctrl_f():
    # Ctrl�� �����ϴ�.
    key_on("control")
    # a�� �����ϴ�.
    key_on("f")
    # �� Ű�� ��� ���ϴ�.
    key_off("control")
    key_off("f")


# Alt F4 (����)
def alt_f4():
    # Alt�� �����ϴ�.
    key_on("alt")
    # F4�� �����ϴ�.
    key_on("f4")
    # �� Ű�� ��� ���ϴ�.
    key_off("alt")
    key_off("f4")


# Alt Tab (ȭ�� ��ȯ)
def alt_tab():
    # Alt�� �����ϴ�.
    key_on("alt")
    # F4�� �����ϴ�.
    key_on("tab")
    # �� Ű�� ��� ���ϴ�.
    key_off("alt")
    key_off("tab")

