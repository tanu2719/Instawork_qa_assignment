from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FlightBooking:
    link_flights_xpath = "(//a[@class='uitk-tab-anchor'])[2]"
    link_roundtrip_xpath = "//span[text()='Roundtrip']"
    inpbox_leaving_from_xpath = "//button[@aria-label='Leaving from']"
    inpbox_going_to_xpath = "//button[@aria-label='Going to']"
    cal_depart_date_box_id = "d1-btn"
    cal_return_date_box_id = "d2-btn"
    cal_depart_date_sel_xpath = "//button[@aria-label='Sep 3, 2021']"
    cal_done_xpath_xpath = "//div[@class='uitk-flex uitk-date-picker-menu-footer']/button"
    cal_return_date_sel_xpath = "//button[@aria-label='Sep 10, 2021']"
    btn_search_xpath = "//button[text()='Search']"
    chkbox_nonstop_xpath = "(//div[@class='uitk-switch uitk-checkbox'])[4]/input"
    drp_highest_price_id = 'listings-sort'
    li_first_flight_xpath = "(//button[@class='uitk-card-link'])[1]"
    btn_continue_xpath = "//button[text()='Continue']"
    ckh_nonstop_aftr_refresh_xpath = "(//div[@class='uitk-switch uitk-checkbox'])[4]/input"
    btn_random_box_xpath = "//div[@class='uitk-flex uitk-flex-gap-three uitk-flex-wrap']/a[2]"
    txt_sf_to_ny_xpath = "(//h2[@class='uitk-heading-4'])[1]"
    txt_ny_to_sf_xpath = "(//h2[@class='uitk-heading-4'])[2]"

    # driver=webdriver.Chrome()
    # driver.switch_to.current_window_handle

    def __init__(self, driver):
        self.driver = driver

    def click_on_flights(self):
        self.driver.find_element_by_xpath(self.link_flights_xpath).click()

    def click_on_roundtrip(self):
        self.driver.find_element_by_xpath(self.link_roundtrip_xpath).click()

    def select_leaving_from(self, cityname):
        btn = self.driver.find_element_by_xpath(self.inpbox_leaving_from_xpath)
        btn.send_keys(cityname)
        action = ActionChains(self.driver)
        action.move_to_element(btn).send_keys(Keys.DOWN).pause(2).send_keys(Keys.ENTER).perform()

    def select_going_to(self, cityname):
        btn = self.driver.find_element_by_xpath(self.inpbox_going_to_xpath)
        btn.send_keys(cityname)
        action = ActionChains(self.driver)
        action.move_to_element(btn).send_keys(Keys.DOWN).pause(2).send_keys(Keys.ENTER).perform()

    def select_departing_date(self):
        self.driver.find_element_by_id(self.cal_depart_date_box_id).click()
        wait = WebDriverWait(self.driver, 10)
        dep_date = wait.until(EC.element_to_be_clickable((By.XPATH, self.cal_depart_date_sel_xpath)))
        self.driver.execute_script("arguments[0].click();", dep_date)
        self.driver.find_element_by_xpath(self.cal_done_xpath_xpath).click()

    def select_return_date(self):
        self.driver.find_element_by_id(self.cal_return_date_box_id).click()
        wait = WebDriverWait(self.driver, 10)
        ret_date = wait.until(EC.element_to_be_clickable((By.XPATH, self.cal_return_date_sel_xpath)))
        self.driver.execute_script("arguments[0].click();", ret_date)
        self.driver.find_element_by_xpath(self.cal_done_xpath_xpath).click()

    def click_on_search_btn(self):
        self.driver.find_element_by_xpath(self.btn_search_xpath).click()

    def click_nonstop_chkbox(self):
        self.driver.find_element_by_xpath(self.chkbox_nonstop_xpath).click()

    def select_highest_price(self):
        drpdwn = self.driver.find_element_by_id(self.drp_highest_price_id)
        sel = Select(drpdwn)
        sel.select_by_value('PRICE_DECREASING')

    def sel_first_flight_frm_table(self):
        wait = WebDriverWait(self.driver, 10)
        select_first_flight = wait.until(EC.visibility_of_element_located((By.XPATH, self.li_first_flight_xpath)))
        self.driver.execute_script("arguments[0].click();", select_first_flight)

    def click_on_continue(self):
        self.driver.find_element_by_xpath(self.btn_continue_xpath).click()

    def click_on_continue_firefox(self):
        ele = self.driver.find_element_by_xpath(self.btn_continue_xpath)
        self.driver.execute_script("arguments[0].click();", ele)
        #self.driver.execute_script("arguments[0].scrollIntoView", ele)
        #ele.click()

    def click_on_nonstop_aftr_refresh(self):
        ns = self.driver.find_element_by_xpath(self.ckh_nonstop_aftr_refresh_xpath)
        self.driver.execute_script("arguments[0].click();", ns)
        self.sel_func = self.select_highest_price()

    def click_on_random_box(self):
        self.driver.find_element_by_xpath(self.btn_random_box_xpath).click()

    def verify_leav_from(self, expected_leave_from):
        flag = False
        wait = WebDriverWait(self.driver, 10)
        self.actual_leaving_from_city = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//button[text()='San Francisco, CA (SFO-San Francisco Intl.)']")))
        self.actual_leaving_from_city = self.driver.find_element_by_xpath(
            "//button[text()='San Francisco, CA (SFO-San Francisco Intl.)']").text
        if expected_leave_from == self.actual_leaving_from_city:
            # print(self.actual_leaving_from_city)
            flag = True
        return flag

    def verify_flying_to(self, expected_going_to):
        flag = False
        wait = WebDriverWait(self.driver, 10)
        self.actual_going_to_city = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='New York (NYC-All Airports)']")))
        self.actual_going_to_city = self.driver.find_element_by_xpath(
            "//button[text()='New York (NYC-All Airports)']").text
        if expected_going_to == self.actual_going_to_city:
            flag = True
        return flag

    def verify_departing_date(self, expected_departing_date):
        flag = False
        self.actual_departing_date = self.driver.find_element_by_xpath(
            "//button[text()='Sep 3']").text
        if expected_departing_date == self.actual_departing_date:
            flag = True
        return flag

    def verify_returning_date(self, expected_returning_date):
        flag = False
        self.actual_returning_date = self.driver.find_element_by_xpath(
            "//button[text()='Sep 10']").text
        if expected_returning_date == self.actual_returning_date:
            flag = True
        return flag

    def verify_departing_flight(self, expected_departing_flight):
        flag = False
        ele = self.driver.find_element_by_xpath(self.txt_sf_to_ny_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView", ele)
        wait = WebDriverWait(self.driver, 10)
        self.actual_departing_flight = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.txt_sf_to_ny_xpath)))
        self.actual_departing_flight = self.driver.find_element_by_xpath(self.txt_sf_to_ny_xpath).text
        print(self.actual_departing_flight)
        if expected_departing_flight == self.actual_departing_flight:
            flag = True
        return flag

    def verify_arrival_flight(self, expected_arrival_flight):
        flag = False
        ele = self.driver.find_element_by_xpath(self.txt_ny_to_sf_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView", ele)
        wait = WebDriverWait(self.driver, 10)
        self.actual_arrival_flight = wait.until(EC.visibility_of_element_located(
            (By.XPATH, self.txt_ny_to_sf_xpath)))
        self.actual_arrival_flight = self.driver.find_element_by_xpath(self.txt_ny_to_sf_xpath).text
        print(self.actual_arrival_flight)
        if expected_arrival_flight == self.actual_arrival_flight:
            flag = True
        return flag
