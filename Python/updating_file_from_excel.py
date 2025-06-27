import pandas as pd
import gdown
from datetime import datetime

# Google Drive file ID and output path
file_id = "1RUC1XiQLVptDqG0DHSMYr6kVQz640dQymiKIwSYot7I"
output_xlsx = "sheet_data.xlsx"
log_file = "last_row_log.txt"
url = f"https://drive.google.com/uc?export=download&id={file_id}"

def download_xlsx(link):
    try:
        gdown.download(url, output_xlsx, quiet=True)
        print("Downloaded XLSX successfully.")
    except Exception as e:
        print(f"Download failed: {e}")

start = datetime.now()
end = datetime.now()

while (end-start).total_seconds()/3600 < 2:
    download_xlsx(url)

    with open(log_file, 'a') as file:
        df = pd.read_excel(output_xlsx, engine="openpyxl")
        last_row = df.tail(1).to_string()
        file.write(last_row)
