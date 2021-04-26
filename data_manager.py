import gspread
import os
from dotenv import load_dotenv

load_dotenv("C:/Users/Yehya Ahmed/OneDrive/Documents/env.txt")

google_sheet_url = os.getenv("google_sheet_url")


class DataManager:
    def __init__(self):
        self.sheet_data = None

    def get_sheet_data(self):
        # Returns the current sheet data
        gc = gspread.service_account(filename='creds.json')
        self.gsheet = gc.open_by_url(google_sheet_url)

        return self.gsheet.sheet1.get_all_values()

    def update_iatacode(self):
        # Update the google sheet with the IATA code
        counter = 1
        for values in self.sheet_data:
            self.gsheet.sheet1.update_cell(counter, 2, values[1])
            counter += 1
