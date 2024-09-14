# GitHub API Test

## This project contains an automated test for GitHub API operations using Python.

### Setup

#### 1. Clone the repository:

`git clone https://github.com/MilanKutnaGora/github-api-test.git`
`cd github_api_test`

#### 2. Create a virtual environment and activate it:

`python -m venv venv`
`source venv/bin/activate` 

#### On Windows use 

`venv\Scripts\activate`

#### 3. Install dependencies:

`pip install -r requirements.txt`

#### 4. Create a `.env` file in the project root and add your GitHub credentials:

`GITHUB_USERNAME=your_username`

`GITHUB_TOKEN=your_personal_access_token`

`REPO_NAME=test_repo_name`


#### Note: To create a personal access token, go to GitHub Settings > Developer settings > Personal access tokens.

### Running the Test

#### To run the test, execute the following command:

`pytest test_github_api.py`

#### The test will create a new repository, verify its existence, delete it, and confirm the deletion.

## Note

#### Ensure that your GitHub token has the necessary permissions to create and delete repositories.
