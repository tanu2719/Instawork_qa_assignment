import pytest
from pageObject.FightBooking import FlightBooking


class Test001_FlightBooking:
    url = "https://www.orbitz.com/"
    leaving_from_city = 'San Francisco'
    flying_to_city = 'New York'
    expected_leave_from = "San Francisco, CA (SFO-San Francisco Intl.)"

    def test_flight_booking(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.fb = FlightBooking(self.driver)
        self.fb.click_on_flights()
        self.fb.click_on_roundtrip()
        self.fb.select_leaving_from(self.leaving_from_city)
        self.fb.select_going_to(self.flying_to_city)
        self.fb.select_departing_date()
        self.fb.select_return_date()
        self.fb.click_on_search_btn()
        # self.driver.implicitly_wait(20)
        status_leavingfm = self.fb.verify_leav_from("San Francisco, CA (SFO-San Francisco Intl.)")
        assert True == status_leavingfm
        self.driver.save_screenshot("E:\\Instawork\\Screenshots\\verify_departure_city.png")
        status_goingto = self.fb.verify_flying_to("New York (NYC-All Airports)")
        assert True == status_goingto
        status_departing_date = self.fb.verify_departing_date("Sep 3")
        assert True == status_departing_date
        status_returning_date = self.fb.verify_returning_date("Sep 10")
        assert True == status_returning_date
        self.driver.save_screenshot("E:\\Instawork\\Screenshots\\verify_all_details.png")
        self.driver.implicitly_wait(20)
        self.fb.click_nonstop_chkbox()
        self.fb.select_highest_price()
        self.fb.sel_first_flight_frm_table()
        # self.fb.click_on_continue()
        self.fb.click_on_continue_firefox()
        self.driver.implicitly_wait(6)
        self.fb.click_on_nonstop_aftr_refresh()
        self.fb.sel_first_flight_frm_table()
        # self.fb.click_on_continue()
        self.fb.click_on_continue_firefox()
        self.fb.click_on_random_box()
        chkout_window = self.driver.window_handles[1]
        print(chkout_window)
        self.driver.switch_to.window(chkout_window)
        # wh_bef=self.driver.window_handles[0]
        # self.driver.switch_to.window(wh_bef)
        status_departing_flight = self.fb.verify_departing_flight("San Francisco to New York")
        assert True == status_departing_flight
        status_arrival_flight = self.fb.verify_arrival_flight("New York to San Francisco")
        # print(status_departing_flight)
        assert True == status_arrival_flight
        self.driver.quit()
