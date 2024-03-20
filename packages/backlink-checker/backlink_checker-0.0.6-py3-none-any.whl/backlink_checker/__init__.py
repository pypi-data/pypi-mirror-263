from google.oauth2 import service_account
from googleapiclient.discovery import build
import requests
from bs4 import BeautifulSoup
import pandas as pd


class Website:
    def __init__(self, domain_name):
        self.domain_name = domain_name
        self.links = []
    
    def read_google_sheets_links(self, spreadsheet_id, service_account_file, row_range):
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        creds = None
        creds = service_account.Credentials.from_service_account_file(
                service_account_file, scopes=SCOPES)
        SAMPLE_SPREADSHEET_ID = spreadsheet_id
        service = build('sheets','v4',credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId = SAMPLE_SPREADSHEET_ID,range = row_range).execute()
        values = result.get('values',[])
        for val in values:
            if str(val[0]).strip() != "":
                self.links.append(val[0])
    def read_excel_links(self, excel_path, column_name):
        data = pd.read_excel(excel_path)
        for link in data[column_name]:
            self.links.append(link)

        
    
    def print_backlinks(self, backlinks):
        for index, link in enumerate(backlinks):
            print("--------------------")
            print(f"Index: {index}")
            print(f"Target link: {link.target_link}")
            print(f"Backlink: {link.backlink}")
            print(f"Keywords: {link.keywords}")
            print(f"Link rel: {link.link_rel}")
            if index + 1 == len(backlinks):
                print("--------------------")

    def start(self, api_key = None):
        backlinks = []
        
        for index, link in enumerate(self.links):
            if api_key != None:
                response = requests.get(
                    url='https://proxy.scrapeops.io/v1/',
                    params={
                        'api_key': api_key,
                        'url': link, 
                    },
                )
            else:
                response = requests.get(link)

            if response.ok:
                html_content = response.content
                soup = BeautifulSoup(html_content, 'html.parser')

                for backlink in soup.find_all('a'):
                    href = backlink.get('href')
                    rel = backlink.get('rel')
                    keywords = backlink.text

                    if href != None and self.domain_name in href:
                        if rel == None:
                            rel = "follow"
                        else:
                            rel = " ".join(rel)
                        new_backlink = Link(
                            target_link=link,
                            backlink=href,
                            keywords=keywords,
                            link_rel=rel
                        )
                        print("--------------------")
                        print(f"Index: {index}")
                        print(f"Target link: {new_backlink.target_link}")
                        print(f"Backlink: {new_backlink.backlink}")
                        print(f"Keywords: {new_backlink.keywords}")
                        print(f"Link rel: {new_backlink.link_rel}")
                        backlinks.append(new_backlink)

        return backlinks

class Link:
    def __init__(self, backlink, keywords, link_rel, target_link):
        self.target_link = target_link
        self.backlink = backlink
        self.keywords = keywords
        self.link_rel = link_rel
    
