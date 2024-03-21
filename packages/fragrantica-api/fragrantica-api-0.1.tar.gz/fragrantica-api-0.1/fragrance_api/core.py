import requests
import json
from bs4 import BeautifulSoup
import random
import time

class FragranticaAPI:
    def __init__(self):
        self.user_agent = self.get_fake_user_agent()
    
    
    def get_csrf_token(self, url, headers):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            csrf_input = soup.find("input", {"type": "hidden", "name": "csrf_token"})
            if csrf_input:
                csrf_token = csrf_input["value"]
                return csrf_token
            else:
                return None
        except requests.RequestException as e:
            print("Failed to retrieve CSRF token:", e)
            return None

    def get_fake_user_agent(self):
        response = requests.get("http://headers.scrapeops.io/v1/user-agents?api_key=5c0e5bea-5392-430d-924e-47aa1d0f4a76&num_results=100")
        json_response = response.json()
        user_agent_list = json_response.get('result', [])
        user_agent = random.choice(user_agent_list)
        return user_agent

    def fetch_fragrances(self, fragrance, limit):
        url = "https://fgvi612dfz-dsn.algolia.net/1/indexes/*/queries"
        
        apiheaders = {
            "x-algolia-api-key": "NjlhYThlMDRmN2UzNDUyODhiMzRkOTY0OTc2MTgyNzM0NGJhZWRkOGE3MjhkODRmZTkyYTkyN2IzYmMzYTAwY3ZhbGlkVW50aWw9MTcxMTc2MjIwMA==",
            "x-algolia-application-id": "FGVI612DFZ",
        }   

        payload = {
            "requests":[
                {"indexName":"fragrantica_perfumes","query":f"{fragrance}","params":f"hitsPerPage={limit}"},
            ]
        }

        response = requests.post(url, headers=apiheaders, data=json.dumps(payload))
        if response.status_code == 200:
            data = response.json()
            result_json = []
            for hit in data["results"][0]["hits"]:
                fragrance_info = {
                    "Thumbnail": hit["thumbnail"],
                    "Brand/Designer": hit["dizajner"],
                    "Perfume Name": hit["naslov"],
                    "Collection": hit["collection"],
                    "Gender": hit["spol"],
                    "Year": hit["godina"],
                    "Rating": hit["rating"],
                    "English URL": hit["url"]["EN"][0]
                }
                result_json.append(fragrance_info)
            return json.dumps(result_json, indent=2)
        else:
            print("Error:", response.status_code)
            return None
    
    def fetch_fragrance_accords(self, fragrance):
        userheader = {
            "User-Agent": self.user_agent
        }
        print(f'user agent: {self.user_agent}')
        
        try:
            fragrances_data_json = self.fetch_fragrances(fragrance, 1)  
            if fragrances_data_json:
                fragrances_data = json.loads(fragrances_data_json)  
                fragrance_url = fragrances_data[0]["English URL"]
                response = requests.get(fragrance_url, headers=userheader)
                response.raise_for_status()  
                soup = BeautifulSoup(response.text, 'html.parser')
                main_accord_rows = soup.find_all(class_="cell accord-box")
                accords = {}
                for main_accord_row in main_accord_rows:
                    main_accord_div = main_accord_row.find(class_="accord-bar")
                    if main_accord_div:
                        width_style = main_accord_div.get('style')
                        if width_style:
                            width_start_index = width_style.find('width:') + len('width:')
                            width_end_index = width_style.find('%', width_start_index)
                            width_value = width_style[width_start_index:width_end_index].strip()
                            main_accord = main_accord_div.text.strip()
                            accords[main_accord] = f"{width_value}%"
                        else:
                            accords[main_accord] = "N/A"
                    else:
                        accords["accord-bar div not found"] = "N/A"
                
                return json.dumps({"accords": accords}, indent=2) 
            else:
                return None
        except requests.exceptions.RequestException as e:
            print("Error fetching fragrance accords:", e)
            return None

    def login(self, username, password):
        login_url = "https://www.fragrantica.com/board/login.php"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        }

        csrf_token = self.get_csrf_token(login_url, headers)  
        if not csrf_token:
            print("CSRF token not found. Exiting.")
            return

        payload = {
            "form_sent": "1",
            "redirect_url": login_url,
            "csrf_token": csrf_token,
            "req_username": username,
            "req_password": password,
            "save_pass": "1",
            "login": "Login"
        }
        try:
            session = requests.Session()
            response = session.post(login_url, data=payload, headers=headers)
            response.raise_for_status()
            if response.status_code == 200 and "Logged in successfully" in response.text:
                for i in range(3):
                    print("Logging in...")
                    time.sleep(i)
                print(f"Logged in as {username}")
            else:
                print("Login failed. Username/Password is Incorrect.")
        except requests.RequestException as e:
            print("Login failed:", e)