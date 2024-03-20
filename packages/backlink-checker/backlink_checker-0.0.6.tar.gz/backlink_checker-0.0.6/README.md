Backlink Checker
-----------------
USAGE:
# Example for local excel file
```
from backlink_checker import Website
web = Website(domain_name="example.com")
web.read_excel_links(excel_path="example.xlsx", column_name="Links")
backlinks = web.start()
```
# Example for google sheets
```
from backlink_checker import Website
web = Website(domain_name="example.com")
web.read_google_sheets_links(
    spreadsheet_id="1DY57Dq5yMD_Tb6DtI5_FqyIPRN1QMzQ9VtW3XKvnnhE",
    service_account_file="keys.json",
    row_range="Sheet1!A2:A"
)
backlinks = web.start()
```
```
# Acess backlinks details
for b in backlinks:
    print(b.target_link)
    print(b.backlink)
    print(b.keywords)
    print(b.link_rel)
```

# Install using pypi:
```
pip install backlink-checker
```
