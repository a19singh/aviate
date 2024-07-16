# Aviate POC


## Introduction
A POC for the provided problem statement:

Build REST API server for basic ATS for recruiters.
- It should have api endpoints to create, search, shortlist or reject candidates.
- It should be able to store the candidate's name, age, gender, years_of_exp, phone number, email, current salary and expected salary. Apart from this there will be a status field, which will be _Applied_ by default and it will change if the candidate gets shortlisted or rejected.
- Search api should be a listing api, which can be used to filter/search for specific candidates, who satisfy all the applied conditions. Example of search conditions:
- Search for all candidates whose expected salary is between 8 to 12.
- Search for candidates whose age is between 21 to 30 and years of exp is more than 3.
- Search for candidate based of there phone number, email or name.

Bonus Point
_______
- Create a separate api for name based search, which has a relevance based sorting. So that given a query, the api should return results in the following order:
- On Top, Should be exact matches, where the query matches the name exactly.
- After that should be all the names where some of the words in the query match the words in the name, in the descending order of number of overlapping words.
- Example: if a query is _Ajay Kumar yadav_ the order of results will be [_Ajay Kumar Yadav_, _Ajay Kumar_, _Ajay Yadav_, _Kumar Yadav_, _Ramesh Yadav_, _Ajay Singh_]
- Write as optimised version of this logic as you can possibly think of.


## Technologies Used
- Python
- Django
- DjangoRestFramework

## Installation:

1. Clone the repo:
```bash
    git clone https://github.com/a19singh/aviate.git
```

2. Navigate to the project directory:
```bash
cd aviate
```

3. Before starting create a python virtual env using:

```sh
python3 -m venv pyenv
```

4. To activate the environment, use:

```sh
source pyenv/bin/activate
```
 
5. Install dependencies using command:

```sh
pip3 install -r requirements.txt
```

## Usage

Start the Server on localhost, using command:

```sh
python poc/manage.py runserver
```

## How to Test:

A postman collection named 'Aviate.postman_collection.json' can be found inside the repo clone, kindly import that in your Postman Application and api endpoints can be tested from there.
