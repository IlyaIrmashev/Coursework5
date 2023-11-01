# Класс для получения данных с ресурса HeadHunter
import requests


class HHApi:
    def __init__(self):
        self.employer_data = []
        self.url_hh = "https://api.hh.ru/vacancies"

    def get_vacancies(self):

        search_ids=[1740,23427,84585,592442,3529,15748,1532045,2180,80,1373]
        params = {'employer_id': search_ids, 'per_page': 100}
        vacancies_data = []
        response = requests.get(self.url_hh, params)
        if response.status_code == 200:
            print(response.json())
            vacancies = response.json()["items"]
            for vacancy in vacancies:
                # if vacancy['employer']['id'] == search_query:
                if vacancy['salary'] is not None:
                    vacancy_data = {
                        'id_vacancy': vacancy['id'],
                        'employer_id': vacancy['employer']['id'],
                        'vacancy_name': vacancy['name'],
                        'description': vacancy['snippet']['responsibility'],
                        'area': vacancy['area']['name'],
                        'url': vacancy['alternate_url'],
                        'salary_from': vacancy['salary']['from'],
                        'salary_to': vacancy['salary']['to'],
                        'currency': vacancy['salary']['currency'],
                        'published_at': vacancy['published_at']
                    }
                    vacancies_data.append(vacancy_data)
                    self.employer_data.append({'employer_id': vacancy['employer']['id'], 'name': vacancy['employer']['name'], 'url': vacancy['employer']['url']})
                else:
                    continue
        else:
            print("Error:", response.status_code)
        return self.employer_data, vacancies_data

    @staticmethod
    def get_employers(employer_id):
        employers = []
        response_employers = requests.get(f'https://api.hh.ru/employers/{employer_id}')
        if response_employers.ok:
            data_employer = response_employers.json()
            employer = {'employer_id': data_employer['id'], 'name': data_employer['name'],
                        'url': data_employer['site_url']}
            employers.append(employer)
        return employers
