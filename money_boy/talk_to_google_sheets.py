import gspread


class TalkToGoogleSheets:

    def __init__(self):
        self.gc = gspread.service_account(filename="money_boy/sheets-creds.json")
        self.sheet = self.gc.open("Finance_Wiz").sheet1

    def get_all_data(self):
        return self.sheet.get_all_records()
