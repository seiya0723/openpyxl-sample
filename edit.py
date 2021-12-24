import openpyxl as px
import datetime

#編集対象のファイルを読み込み
wb  = px.load_workbook('salary.xlsx')

#アクティブシートを選択(新規作成時に最初からあるシート)
#ws  = wb.active
ws  = wb.worksheets[0]

ws["C2"].value  = "テスト"


#別名で保存
today   = str(datetime.date.today())

wb.save("salary" + today + ".xlsx")

