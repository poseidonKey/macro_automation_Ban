
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pywinmacro as pw
import pyperclip

querry = "https://www.google.com/search?tbm=nws&q="
options = Options()
options.add_argument("--window-size=1600,900")
driver = webdriver.Chrome(
    "./chromedriver.exe", options=options)
news_list = []
news_text = ""
keyword = sys.argv[1]
driver.get(querry + keyword)
# 로딩이 오래 걸릴 수 있으니 잠시 대기합니다.
time.sleep(3)

pw.ctrl_a()
# 한 번 눌러서는 안 될 때도 있습니다. 한국인의 근성을 보여줍시다.
time.sleep(1)
pw.ctrl_c()
time.sleep(1)
pw.ctrl_c()
time.sleep(1)
pw.ctrl_c()
# 뉴스 리스트를 초기화합니다.
news_list = []
# 텍스트를 클립보드에서 추출해 스트링으로 따 옵니다.
news_text = pyperclip.paste()
# 한 줄씩 쪼개줍니다.
splt = news_text.split("\n")

# 구글 뉴스는 이미지 정보, 헤드라인, 게시 시간, 본문 요약 순으로 정보가 제공됩니다.
# 내용물을 한 줄씩 읽으면서 정보를 취합해 봅시다.

# 글자들을 한 줄씩 불러옵니다.
for i, line in enumerate(splt):
    # 길이가 너무 짧은 줄은 건너뜁니다. 공백일 가능성이 큽니다.
    if len(line.strip()) < 3:
        continue
    # 뉴스의 작성 시점을 알려주는 문자가 등장하면 앞의 3개 줄을 뽑아와 하나로 합쳐 줍니다.
    elif line.strip()[-3:] in "달 전  주 전  일 전  시간 전  분 전  초 전":
        new_news = "\n".join(splt[i - 3:i])
        # 만들어진 뉴스를 news_list에 삽입합니다.
        news_list.append(new_news)

print(news_list)
