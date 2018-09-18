# ここにAPI_KEYを設定してください。
API_KEY = ''
SPREADSHEET_ID = '11BCnspCt2Mut3nhc4WMY6CYTd0zF9C3eCzsk1AEpKLM'
RANGE = 'sales!A1:E6'
DATA = 'https://sheets.googleapis.com/v4/spreadsheets/' + SPREADSHEET_ID + '/values/' + RANGE + '?key=' + API_KEY
print(DATA)
