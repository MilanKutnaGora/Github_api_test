import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")

BASE_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


def test_github_api():
    # Создание репозитория
    create_repo_url = f"{BASE_URL}/user/repos"
    create_repo_data = {"name": REPO_NAME, "auto_init": True}
    response = requests.post(create_repo_url, json=create_repo_data, headers=HEADERS)
    assert response.status_code == 201, f"Failed to create repository: {response.text}"

    # Проверка наличия репозитория
    list_repos_url = f"{BASE_URL}/user/repos"
    response = requests.get(list_repos_url, headers=HEADERS)
    assert response.status_code == 200, f"Failed to list repositories: {response.text}"
    repos = response.json()
    assert any(repo["name"] == REPO_NAME for repo in repos), f"Repository {REPO_NAME} not found in the list"

    # Удаление репозитория
    delete_repo_url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.delete(delete_repo_url, headers=HEADERS)
    assert response.status_code == 204, f"Failed to delete repository: {response.text}"

    # Проверка удаления репозитория
    response = requests.get(list_repos_url, headers=HEADERS)
    assert response.status_code == 200, f"Failed to list repositories: {response.text}"
    repos = response.json()
    assert not any(repo["name"] == REPO_NAME for repo in repos), f"Repository {REPO_NAME} still exists after deletion"


if __name__ == "__main__":
    pytest.main([__file__])