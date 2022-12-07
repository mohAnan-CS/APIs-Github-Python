import requests
import json


def get_commits():
    _headers = {
        "accept": "application/vnd.github+json",
        "Authorization": "Bearer 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",
        "X-GitHub-Api-Version": "2022-11-28"}
    r = requests.get('https://api.github.com/repos/mohAnan-CS/Accounting-System-DesktopApp/commits', headers=_headers)
    print(json.dumps(r.json(), indent=4))


def get_repos():
    _headers = {
        "accept": "application/vnd.github+json",
        "Authorization": "Bearer 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",
        "X-GitHub-Api-Version": "2022-11-28"}
    r = requests.get('https://api.github.com/users/mohAnan-CS/repos', headers=_headers)
    print(json.dumps(r.json(), indent=2))

def get_all_name_repos():
    


# def get_repos():
# def get_commits_for_repo
if __name__ == '__main__':
    get_commits()
    get_repos()
