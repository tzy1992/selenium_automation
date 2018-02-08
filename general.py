import unittest
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



class General_Test(object):
	@classmethod
	def chrome(self):
		self.driver = webdriver.Chrome()
		#Maximize window
		options = webdriver.ChromeOptions()
		options.add_argument("--start-maximized")
		self.driver = webdriver.Chrome(chrome_options=options)
		#Go to website
		self.driver.get("https://travelog.com")

	@classmethod
	def mozilla(self):
		self.driver = webdriver.Firefox()
		self.driver.get("https://travelog.com")

	@classmethod
	def IE(self):
		self.driver = webdriver.Ie()
		self.driver.get("https://travelog.com")

	@classmethod
	def facebook_login(self):
		#Click login
		self.driver.find_element_by_xpath('//*[@id="navbar-inverse-document"]/nav/ul[2]/li[1]/p/a[1]').click()
		#Click and login facebook
		self.driver.execute_script("document.querySelector('div.col-md-12.facebookContent.marTop10').click();")
		#email or username
		self.driver.find_element_by_id('email').send_keys('test')
		#password
		self.driver.find_element_by_id('pass').send_keys('test')
		self.driver.find_element_by_id('loginbutton').submit()

	@classmethod
	def product_date_type(self):
		#select any product
		self.driver.find_element_by_class_name('destinations').click()
		self.driver.find_element_by_id('searchCity').click()
		self.driver.find_element_by_xpath('//span[contains(text(),"Kuala Lumpur")]').click()
		self.driver.find_element_by_class_name('productImageLink').click()
		
		#select date
		self.driver.find_element_by_id('bookingDate').click()
		self.driver.find_element_by_class_name('ui-datepicker-days-cell-over').click()
		
		#get date value from calendar datepicker
		self.date = self.driver.find_element_by_id('bookingDate')
		self.date1 = self.date.get_attribute('value')
		print self.date1
		
		#select room type
		Select(self.driver.find_element_by_id('variant1')).select_by_index(1)
		time.sleep(3)
		self.driver.find_element_by_xpath('//*[@id="productBookingDesktop"]/button').submit()
		
		#Select Country
		Select(self.driver.find_element_by_id('country')).select_by_visible_text('Malaysia')
		
		#get date before proceed 
		self.date2 = self.driver.find_element_by_xpath('//*[@id="productCheckout"]/div[1]/div/div[2]/div[1]/p').text
		print self.date2
		
		#get total price before proceed
		self.price = self.driver.find_element_by_id('totalAmountInSpan').text
		print self.price
		return  self.date1, self.date2, self.price;
		
	@classmethod
	def a(self):
		self.chrome()
		self.facebook_login()
		self.product_date_type()

	@classmethod
	def final_date_price(self):
		#get date value final checkout
		self.date3 = self.driver.find_element_by_xpath('//*[@id="mainView"]/div/div[2]/div[3]/div[1]/p').text
		print self.date3
		
		#get total price final checkout
		self.price1 = self.driver.find_element_by_class_name('themeColor').text
		self.price2 = self.price1.replace("RM", "")
		print self.price2	

		return self.date3, self.price2;	

	@classmethod
	def verify(self):
		if self.date1 == self.date2 == self.date3:
			print "date match"
		else:
			print "wrong date"

		if self.price == self.price2:
			print "price match"
		else:
			print "wrong price"

	@classmethod
	def redirect_bank(self):
		#go to bank page
		self.driver.find_element_by_xpath('//*[@id="fpxPayment"]/button').submit()

	@classmethod
	def b(self):
		#submit and go to final checkout page
		self.driver.find_element_by_xpath('//*[@id="personalInformation"]/button').submit()
		self.final_date_price()
		self.verify()
		self.redirect_bank()
		

		
#General_Test.setup()

# if __name__ == '__main__':
    # unittest.main()