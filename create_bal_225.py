# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import subprocess, datetime, time, timeit
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""
1. 발주그룹등록 (220_AT0000000004)
2. 발주그룹 내 발주등록
3. 공급사에서 발주확정

"""

# 테스트서버 입력
eSCM_server = '02'
RMS_server = '01'
# rms_web_id = 'qa_auto_test'
# rms_web_pw = 'kurlyqa123!'
driver = webdriver.Chrome('/Users/tf-mac-065/PycharmProjects/autotest/chromedriver')
driver.implicitly_wait(10)
now = datetime.datetime.today()
start = time.time()  # 시작 시간 저장

print()
print('테스트 시작시간 ▼')
print(now)

# 1.
# 발주그룹 등록
# eSCM md 로그인
driver.get('https://front' + eSCM_server + '.escm.dev.kurly.com/#/stafflogin')
# 아이디 입력란을 찾은 후, 아이디를 입력함
driver.find_element_by_id('inputEmail').send_keys('qa_md4@kurlycorp.com')
# 비밀번호 입력란을 찾은 후, 비밀번호를 입력함
driver.find_element_by_id('inputPassword').send_keys('1234512345q#')
# 로그인 버튼을 찾은 후, 클릭
driver.find_element_by_xpath('/html/body/div/form/div/button[1]').click()
time.sleep(1)
# 발주관리 메뉴 이동
driver.find_element_by_partial_link_text('발주관리').click()
time.sleep(1)
# 상품코드 검색
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys('AT0000000004')
time.sleep(1)
# 검색버튼 클릭
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/button[1]').click()
time.sleep(2)
# 검색결과 체크박스 선택
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr/td[1]/div').click()
# 발주그룹 생성 버튼 클릭
driver.find_element_by_id('viewPurchaseOrder').click()
time.sleep(1)
# 발주그룹 생성 상세페이지 접근
# 수량 입력
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[3]/div[1]/div/table/tbody/tr[2]/td[8]/input').send_keys('100')
# 긴급발주 설정 후 생성
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[3]/div[1]/div/table/tbody/tr[2]/td[10]/select')).select_by_visible_text('긴급발주')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/button[1]').click()
# 발주서 등록완료 팝업 닫기
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'modal-content')))
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/header/button').click()
time.sleep(4)

# 2.
# 발주서그룹에서 발주등록
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div/div[2]/div/ul/li[3]/a/span').click()
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr[1]/td[10]/button').click()
time.sleep(1)

driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[3]/div[3]/div[2]/button[1]').click()

# 발주서 등록완료 팝업 닫기
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'modal-content')))
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/header/button').click()
time.sleep(4)

# 로그아웃
driver.find_element_by_xpath('/html/body/div/div[1]/nav/div/ul[2]/li[3]/a').click()

time.sleep(2)

# 공급사 계정으로 발주확정 하기
driver.get('https://front' + eSCM_server + '.escm.dev.kurly.com/#/login')
driver.find_element_by_id('inputEmail').send_keys('VD3658.01')
driver.find_element_by_id('inputPassword').send_keys('1234512345q!')
driver.find_element_by_xpath('//*[@id="app"]/form/div/button').click()
time.sleep(1)
driver.find_element_by_partial_link_text('발주관리').click()
time.sleep(1)
# 상품코드 검색
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/select')).select_by_visible_text('상품코드')
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys('AT0000000004')
Select(driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div[1]/fieldset/div/select')).select_by_visible_text('발주생성')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/div[4]/fieldset/div/button[1]').click()
time.sleep(2)

# 상세 버튼 클릭하여 발주 상세 페이지 접근
driver.find_element_by_xpath(
    '/html/body/div/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr[1]/td[14]/button').click()
time.sleep(1)
# 유통기한 입력 후 확정처리
driver.find_element_by_xpath(
    '/html/body/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr/td[14]/div[2]/div[1]/input').send_keys(
    '2030/12/31')
time.sleep(1)
# 확인 창 닫기
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button').click()
time.sleep(2)
# 동의 체크박스 설정
# 체크박스 오류가 자주 발생하여 페이지 하단으로 스크롤 후, 체크
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element_by_xpath(
    '/html/body/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div[2]/div[2]/fieldset/div/div').click()
time.sleep(1)
# 발주확정
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[5]/div[2]/button[1]').click()
time.sleep(1)
# 확인 팝업창
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/footer/div/button[1]').click()
time.sleep(5)
# 발주관리 메뉴로 이동
driver.find_element_by_xpath('/html/body/div/div[1]/nav/div/ul[1]/li[3]/a').click()
time.sleep(2)
# 발주확정 된 발주코드 가져오기
Pom = driver.find_element_by_xpath(
    '/html/body/div/div[1]/div/div[2]/div/div[2]/div[5]/div/div/table/tbody/tr[1]/td[2]').text

print('* eSCM > 발주서 생성 결과 : Pass / ' + Pom)

driver.close()

print("%f초 걸렸습니다." % (time.time() - start))