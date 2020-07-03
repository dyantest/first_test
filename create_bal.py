# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
import subprocess, datetime, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""
1. 발주그룹등록
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
driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[1]/fieldset/div/div/input').send_keys('DY0000000137')
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

driver.close()