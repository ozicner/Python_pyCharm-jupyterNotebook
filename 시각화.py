# 예제01.
# 환경 설정 방법
# File > Setting > matplotlib 설치
# 예제02.
# 1) 형태01.
import matplotlib.pyplot
# matplotlib.pyplot.plot()
# matplotlib.pyplot.show()
# 2) 형태02. pyplot 생략하고 출력 가능
# from matplotlib.pyplot import *
# plot()
# show()
# 3) 형태03.
# import matplotlib.pyplot as plt
# plt.plot()
# plt.show()
# 예제03. plot의 종류
# 1) lineplot: 점과 점 사이를 선으로 이어줌
# 2) barplot: 막대그래프 형태로 보여줌 (barchart)
# 3) histogram(히스토그램) plot
# 4) scatter plot
# 5) contour(컨투어) plot
# 6) surface plot
# 7) box plot
# 예제04. 그래프의 title 설정
# import matplotlib.pyplot as plt
# plt.title("title")
# plt.show()
# 예제05. 리스트 설정
# 1)
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16])     # y축 값으로 설정됨
# plt.show()
# 2)
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16], [10, 20, 30, 40])       # 순서대로 x축, y축 값으로 설정됨
# plt.show()
# 3)
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16], [10, 20, 40])       # x,y 갯수 안맞으면 불가능
# plt.show()
# 4)
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16], [10, 20, 30, 40])
# plt.grid(True)      # 격자 보여줌 -> 아무데나 써도 나옴
# plt.show()
# 5)
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16], [10, 20, 30, 40])
# plt.xlabel("x-label")       # x축 이름
# plt.ylabel("y-label")       # y축 이름
# plt.show()
# 6) 기존의 plot을 그대로 유지한 채 새로운 plot을 추가하는 것을 "hold"라고 함
# import matplotlib.pyplot as plt
# plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
# plt.plot([10, 20, 30, 40], [3, 7, 11, 20])
# plt.plot([10, 20, 30, 40], [5, 8, 13, 24])
# plt.show()
# 7)
# import matplotlib.pyplot as plt
# plt.plot([10, 20, 30, 40], range(4))        # range로도 나타낼 수 있음
# plt.plot([10, 20, 30, 40], range(2, 6))
# plt.show()
# 8)
# import matplotlib.pyplot as plt
# plt.plot(range(1, 5), "r")      # 색상 설정
# plt.plot(range(2, 6), "g")
# plt.plot(range(3, 7), "b")
# plt.plot(range(4, 8), "c")
# plt.plot(range(5, 9), "m")
# plt.plot(range(6, 10), "y")
# plt.plot(range(7, 11), "k")
# plt.plot(range(8, 12), "w")
# plt.show()
# 9)
# import matplotlib.pyplot as plt
# plt.plot(range(8, 12), range(1, 5), "m")
# plt.show()
# 10) 마크 설정
# import matplotlib.pyplot as plt
# a = '.,ov^<>w1234sp*hH+xDd'     # 문자열로도 끄집어낼 수 있다
# for k, v in enumerate(a):
#     print(k, v)
#     plt.plot(range(1+k, 5+k),  v + '-')
# plt.show()
# 11) 선 스타일 설정
# import matplotlib.pyplot as plt
# plt.plot(range(1, 5), '-')
# plt.plot(range(2, 6), '--')
# plt.plot(range(3, 7), '-.')
# plt.plot(range(4, 8), ':')
# plt.show()
# 12) 색상+마크+선스타일 모두
# import matplotlib.pyplot as plt
# plt.plot(range(2, 6), 'r^:')        # 세가지 한번에 설정(색상, 마크, 선스타일 순서로)
# plt.plot(range(1, 7), range(4, 10), 'co-.')        # 세가지 한번에 설정(색상, 마크, 선스타일 순서로)
# plt.show()
# 13) 선 세부 설정
# import matplotlib.pyplot as plt
# plt.plot(
#     [10, 20, 30, 40],  # x축
#     [1, 4, 9, 16],   # y축
#     c="m",    # 선 색깔
#     lw=4,     # 선 굵기
#     ls=":",      # 선 스타일
#     marker="^",       # 마커 종류
#     ms=5,        # 마커 크기
#     mec="g",      # 마커 선 색깔
#     mew=10,        # 마커 선 굵기
#     mfc="y"       # 마커 내부 색깔
# )
# plt.show()
# 14)
# import matplotlib.pyplot as plt
# plt.plot([1, 4, 9, 16], [10, 20, 30, 40], 'co-.')
# plt.xlim(-10, 30)       # x의 유효범위
# plt.ylim(-20, 70)       # y의 유효범위
# plt.grid(True)
# plt.show()
#
#
#15)
import matplotlib.pyplot as plt
# plt.plot([10,20,30,40], [5,6,7,8])
# plt.xticks([10,20,30])
# plt.yticks(range(0,10))# 엑스틱, 와이틱 눈금자
# plt.show()
#
# plt.xticks([1,2,3,4], ['one day', 'two day', 'three day', 'four day'], rotation='50') # x축 값이 너무 길면 회전 시켜줌
# plt.yticks([1,2,3,4], ['tiger', 'lion', 'dog', 'cat'])
# plt.show()
#
# plt.plot([10, 20, 30, 40], label='tiger') # 라벨을 달겠다
# plt.plot([5, 10, 20, 25], label='lion')
# plt.legend(loc=4)  # 범례를 표시하고 loc의 숫자로 위치를 조정
# plt.show()
#
# plt.gca().set_facecolor([0.91, 0.78, 0.86])  # 그래프의 배경색 설정, 16진수를 RGB값으로 변경, 0~1범위이며 0.1은 10 0.5는 50
# plt.show()
#
# plt.figure(figsize=(6.4*1.5, 4.8*1.5))  # 그래프 창 크기 조절, 디폴트 값이 6.4, 4.8
# plt.show()
#
# 한글 깨짐 처리
import matplotlib.font_manager as fm
# font_location = 'C:/Windows/Fonts/malgun.ttf'  # 폰트 위치와 정보 가져옴
# font_family = fm.FontProperties(fname=font_location).get_name()
# plt.rc('font', family=font_family)
# plt.plot(['호랑이', '독수리', '코끼리'])
# plt.show()
#
# plt.subplot(3,3, 1)  # 하나의 플롯에 최대 4개의 그래프 출력, 세번째 인수가 창의 위치를 나타냄
# plt.plot([1,2,3,4], [10,20,30,40])
# plt.subplot(2,2, 2)  # 인수1,2는 플롯을 가로 2칸 세로 2칸으로 보고 위치를 정하겠다는것
# plt.plot([1,2,3,4], [10,20,30,40])
# plt.subplot(2,2, 3)
# plt.plot([1,2,3,4], [10,20,30,40])
# plt.subplot(3,3, 9)
# plt.plot([1,2,3,4], [10,20,30,40])
# plt.show()
#
# y축 공동 활용
# age = [10, 20, 30, 40, 50, 60]
# weight = [20, 40, 55, 50, 70, 63]
# height = [100, 120, 140, 150, 170, 165]
# plt.plot(age, weight, 'b')
# plt.twinx()
# plt.plot(age, height, 'r')
# plt.show()
#
# plt.plot([10,20,30], [5,10,15])  # 그래프 생성해서 png 이미지로 저장, 좌측 파일목록에서 확인
# fig = plt.gcf()
# plt.show()
# fig.savefig('test.png')
#
# plt.bar([1,2,3], [2,3,1])  # 바 그래프(차트)출력
# plt.show()
#
# plt.barh([1,2,3], [2,3,1])  # 바 그래프 가로 출력, 데이터가 많을 경우 가독성 더 좋음
# plt.show()
#
# a = ['PYTHON', 'C++', 'JAVA', 'SCALAR', 'LISP', 'PEARL', 'JAVA SCRIPT']
# b = [12, 10, 8, 6, 4, 2, 1]
# plt.subplot(1,2,1)
# plt.barh(a, b, align='edge')  # 데이터 눈금선의 끝쪽에 맞춰 정렬
# plt.subplot(1,2,2)
# plt.bar(a, b, align='center')  # 데이터 눈금선의 중앙에 맞춰 정렬, 디폴트 값
# plt.show()
#
# plt.bar(a, b, 0.3, 10, align='edge', alpha=0.45)
#
# alpha값은 배경과 그래프 색깔을 얼마나 섞는가, 블렌딩, 투명도
# def bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs): # 세번째 인수는 바 그래프의 너비로 디폴트 값이 있어서 기본적으로 입력안함, 네번째 인수는 시작 기준 값을 지정
# plt.show()   # 원하는 명령어나 함수명 뒤에서 우클릭-고투-디클레이션 오얼 유스에이지, 메뉴얼 안내
#
import numpy as mp
# a = [0,1,2,3]
#
# a = a+3  # 불가
#
# a = range(4)  # 역시 리스트라서 불가
# a = a+3
#
# a = mp.arange(4)  # 가능, 리스트 값에 각각 덧셈
# a = a+2
# print(type(a))  # 결과에 콤마 없음, 타입 다름
# print(a)
#
# a = plt.bar(mp.arange(4)+0.5, [90, 55, 40, 65], 0.4, color='m', label='A')  # 그래프 막대가 중첩 출력
# b = plt.bar(mp.arange(4)+0.2, [65, 40, 55, 95], 0.4, color='g', label='B')
# plt.legend(loc=9)
# plt.show()
#
# a = plt.bar(mp.arange(4), [90, 55, 40, 65], 0.4)  # 바탐, 시작기준을 데이터 별로 다르게 설정
# b = plt.bar(mp.arange(4), [65, 40, 55, 95], 0.4, bottom=[90, 55, 40, 65])  # 위 데이터와 연계 출력
# plt.show()
#
# 연도별 석탄 채굴량 그래프
# import matplotlib.pyplot as plt
# from random import *
# import matplotlib.font_manager as fm
#
# font_location = 'C:/Windows/Fonts/malgun.ttf'
# font_family = fm.FontProperties(fname=font_location).get_name()
# plt.rc('font', family=font_family)
#
# year = [1900 + i*10 for i in range(12)]
# x = []
#
# for _ in range(12):
#     a = randint(100, 1000)
#     x.append(a)
# print(x)
#
# plt.barh(year, x, width=5, color='g')
# plt.barh(year, x, align='edge', color='g')
# plt.title("년도별 석탄 채굴량")
# plt.xlabel("연도")
# plt.ylabel("석탄 채굴량")
# plt.xticks(rotation=30)
# plt.grid("True")
# plt.show()
# 
# 추출 데이터 유형:
# 나이대별급여/직업별급여차이/성별급여차이/학과별경쟁율차이/월별수익률/팀별성적/동물원별사자와호랑이의개체수/국가별남녀인구수
#
#
#
#
# 판다스 : 보통 2차원 데이터 프레임 구현 목적
#
# 데이터 프레임 생성, 딕쇼너리
import pandas as pd
#
# data = {'이름': ['홍길동','이순신','유관순'],
#      '나이': [30,40,50],
#      '고향': ['서울','부산','대구']}
# df = pd.DataFrame(data)
# print(df)
#
# # 데이터 프레임 생성, 리스트
# a = [10,20,30,40]  # 많은 부분에서 필드의 성격을 지닌다
# b = [50,60,70,80]
# c = [a,b]
# df = pd.DataFrame(c).T  # .T 로 필드의 성격으로 바꿔줌
# df.columns = ['나이','급여']  # 위에 .T 여부 따라 컬럼수 맞춰줘야함
# print(df)
#
# df = pd.DataFrame(columns=('이름', '나이', '고향'))  # 컬럼만 생성
# print(df)
# print(len(df))  # 0이 출력됨. 로우값이 없다는 뜻
#CRUD/ 생성,갱신,삭제
# df.loc[20] = ['호랑이', '30', '서울']  # 20은 키값이고 컬럼순으로 데이터 입력, 생성
# df.loc[30] = ['너구리', '20', '부산']
# df.loc[40] = ['두루미', '25', '인천']  # 중복된 키값에 데이터 입력시 최신껄로 갱신
#
#
# for i in range(10):
#     df.loc[len(df)] = ["이순신" + str(i), 50+i, "울산"]
# print(df)
#
# a = df.drop([20])  # 원본 보존하고 출력만 삭제
# df = df.drop([20])  # 완전 삭제
# print(df)
#
# print(df.loc[20])  # 키값으로 데이터 검색
# print(df.head())  # 상위 5개 데이터만 출력, 원하는 숫자 넣어서 검색 가능
# print(df.tail())  # 하위 5개 데이터만 출력
#
# print(df.tail());print('-'*30)
#
#
#
import numpy as np
# x = np.array([[1., 2., 3.],
#               [4., 5., 6.]])
# y = np.array([[6., 23.],
#               [-1, 7],
#               [8, 9]])
# print(x); print(sep="*")
# print(y); print(sep="*")
# print(x.dot(y))
# print(np.dot(x, y)); print(sep="*")     # 동일( x.dot(y) = np.dot(x, y) )
# print(np.ones(3))
# print(np.dot(x, np.ones(3)))
# print(x @ np.ones(3)); print(sep="*")
# ##########################################################################
# from numpy.linalg import inv, qr
# x = np.random.randn(3, 3)
# print(x); print(sep="*")
# print(x.T); print(sep="*")
# y = inv(x)      # 역행렬 구하기
# print(y); print(sep="*")
# mat = x.T.dot(x)
# print(inv(mat)); print(sep="*")
# a = np.array([1, 2, 3])
# b = np.diag(a)          # diag:
# print(np.trace(b)); print(sep="*")      # trace: 대각선 원소의 합
# # A*x=b에서 x 값 구하기
# # 문제1)
# A = np.array([[1,2],
#               [3,4]])
# b = np.array([[6,7],
#               [8,9]])
# x = np.linalg.solve(A,b)
# print(x); print(sep="*")
# # 문제2)
# A = np.array([[2, 3],
#               [3, 1]])
# b = np.array([[5],
#               [2]])
# x = np.linalg.solve(A, b)
# print(x); print(sep="*")
#
#
# import math
#
# print(math.radians(30))
#
#
# # 사각형의 이동
# import matplotlib.pyplot as plt
# x = [10, 20, 20, 10, 10]
# y = [10, 10, 20, 20, 10]
# dx = 50
# dy = 30
# c = []
# d = []
# for i in range(len(x)):
#     e = x[i]
#     f = y[i]
#     a = [[1, 0, dx], [0, 1, dy], [0, 0, 1]]
#     b = [[e], [f], [1]]
#     t = np.dot(a, b)
#     c.append(t[0])
#     d.append(t[1])
# # 회전하는 사각형( 원점을 기준으로, 각도는 30으로 고정 )
# c1 = []
# d1 = []
# for i in range(len(x)):
#     e = x[i]
#     f = y[i]
#     a1 = [[np.sqrt(3)/2, -1/2, 0], [1/2, np.sqrt(3)/2, 0], [0, 0, 1]]
#     b1 = [[e], [f], [1]]
#     t = np.dot(a1, b1)
#     c1.append(t[0])
#     d1.append(t[1])
# # # 제자리에서 회전한 사각형하기
# x1 = [-5, 5, 5, -5, -5]
# y1 = [-5, -5, 5, 5, -5]
# c2 = []
# d2 = []
# # 원점에서 회전
# for i in range(len(x)):
#     e = x1[i]
#     f = y1[i]
#     a1 = [[np.sqrt(3)/2, -1/2, 0], [1/2, np.sqrt(3)/2, 0], [0, 0, 1]]
#     b1 = [[e], [f], [1]]
#     t = np.dot(a1, b1)
#     c2.append(t[0])
#     d2.append(t[1])
# # 회전한 사각형을 이동
# for i in range(len(c2)):
#     c2[i] = c2[i] + 15
#     d2[i] = d2[i] + 15
# # 그래프 구하기
# plt.plot(x, y)
# plt.plot(c, d)
# plt.plot(c1, d1)
# plt.plot(c2, d2)
# plt.xlim(-10, 100)
# plt.ylim(-10, 100)
# plt.show()
#
#
# 계단 그래프 만들기
# import random
# position = 0
# walk = [position]
# steps = 5000
# for i in range(steps):
#     step = 1 if random.randint(0,1) else -1
#     position += step
#     walk.append(position)
# plt.plot(walk[:100])
# nsteps = 5000
# draws = np.random.randint(0,2,size=nsteps)
# steps = np.where(draws > 0,1,-1)
# walk = steps.cumsum()
#
# print(walk.min(), walk.max(), sep=' , ')
# print((np.abs(walk) >= 10).argmax())
# plt.show()
#
#
# cx_Oracle 패키지 모듈들을 import
import cx_Oracle as oci
# Oracle 서버와 연결(Connection 맺기)
# conn = oci.connect('hwj', '1234', 'localhost:1521/orcl')
# conn = oci.connect('chk/1234@localhost:1521/orcl')
# Connection 확인
# print(conn.version)
# conn.version
# Oracle DB의 test_member 테이블 검색(select)
# cursor = conn.cursor() # cursor 객체 얻어오기
# cursor.execute('select * from EMP') # SQL 문장 실행
# print(cursor.fetchall())  # 한번에 불러옴
# rows = cursor.fetchall()  # 원하는 순서의 데이터 뽑아오기
# print(rows[3])
# print(cursor.fetchone())  # 하나만 불러옴
# print(cursor.fetchmany())  # 원하는 갯수만큼 불러옴
# for rs in cursor:   # for문 돌려서 하나씩
#     print(rs)
# cursor.close() # cursor 객체 닫기
# Oracle 서버와 연결 끊기
# conn.close
#
#
# import cx_Oracle
# db = cx_Oracle.connect('chk','1234', 'localhost:1521/orcl')
# print('{}'.format(db.version))
# import pandas as pd
# datas = pd.read_sql(sql='select * from EMP', con = db)
# print(datas)
# db.close
#
#데이터 프레임 생성과 csv 파일 생성
# data = pd.DataFrame({'기온':[10,20,30,40],
#                      '강수량':[15,2,35,40]})
# print(data)
# fn = 'out.csv'
# data.to_csv(fn)
#
# fn = '호%d랑%d이' % (10,20)
# print(fn)
#
# fn = '%04d.csv' % (1)
# print(fn)
#
import sys
#
# for i in range(3):
#     fn = 'tiger%04d.csv' % (i)
#     # data.to_csv(fn,sep='|') # 파일 별로 데이터 간에 파이프로 구분
#     data.to_csv(sys.stdout, sep='|')  # 파일 생성하지 않고, 저장 데이터 바로 보여줌
#     print(fn)
#
#
#
# data = pd.DataFrame({'기온':[10, None, 30, 40],  # 데이터 일부 누락
#                      '강수량':[15, 20, 35, 40]})
# print(data)
# fn = 'out.csv'
# data.to_csv(sys.stdout, na_rep='호랑이')  # 누락 데이터를 채우겟다
#
# a = pd.read_csv('out.csv')  # 해당 파일에서 누락으로 수정하면 NaN 출력, 스페이스하면 공백 출력
# print(a)
#
# print(pd.isnull(data))  # 결측값 확인, 트루 출력
# print(data.replace(np.nan, 100))  # 결측 값 입력 혹은 교체
#
#
# print(pd.read_csv('out.csv'))
# f = open('out.csv')
#
# for line in f:
#     print(line)
#
# with open('out.csv') as f:
#     lines = list(f)
#     header, values = line[0], lines[1:]
# print(f)
#
#
# a = [1,2,3]
# b = [[4,5,6]]
# print(a,b)
#
# for i in zip(a,*b):  # *로 전치하여 a,b 짝지어 매칭
#     print(i)
#
#
# obj = """
# {"name": "Wes",
#  "places_lived": ["United States", "Spain", "Germany"],
#  "pet": null,
#  "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
#               {"name": "Katie", "age": 38,
#                "pets": ["Sixes", "Stache", "Cisco"]}]
# } """
#
# import json
# result = json.loads(obj)
# print(result)
#
# # asjson = json.dumps(result)
# # print(result)
#
# siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
# print(siblings)
#
#
# data = pd.read_json('sample.json')
# print(data)
#
# print(data.to_json())
# print(data.to_json(orient='records'))
#
#
# x = pd.ExcelFile('ex1.xlsx')  # 외부 엑셀 파일 불러오기
# a = pd.read_excel(x, 'Sheet1')
# print(a)
#
#
# import requests
#
# url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
# resp = requests.get(url)
# print(resp)
# data = resp.json()
# print(data[0]['title'])   # 403에러
#
#
# 중복 제거
# data = pd.DataFrame({'k1': ['one','two']*3+['two'],
#                      'k2': [1,1,2,3,3,4,4]})
# print(data)
# print(data.duplicated())  # 중복 값을 불리언 시리즈로 반환
# print(data.drop_duplicates())
#
# data['v1'] = range(7)
# print(data.drop_duplicates(['k1']))
# print(data.drop_duplicates(['k1', 'k2'], keep='last'))
#
# data = pd.DataFrame({'food': ['밥','국', '밥',
#                               '면', '옥수수', '보리밥',
#                               '소면', '꿀', '떡'],
#                      '인분': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
# print(data)
#
#
# meat = {
#   'bacon': 'pig',
#   'pulled pork': 'pig',
#   'pastrami': 'cow',
#   'corned beef': 'cow',
#   'honey ham': 'pig',
#   'nova lox': 'salmon'}
#
# l = data['food'].str.lower()
# print(l)
#
#
#
#############################
#
# import json
# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# from collections import defaultdict, Counter
# import seaborn as sns
# usa_path = 'usa.txt'
# records = [json.loads(line) for line in open(usa_path, encoding='UTF8')]
# # records 는 list 타입이고, 원소들은 dict 타입
# # print(records)
# # 'tz' key 값이고 (timezone), 'tz' 가 있는 경우 그 값을 list 에 추가
# # time_zones 는 records 의 모든 dict 에서 'tz' key 에 해당하는 value 를 모아둔 list
# time_zones = [rec['tz'] for rec in records if 'tz' in rec]
# # print(time_zones)
# # time_zones 의 대륙/도시 명을 key 값으로 하고 개수를 그 value 로 한 defaultdict 를 반환
# def get_counts(sequence):  #
#     counts = defaultdict(int)  # values will initialize to 0
#     for x in sequence:
#         counts[x] += 1
#     return counts
# # counts 는 key 값이 대륙/도시, value 가 갯수(count) , time_zones 에서 개수를 셈
# # get_counts 함수에 time_zones 를 인수로 넣어서 중복되는 갯수를 count 하여 defaultdict 을 counts 에 저장
# counts = get_counts(time_zones)
# # print(counts['America/New_York'])
# # print(len(time_zones))
# # 가장 많이 등장하는 상위 10개의 표준 시간대 list 를 리턴하는 함수
# def top_counts(count_dict, n=10):
#     value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
#     # sort() 는 default 가 오름차순 정렬, 내림차순 정렬은 reverse=True 옵션으로 설정
#     value_key_pairs.sort(reverse=True)
#     return value_key_pairs[:n]
# # 대륙/도시 별 count 한 counts 를 인수로 받고 count 수가 많은 순서대로 출력
# # print(top_counts(counts))
# # 위 top_counts 기능을 defaultdict 에서 메소드 지원
# # defaultdict.most_common(x)  상위 x 만큼 출력
# counts = Counter(time_zones)
# # for i in counts.most_common(10):
# #     print(i)
# frame = pd.DataFrame(records)
# # frame 정보 출력
# # print(frame.info())
# # 'tz' co; 의 상위 10개를 출력
# # print(frame['tz'][:10])
# # 'tz' col 에 중복되는 값을 세어줌
# # print(frame['tz'].value_counts())
# # 먼저 col 의 값 중에서 '' 인 것을 'Unkown' 으로 바꾼 후
# clean_tz = frame['tz'].fillna('*Missing*')
# clean_tz[clean_tz == ''] = '*Unknown*'
# # 바꾼 후 .value_counts() 'tz' col 에 중복되는 값을 셈
# tz_counts = clean_tz.value_counts()
# print(tz_counts[:10])
# # figure 가 윈도우 창 생성, figsize 옵션으로 크기 설정
# plt.figure(figsize=(10, 4))
# subset = tz_counts[:10]
# # seaborn.barplot() # 메소드로 plt.figure 에 막대 그래프를 그림
# # y 축은 subset.index 로 대륙/도시 이고, x 축은 count 한 개수
# sns.barplot(y=subset.index, x=subset.values)
# # 창을 생성함
# plt.show()
#
#
#
# data = pd.DataFrame(np.arange(6).reshape((2, 3)),
#                    index=pd.Index(['Ohio', 'Colorado'], name='state'),
#                    columns=pd.Index(['one', 'two', 'three'], name='number'))
# print(data)
# result = data.stack()  # 스택으로 로우로 피벗하여 시리즈 출력
# print(result)
# print(result.unstack())   # 언스택으로 다시 데이터프레임으로 피벗
#
#
#
#
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

plt.plot(np.random.randn(50).cumsum(), 'k--')   # 검정색 점선 그래프
_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)   # 검정색 히스토그램
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))   # 산점도

plt.show()
























