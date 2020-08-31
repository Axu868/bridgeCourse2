from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_if_button_is_clickable(self):
        self.browser.get('http://localhost:8000')
        time.sleep(2)
        button1 = self.browser.find_element_by_id("pd2")
        button2 = self.browser.find_element_by_id("pp2")
        button3 = self.browser.find_element_by_id("we2")
        button4 = self.browser.find_element_by_id("e2")
        button4 = self.browser.find_element_by_id("i2")
        button5 = self.browser.find_element_by_id("r2")
        href_data1 =button1.get_attribute('href')
        href_data2 =button2.get_attribute('href')
        href_data3 =button3.get_attribute('href')
        href_data4 =button4.get_attribute('href')
        href_data5 =button5.get_attribute('href')
        if href_data1 is None:
            button1.is_clickable = False
        if href_data2 is None:
            button2.is_clickable = False
        if href_data3 is None:
            button3.is_clickable = False
        if href_data4 is None:
            button4.is_clickable = False
        if href_data5 is None:
            button5.is_clickable = False
            
        
    def test_if_button_edit_works(self):
        self.browser.get('http://localhost:8000')
        time.sleep(2)
        # check the title
        self.assertIn('Adriana Ungureanu',self.browser.title)
        # check the first heading
        header_main_text= self.browser.find_element_by_id("header_main").text
        self.assertIn('Adriana Ungureanu', header_main_text)

        # check the rest of the headings
        header1 = self.browser.find_element_by_id("pd").text
        header2 = self.browser.find_element_by_id("pp").text
        header3 = self.browser.find_element_by_id("we").text
        header4 = self.browser.find_element_by_id("e").text
        header5 = self.browser.find_element_by_id("i").text
        header6 = self.browser.find_element_by_id("r").text
        self.assertIn('Personal details', header1)
        self.assertIn('Personal Profile', header2)
        self.assertIn('Work Experience', header3)
        self.assertIn('Education', header4)
        self.assertIn('Interests', header5)
        self.assertIn('References', header6)

        formPD= self.browser.find_element_by_id("form_pd") 
        formPP= self.browser.find_element_by_id("form_pp") 
        formWE= self.browser.find_element_by_id("form_we") 
        formE= self.browser.find_element_by_id("form_e") 
        formI= self.browser.find_element_by_id("form_i")
        formR= self.browser.find_element_by_id("form_r")  
        buttonE1= self.browser.find_element_by_id("button1")
        buttonS1= self.browser.find_element_by_id("save1")
        buttonE1.click()
        self.assertEqual(buttonS1.value_of_css_property('display'), "block")
        self.assertEqual(formPD.value_of_css_property('display'),"block")

        buttonE2= self.browser.find_element_by_id("button2")
        buttonS2= self.browser.find_element_by_id("save2")
        buttonE2.click()
        self.assertEqual(buttonS2.value_of_css_property('display'), "block")
        self.assertEqual(formPP.value_of_css_property('display'),"block")

        buttonE3= self.browser.find_element_by_id("button3")
        buttonS3= self.browser.find_element_by_id("save3")
        buttonE3.click()
        self.assertEqual(buttonS3.value_of_css_property('display'), "block")
        self.assertEqual(formWE.value_of_css_property('display'),"block")

        buttonE4= self.browser.find_element_by_id("button4")
        buttonS4= self.browser.find_element_by_id("save4")
        buttonE4.click()
        self.assertEqual(buttonS4.value_of_css_property('display'), "block")
        self.assertEqual(formE.value_of_css_property('display'),"block")

        buttonE5= self.browser.find_element_by_id("button5")
        buttonS5= self.browser.find_element_by_id("save5")
        buttonE5.click()
        self.assertEqual(buttonS5.value_of_css_property('display'), "block")
        self.assertEqual(formI.value_of_css_property('display'),"block")

        buttonE6= self.browser.find_element_by_id("button6")
        buttonS6= self.browser.find_element_by_id("save6")
        buttonE6.click()
        self.assertEqual(buttonS6.value_of_css_property('display'), "block")
        self.assertEqual(formR.value_of_css_property('display'),"block")

        # input_name_pd = self.browser.find_element_by_id("name_pd")
        # input_email_pd = self.browser.find_element_by_id("email_pd")
        # input_phone_pd = self.browser.find_element_by_id("phone_pd")
        # input_address_pd = self.browser.find_element_by_id("adress_pd")
        # self.assertEqual(input_name_pd.get_attribute('placehold'),"Alex")
        # self.assertEqual(input_email_pd.get_attribute('placehold'),'alex@gmail.com')
        # self.assertEqual(input_phone_pd.get_attribute('placehold'),'0712345678')
        # self.assertEqual(input_address_pd.get_attribute('placehold'),'28 Hubert Road')


        

        # buttonE = self.browser.find_element_by_id("button1")
        # buttonS = self.browser.find_element_by_id("save_pd")
        # formPP = self.browser.find_element_by_id("form_pd") 
        # buttonE.click()
        # self.assertEqual(buttonS.value_of_css_property('display'), "block")
        # self.assertEqual(formPP.value_of_css_property('display'),"block")

        # buttonS.click()
        # self.assertEqual(buttonS.value_of_css_property('display'),"none")
        
    # def check_edit_buttons_if_they_work(self):
    #     self.browser.get('http://localhost:8000')
    #     time.sleep(2)
    #     formPD= self.browser.find_element_by_id("form_pd") 
    #     formPP= self.browser.find_element_by_id("form_pp") 
    #     formWE= self.browser.find_element_by_id("form_we") 
    #     formE= self.browser.find_element_by_id("form_e") 
    #     formI= self.browser.find_element_by_id("form_i")
    #     formR= self.browser.find_element_by_id("form_r")  
    #     buttonE1= self.browser.find_element_by_id("button1")
    #     buttonS1= self.browser.find_element_by_id("save1")
    #     buttonE1.click()
    #     self.assertEqual(buttonS1.value_of_css_property('display'), "block")
    #     self.assertEqual(formPD.value_of_css_property('display'),"block")

    #     buttonE2= self.browser.find_element_by_id("button2")
    #     buttonS2= self.browser.find_element_by_id("save2")
    #     buttonE2.click()
    #     self.assertEqual(buttonS2.value_of_css_property('display'), "block")
    #     self.assertEqual(formPP.value_of_css_property('display'),"block")

    #     buttonE3= self.browser.find_element_by_id("button3")
    #     buttonS3= self.browser.find_element_by_id("save3")
    #     buttonE3.click()
    #     self.assertEqual(buttonS3.value_of_css_property('display'), "block")
    #     self.assertEqual(formWE.value_of_css_property('display'),"block")

    #     buttonE4= self.browser.find_element_by_id("button4")
    #     buttonS4= self.browser.find_element_by_id("save4")
    #     buttonE4.click()
    #     self.assertEqual(buttonS4.value_of_css_property('display'), "block")
    #     self.assertEqual(formE.value_of_css_property('display'),"block")

    #     buttonE5= self.browser.find_element_by_id("button5")
    #     buttonS5= self.browser.find_element_by_id("save5")
    #     buttonE5.click()
    #     self.assertEqual(buttonS5.value_of_css_property('display'), "block")
    #     self.assertEqual(formI.value_of_css_property('display'),"block")

    #     buttonE6= self.browser.find_element_by_id("button6")
    #     buttonS6= self.browser.find_element_by_id("save6")
    #     buttonE6.click()
    #     self.assertEqual(buttonS6.value_of_css_property('display'), "block")
    #     self.assertEqual(formR.value_of_css_property('display'),"block")

    # def check_form_input(self):
    #     self.browser.get('http://localhost:8000')
    #     time.sleep(2)
    #     input_name_pd = self.browser.find_element_by_id("name_pd")
    #     input_email_pd = self.browser.find_element_by_id("email_pd")
    #     input_phone_pd = self.browser.find_element_by_id("phone_pd")
    #     input_address_pd = self.browser.find_element_by_id("adress_pd")
    #     self.assertEqual(input_name_pd.get_attribute('placehold'),'Alex')
    #     self.assertEqual(input_email_pd.get_attribute('placehold'),'alex@gmail.com')
    #     self.assertEqual(input_phone_pd.get_attribute('placehold'),'0712345678')
    #     self.assertEqual(input_address_pd.get_attribute('placehold'),'28 Hubert Road')



        




    
        

    


    # def check_for_row_in_list_table(self,row_text):
    #     table = self.browser.find_element_by_id('id_list_table')
    #     rows = table.find_elements_by_tag_name('tr')
    #     self.assertIn(row_text, [row.text for row in rows])

    # def test_can_start_a_list_and_retrieve_it_later(self):


    #     # Edith has heard about a cool new online to-do app. She goes
    #     # to check out its homepage
    #     self.browser.get('http://localhost:8000')

    #     # She notices the page title and header mention to-do lists
    #     self.assertIn('To-Do', self.browser.title)
    #     header_text = self.browser.find_element_by_tag_name('h1').text  
    #     self.assertIn('To-Do', header_text)

    #     # She is invited to enter a to-do item straight away
    #     inputbox = self.browser.find_element_by_id('id_new_item')  
    #     self.assertEqual(
    #         inputbox.get_attribute('placeholder'),
    #         'Enter a to-do item'
    #     )

    #     # She types "Buy peacock feathers" into a text box (Edith's hobby
    #     # is tying fly-fishing lures)
    #     inputbox.send_keys('Buy peacock feathers')  

    #     # When she hits enter, the page updates, and now the page lists
    #     # "1: Buy peacock feathers" as an item in a to-do list table
    #     inputbox.send_keys(Keys.ENTER)  
    #     time.sleep(1)
    #     self.check_for_row_in_list_table('1: Buy peacock feathers')

    #     # There is still a text box inviting her to add another item. She
    #     # enters "Use peacock feathers to make a fly" (Edith is very
    #     # methodical)
    #     inputbox = self.browser.find_element_by_id('id_new_item')
    #     inputbox.send_keys('Use peacock feathers to make a fly')
    #     inputbox.send_keys(Keys.ENTER)
    #     time.sleep(1)

    #     self.check_for_row_in_list_table('1: Buy peacock feathers')
    #     self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')


    #     self.fail('Finish the test!')
if __name__ == '__main__':  
    unittest.main(warnings='ignore') 