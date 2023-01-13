from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_get_profile():
    response = client.get("/api/v1/github/user/?username=vaibbhavk")
    assert response.status_code == 200
    assert response.json() == {
    "login": "vaibbhavk",
    "id": 67103161,
    "avatar_url": "https://avatars.githubusercontent.com/u/67103161?v=4",
    "html_url": "https://github.com/vaibbhavk",
    "name": "Vaibhav Kesharwani",
    "location": "Satna, Madhya Pradesh, India",
    "bio": "Computer Science Student, Data Scientist, Android Developer, and Web Developer.",
    "twitter_username": None
}

def test_get_profile_invalid_username():
    response = client.get("/api/v1/github/user/?username=vaibbhavky")
    assert response.status_code == 404
    assert response.json() == {
    "detail": "Not Found"
}


def test_get_repos():
    response = client.get("/api/v1/github/repos/?username=vaibbhavk")
    assert response.status_code == 200
    assert response.json() == [
    {
        "id": 397696463,
        "name": "about-me-android",
        "html_url": "https://github.com/vaibbhavk/about-me-android",
        "description": "A basic android app made using Kotlin.",
        "topics": []
    },
    {
        "id": 516751224,
        "name": "android-jetpack-compose-navigation",
        "html_url": "https://github.com/vaibbhavk/android-jetpack-compose-navigation",
        "description": None,
        "topics": []
    },
    {
        "id": 397709986,
        "name": "android-trivia",
        "html_url": "https://github.com/vaibbhavk/android-trivia",
        "description": "An android app. It makes use of the Navigation component within Jetpack to move the user between different screens. Used Kotlin programming language.",
        "topics": []
    },
    {
        "id": 397713693,
        "name": "dice-roller",
        "html_url": "https://github.com/vaibbhavk/dice-roller",
        "description": "A dice roller android app using Kotlin.",
        "topics": []
    },
    {
        "id": 440780818,
        "name": "educative.io_courses",
        "html_url": "https://github.com/vaibbhavk/educative.io_courses",
        "description": "this is downloadings of all educative.io free student subscription courses as pdf from GitHub student pack",
        "topics": []
    },
    {
        "id": 397716509,
        "name": "expense-tracker-app",
        "html_url": "https://github.com/vaibbhavk/expense-tracker-app",
        "description": "An expense tracker app. Used react, react hooks and react context api.",
        "topics": []
    },
    {
        "id": 564289450,
        "name": "fake-db",
        "html_url": "https://github.com/vaibbhavk/fake-db",
        "description": None,
        "topics": []
    },
    {
        "id": 389274351,
        "name": "Front-end-React",
        "html_url": "https://github.com/vaibbhavk/Front-end-React",
        "description": "Simple UI replication. Used React.",
        "topics": []
    },
    {
        "id": 426498417,
        "name": "github-profile-readme-generator",
        "html_url": "https://github.com/vaibbhavk/github-profile-readme-generator",
        "description": "🚀 Generate GitHub profile README easily with the latest add-ons like visitors count, GitHub stats, etc using minimal UI.",
        "topics": []
    },
    {
        "id": 588119490,
        "name": "github-stats-angular",
        "html_url": "https://github.com/vaibbhavk/github-stats-angular",
        "description": None,
        "topics": []
    },
    {
        "id": 588131182,
        "name": "github-stats-server",
        "html_url": "https://github.com/vaibbhavk/github-stats-server",
        "description": None,
        "topics": []
    },
    {
        "id": 513456618,
        "name": "Learn-Together",
        "html_url": "https://github.com/vaibbhavk/Learn-Together",
        "description": "Jetpack Compose",
        "topics": []
    },
    {
        "id": 562353018,
        "name": "leva",
        "html_url": "https://github.com/vaibbhavk/leva",
        "description": "🌋 React-first components GUI",
        "topics": []
    },
    {
        "id": 441634951,
        "name": "material-kit-react",
        "html_url": "https://github.com/vaibbhavk/material-kit-react",
        "description": "Minimal Dashboard - build with React Material UI components.",
        "topics": []
    },
    {
        "id": 583218779,
        "name": "milo",
        "html_url": "https://github.com/vaibbhavk/milo",
        "description": None,
        "topics": []
    },
    {
        "id": 577145734,
        "name": "MVVMRecipeApp",
        "html_url": "https://github.com/vaibbhavk/MVVMRecipeApp",
        "description": "Kotlin, MVVM, Navigation Component, Hilt, Jetpack Compose, Retrofit2",
        "topics": []
    },
    {
        "id": 440781839,
        "name": "Object-Oriented-Design-Pattern-Interview",
        "html_url": "https://github.com/vaibbhavk/Object-Oriented-Design-Pattern-Interview",
        "description": "Educative.io - Grokking the Object Oriented Design Interview",
        "topics": []
    },
    {
        "id": 440789751,
        "name": "parking-lot-backend",
        "html_url": "https://github.com/vaibbhavk/parking-lot-backend",
        "description": "Node.js, Express, Sequelize, JWT Authentication, MySQL.",
        "topics": []
    },
    {
        "id": 441623417,
        "name": "parking-lot-frontend",
        "html_url": "https://github.com/vaibbhavk/parking-lot-frontend",
        "description": "Next.js, React, Redux-toolkit, MUI, HTML, CSS, Axios.",
        "topics": []
    },
    {
        "id": 443951506,
        "name": "portfolio-sanity",
        "html_url": "https://github.com/vaibbhavk/portfolio-sanity",
        "description": "My portfolio website using Sanity.io.",
        "topics": []
    },
    {
        "id": 563868151,
        "name": "product-patient-spring-boot",
        "html_url": "https://github.com/vaibbhavk/product-patient-spring-boot",
        "description": None,
        "topics": []
    },
    {
        "id": 567207459,
        "name": "react-test",
        "html_url": "https://github.com/vaibbhavk/react-test",
        "description": "MERN frontend example.",
        "topics": []
    },
    {
        "id": 567208169,
        "name": "react-test-backend",
        "html_url": "https://github.com/vaibbhavk/react-test-backend",
        "description": "MERN backend example.",
        "topics": []
    },
    {
        "id": 504269366,
        "name": "real-estate-marketplace",
        "html_url": "https://github.com/vaibbhavk/real-estate-marketplace",
        "description": None,
        "topics": []
    },
    {
        "id": 573907870,
        "name": "replica-1",
        "html_url": "https://github.com/vaibbhavk/replica-1",
        "description": "Replicated a UI using Next.js and Tailwind CSS",
        "topics": []
    },
    {
        "id": 563291577,
        "name": "rotate-pdf-page",
        "html_url": "https://github.com/vaibbhavk/rotate-pdf-page",
        "description": "REST API for rotating a pdf file page.",
        "topics": []
    },
    {
        "id": 399244433,
        "name": "study-helper",
        "html_url": "https://github.com/vaibbhavk/study-helper",
        "description": "This app can create list of subjects, add topics under each subject, add notes under each topic, edit or delete each subject or topic. Used firebase as backend and reactjs for frontend and material ui for design.",
        "topics": []
    },
    {
        "id": 397612124,
        "name": "todo-app-react",
        "html_url": "https://github.com/vaibbhavk/todo-app-react",
        "description": "A react app to manage todos. Used react hooks, material-ui and styled components.",
        "topics": []
    },
    {
        "id": 426897308,
        "name": "todo-django-api",
        "html_url": "https://github.com/vaibbhavk/todo-django-api",
        "description": "This is a basic REST API for adding, updating, deleting tasks. Used Django Rest Framework.",
        "topics": []
    },
    {
        "id": 572409417,
        "name": "todo_app_v2",
        "html_url": "https://github.com/vaibbhavk/todo_app_v2",
        "description": None,
        "topics": []
    }
]

def test_get_repos_invalid_username():
    response = client.get("/api/v1/github/user/?username=vaibbhavky")
    assert response.status_code == 404
    assert response.json() == {
    "detail": "Not Found"
}