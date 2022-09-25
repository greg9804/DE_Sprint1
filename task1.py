# 1. Необходимо спарсить данные о вакансиях python разработчиков с сайта hh.ru,
# введя в поиск “python разработчик” и указав, что мы рассматриваем все регионы.
# Необходимо спарсить:
#
# Название вакансии
# Требуемый опыт работы
# Заработную плату
# Регион
# И сохранить эти данные в формате json в следующем виде:
# {"data" : [
#   {
#       "title" : "",
#       "work experience" : "",
#       "salary" : "",
#       "region" : ""
#   },
#   {"...", "..."}
# ]}
import requests
import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import json
import tqdm

data = {
    "data": []
}

url = "https://hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&area=113&page=0&hhtmFrom=vacancy_search_list"
response = req.get(url, headers={'User-Agent': UserAgent().google})

for key, value in response.request.headers.items():
    print(key+": "+value)

with open('newfile.html', 'w', encoding="utf-8") as f:
    f.writelines(response.text)

soup = BeautifulSoup(response.text, "lxml")
tag_pager_spans = soup.find("div", {"class": "pager"}).findAll("span", {"class" : "pager-item-not-in-short-range"})
pages = [i for i in range(0, int(tag_pager_spans[-1].text))]
links_vacancies = []

def get_links():
    #getting all links vacancies
    print('Собираем ссылки...')
    for p in tqdm.tqdm(pages):
        base_url = f'https://hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&area=113&page={p}&hhtmFrom=vacancy_search_list'
        try:
            res = requests.get(base_url, headers={'User-Agent': UserAgent().random})
            soup = BeautifulSoup(res.text, "lxml")
            links = soup.find_all("a", {"class": "serp-item__title"}, href=True)
            for link in links:
                links_vacancies.append(link['href'])
            time.sleep(0.1)
        except Exception as e:
            print(f"{e}")

def get_data():
    #getting data from links
    print('Обрабатываем ссылки...')
    for link in tqdm.tqdm(links_vacancies):
        try:
            res = requests.get(link, headers={'User-Agent': UserAgent().random})
            soup = BeautifulSoup(res.text, "lxml")
            title = soup.find('h1', attrs={'data-qa': 'vacancy-title'}).text
            exp = soup.find('span', attrs={'data-qa': 'vacancy-experience'}).text
            salary = soup.find('div', attrs={'data-qa': 'vacancy-salary'}).text
            region = soup.find('p', attrs={'data-qa': 'vacancy-view-location'})
            if (region == None):
                region = soup.find('a', attrs={'data-qa': 'vacancy-view-link-location'}).text
            else:
                region = region.text
            data["data"].append({"title": title, "work experience": exp, "salary": salary, "region": region})
            time.sleep(0.1)
        except Exception as e:
            print(f"{e}")
            data["data"].append({"title": 'none', "work experience": 'exp', "salary": '0', "region": 'region'})

def write_to_json():
    #to json
    with open("data.json", 'w', encoding='cp1251') as file:
        json.dump(data, file, ensure_ascii=False)

def main():
    get_links()
    get_data()
    write_to_json()

if __name__ == "__main__":
    main()