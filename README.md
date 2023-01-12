# Get info on any GitHub profile and its repositories by searching through username.

## Run Locally

Clone the project

```bash
  git clone https://github.com/vaibbhavk/github-stats-server.git
```

Go to the project directory

```bash
  cd github-stats-server
```

Create a virtual environment

```bash
  py -3 -m venv venv_name
```

Activate the virtual environment

```bash
  venv_name\Scripts\activate.bat
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
```

Server will be running on `http://localhost:8000/`.

## Running Tests

To run tests, run the following command

```bash
  py -m pytest
```

## Tech Stack

**Client:** Angular, Bootstrap

**Server:** FastAPI

## Author

- [@vaibbhavk](https://www.github.com/vaibbhavk)
