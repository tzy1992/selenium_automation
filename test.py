import unittest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from general import General_Test




class fb_login(General_Test, unittest.TestCase):
	

	@classmethod	
	def maybank(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('Maybank2U')
		self.b()
		
		#verify maybank page
		self.driver.find_element_by_xpath('//*[@id="login"]/div[1]/div/div/div/img')
		self.driver.find_element_by_xpath('//*[@id="loginTable"]/tbody/tr/td')
		self.driver.find_element_by_xpath('//*[@id="login"]/div[1]/div/div/div/input')

		self.driver.quit()

	@classmethod
	def public_bank(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('Public Bank Berhad')
		self.b()

		#verify public bank page
		self.driver.switch_to.frame('new-ebank-container')
		self.driver.find_element_by_id('ebanking-logo')
		self.driver.switch_to.frame('iframe1')
		self.driver.find_element_by_xpath('//*[@id="LoginId"]/div[1]/div')
		self.driver.find_element_by_id('NextBtn')

		self.driver.quit()

	@classmethod
	def cimb(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('CIMB Clicks')
		self.b()
		#verify cimb page
		self.driver.find_element_by_xpath('//*[@id="rev-login"]/div[1]/form/div/div[1]')
		self.driver.find_element_by_id('userId')
		self.driver.find_element_by_id('submit')

		self.driver.quit()

	@classmethod
	def hong_leong(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('Hong Leong Bank')
		self.b()

		#verify hong leong bank page
		self.driver.find_element_by_xpath('//*[@id="logonForm"]/table[1]/tbody/tr/td/table/tbody/tr[1]/td/img')
		self.driver.find_element_by_id('txt')
		self.driver.find_element_by_id('showNext')

		self.driver.quit()

	@classmethod
	def standard_chartered(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('Standard Chartered')
		self.b()

		#verify standard chartered bank page
		self.driver.find_element_by_xpath('//*[@id="page-login"]/div[1]')
		self.driver.find_element_by_id('userName')
		self.driver.find_element_by_id('next-btn')

		self.driver.quit()


	@classmethod
	def rhb(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('RHB Bank')
		self.b()

		#verify rhb bank page
		self.driver.find_element_by_xpath('/html/body/div[1]')
		self.driver.find_element_by_id('txtAccessCode')
		self.driver.find_element_by_id('cmdLogin')

		self.driver.quit()

	@classmethod
	def alliance(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('Alliance Bank')
		self.b()

		#verify alliance bank page
		self.driver.find_element_by_xpath('//*[@id="header"]')
		self.driver.find_element_by_id('username')
		self.driver.find_element_by_id('step2')
	    	
		self.driver.quit()

	@classmethod
	def affin_bank(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('Affin Bank')
		self.b()

		#verify affin bank page
		self.driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td[1]/div')
		self.driver.find_element_by_name('userName')
		self.driver.find_element_by_xpath('/html/body/form/table/tbody/tr[10]/td[3]/input')

		self.driver.quit()

	@classmethod
	def am_bank(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('AmBank')
		self.b()

		#verify am bank page
		self.driver.find_element_by_xpath('//*[@id="ambankgroup_logo"]')
		self.driver.find_element_by_id('ctlSignon_txtUserID')
		self.driver.find_element_by_id('ctlSignon_btnContinue')

		self.driver.quit()


	@classmethod
	def bank_islam(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('Bank Islam')
		self.b()

		#verify bank islam page
		self.driver.find_element_by_xpath('//*[@id="login-header"]/img')
		self.driver.find_element_by_id('username')
		self.driver.find_element_by_xpath('//*[@id="usernameForm"]/div[2]/input')

		self.driver.quit()


	@classmethod
	def maybank2e(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('Maybank2E')
		self.b()

		#verify maybank2e page
		self.driver.find_element_by_xpath('//*[@id="header"]/div')
		self.driver.switch_to.frame('frame_7_8_content')
		self.driver.find_element_by_id('property1')
		self.driver.find_element_by_id('ui_button_a_login_btn')

		self.driver.quit()


	@classmethod
	def bank_rakyat(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('Bank Rakyat')
		self.b()

		#verify bank rakyat page
		wait = WebDriverWait(self.driver, 10)
		frame = wait.until(EC.presence_of_element_located((By.ID, "fpxFrame")))
		self.driver.switch_to.frame(frame)
		#self.driver.switch_to.frame('fpxFrame')
		self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/img')
		self.driver.find_element_by_id('username')
		self.driver.find_element_by_id('doSubmit')

		self.driver.quit()



	@classmethod
	def bank_muamalat(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('Bank Muamalat')
		self.b()

		#verify bank muamalat page
		self.driver.find_element_by_xpath('//*[@id="container"]/table/tbody/tr[1]/td[1]/img')
		self.driver.find_element_by_xpath('//*[@id="table-login"]/tbody/tr[4]/td[1]/div/input')
		self.driver.find_element_by_id('btn-login')

		self.driver.quit()

	@classmethod
	def kfh(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('KFH')
		self.b()

		#verify kfh page
		self.driver.switch_to_frame(self.driver.find_element_by_tag_name("frame"))
		self.driver.find_element_by_xpath('//*[@id="topimg2"]')
		self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/input[1]')
		self.driver.find_element_by_xpath('//*[@id="mainContent"]/div[2]/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/input[1]')

		self.driver.quit()

	@classmethod
	def ocbc(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('OCBC Bank')
		self.b()

		#verify ocbc page
		self.driver.find_element_by_id('branding')
		self.driver.find_element_by_id('access-code')
		self.driver.find_element_by_id('cmdLogin')

		self.driver.quit()

	@classmethod
	def uob(self):
		self.a()
		Select(self.driver.find_element_by_id('fpxBankList')).select_by_visible_text('UOB Bank')
		self.b()

		#verify uob page
		self.driver.find_element_by_xpath('/html/body/form[2]/table[2]/tbody/tr[3]/td/table/tbody/tr[1]/td')
		self.driver.find_element_by_id('textfield2')
		self.driver.find_element_by_name('submit')

		self.driver.quit()

	@classmethod
	def visa_card(self):
		self.a()
		self.driver.find_element_by_css_selector("input[type='radio'][value='visacard']").click()
		self.driver.find_element_by_xpath('//*[@id="personalInformation"]/button').submit()
		self.driver.find_element_by_xpath('//*[@id="f"]/button').submit()
		
		#verify visa card page
		self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div[1]')
		self.driver.find_element_by_id('ipan')
		self.driver.find_element_by_id('payBtn')

		self.driver.quit()

	@classmethod
	def master_card(self):
		self.a()
		self.driver.find_element_by_css_selector("input[type='radio'][value='mastercard']").click()
		self.driver.find_element_by_xpath('//*[@id="personalInformation"]/button').submit()
		self.driver.find_element_by_xpath('//*[@id="f"]/button').submit()
		
		#verify master card page
		self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div[1]')
		self.driver.find_element_by_id('ipan')
		self.driver.find_element_by_id('payBtn')

		self.driver.quit()

	@classmethod
	def bank_transfer(self):
		self.a()
		self.driver.find_element_by_css_selector("input[type='radio'][value='BankTransfer']").click()
		self.driver.find_element_by_xpath('//*[@id="personalInformation"]/button').submit()
			
		#verify bank transfer page
		self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div[1]')
		self.driver.find_element_by_id('ipan')
		self.driver.find_element_by_id('payBtn')

		self.driver.quit()

fb_login.public_bank()

		
