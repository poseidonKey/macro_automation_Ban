# -*-coding:'euc-kr'
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6개월 치 업무를 하루 만에 끝내는 업무 자동화
Last Modification : 2020.03.02.
"""

import sys
import time
import twitter_bot_news as tb


# 작업 시작 메시지를 출력합니다.
print("Process Start.")

# 시작 시점의 시간을 기록합니다.
start_time = time.time()

# 아이디를 입력받습니다.
id = sys.argv[1]

# 패스워드를 입력받습니다.
ps = sys.argv[2]

# 검색어를 입력받습니다.
# keyword = sys.argv[3].strip()
keyword = "코로나19"

# 크롤러를 불러옵니다.
BOT = tb.NewsBot()
time.sleep(3)
# 로그인을 시도합니다.
BOT.login(id, ps)

# 뉴스와 함께 삽입할 해시태그를 입력합니다.
hashtags = "#뉴스 #스크랩 하는 #자동화 #코드"

# 구글에서 뉴스를 검색하고,
# 트위터에 자동으로 로그인 한 뒤,
# 긁어온 모든 뉴스를 업로드까지 합니다.
BOT.tweet_all_news(keyword, hashtags)

# 결과 화면을 잠시 감상하기 위해 10초동안 방치합니다.
time.sleep(10)

# 크롤러를 닫아줍니다.
BOT.kill()

# 작업 종료 메세지를 출력합니다.
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
