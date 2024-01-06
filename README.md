<img style="float: left; padding-right: 10px; width: 200px" src="https://upload.wikimedia.org/wikipedia/fr/b/b1/Logo_EPF.png?raw=true"> 

## Data Source API
**P2024** antoine-courbi

# Developping a web application

### [*Moodle course*](https://moodle.epf.fr/course/view.php?id=9502&section=2)
### [*Github depository*](https://github.com/TonioElPuebloSchool/Data_Source_IOT_TP2)
-----

This **README** is meant to explain how the **application runs** and give some **explanations** on what have been implemented.

# **Answers to the Questions**

1. **Question 1:**
   - **Flask**

2. **Question 2:**
   - **FastAPI is renowned for its increased speed and performance compared with Django and Flask.**
     *(<span style="color:green">Explanation:</span> I found usefull information [here](https://medium.com/@tubelwj/comparison-of-flask-django-and-fastapi-advantages-disadvantages-and-use-cases-63e7c692382a#:~:text=Flask%20is%20suitable%20for%20small%20projects%20and%20developers%20who%20require,%2Dperformance%20real%2Dtime%20applications.) : FastAPI is known for its automatic data validation, generation of OpenAPI documentation, and high performance, making it a popular choice for building fast APIs.)*

3. **Question 3:**
   - **A specific URL to which a request can be sent to interact with the API.**
     *(<span style="color:green">Explanation:</span> In REST APIs, an endpoint is a specific URL or URI (Uniform Resource Identifier) that represents a resource. It is the path where API users can send requests. as I found[here](https://www.techtarget.com/searchapparchitecture/definition/API-endpoint#:~:text=An%20API%20endpoint%20is%20a,server%20and%20receiving%20a%20response.))*

4. **Question 4:**
   - **GET, POST, PUT, PATCH, DELETE**
     *(<span style="color:green">Explanation:</span> They are all [here](https://www.restapitutorial.com/lessons/httpmethods.html))*

5. **Question 5:**
   - **Intermediate software that processes the request before it reaches the main application.**
     *(<span style="color:green">Explanation:</span> Middleware in the context of REST APIs refers to software components that can handle aspects like authentication, logging, or request modification before reaching the main application logic.)*

6. **Question 6:**
   - **json.dumps() and json.loads()**

7. **Question 7:**
   - **Update an existing resource, or create one if it doesn't exist.**
     *(<span style="color:green">Explanation:</span> The HTTP "PUT" method is used to update a resource or create it if it doesn't exist.)*

8. **Question 8:**
   - **@app.post("/endpoint")**

# **Requirements**
In order to run the application **locally** after downloading the github reposiroty, it's possible to create a **virtual environment** with the following command:
```bash
python3 -m venv env
```
Then, the **virtual environment** can be **activated** with the following command:
```bash
source env/bin/activate
```
Then, the following **requirements** are needed to run the application:
```bash
pip install -r services\epf-flower-data-science\requirements.txt
```

Important to note that the application requires **google cloud credentials** to be able to access the **firestore database**. The credentials are stored in the following file, and should be **created by the user**:
```bash
services\epf-flower-data-science\src\api\datasourceapi-b7fac-firebase-adminsdk-53gb4-757878c47f.json
```
The application also requires **kaggle credentials** to be able to download the data from the **kaggle API**. The credentials are stored in the following file, and should be **created by the user**:
```bash
services\epf-flower-data-science\src\api\kaggle.json
```

# **Running the application**

The application can be run with the following command:
```bash
python services\epf-flower-data-science\main.py
```
The application can be accessed on port **8000** on the **localhost**. or following this [link](http://localhost:8000/).

# **Overview**

This application is a **data science project** focused on flower classification. It is implemented in **Python** using the **FastAPI** framework for the backend, and it uses **machine learning models** for the classification tasks. The application also integrates with **Firestore** for parameter storage and retrieval.

The application is structured around the following key components:

- `main.py`: This is the **entry point** of the application. It sets up and starts the FastAPI server.
- `app.py`: This file contains the application's **FastAPI instance** and the **API route definitions**.
- `data.py`: This file contains the **API routes related to data processing and model training**.
- `parameters.py`: This file contains the **API routes related to Firestore operations**.

The application provides the following endpoints:

- `PUT /update_firestore`: This endpoint **updates a document in Firestore** with a new value.
- `POST /add_param_firestore`: This endpoint **adds a new document to Firestore**.
- `GET /train_model_with_firestore`: This endpoint **trains a model with parameters from Firestore**.
- `GET /predict_model_with_firestore`: This endpoint **predicts a class using a model and parameters from Firestore**.
- `GET /download_dataset`: This endpoint **downloads the dataset**.
- `GET /loading_dataset`: This endpoint **loads the Iris dataset**.
- `GET /process_data`: This endpoint **processes the dataset**.
- `GET /split_train_test`: This endpoint **splits the dataset into training and test sets**.
- `GET /train_model`: This endpoint **trains the model**.
- `GET /predict_model`: This endpoint **predicts a class using the model**.

Each endpoint plays a crucial role in the application. The Firestore endpoints allow users to **manage training parameters** in a flexible way. The data processing and model training endpoints provide a **complete machine learning pipeline**, from data download to model training and prediction.

# **Architecture**

The application is composed of the following important files :
```bash
C:.
│   INSTRUCTIONS.md
│   README.md
├───.github
│   └───workflows
│           python-app.yml
│           run-tests.yml
├───data
└───services
    └───epf-flower-data-science
        │   main.py
        │   requirements.txt
        ├───src
        │   │   app.py
        │   │   __init__.py
        │   ├───api
        │   │   │   router.py
        │   │   │   __init__.py
        │   │   ├───routes
        │   │   │   │   authentication.py
        │   │   │   │   data.py
        │   │   │   │   hello.py
        │   │   │   │   parameters.py
        │   │   │   │   __init__.py
        │   │       datasourceapi-b7fac-firebase-adminsdk-53gb4-757878c47f.json
        │   │       model_parameters.json
        │   │       __init__.py
        │   │
        │   ├───services
        │   │   │   cleaning.py
        │   │   │   data.py
        │   │   │   firestore.py
        │   │   │   parameters.py
        │   │   │   __init__.py
        │
        ├───tests
        │   ├───unit
        │   │   ├───api
        │   │   │   ├───routes
        │   │   │   │   │   test_data.py
        │   │   │   │   │   test_hello.py
        │   │   │   │   │   test_parameters.py
        │   │   │   │   │   __init__.py
```

# **Github Actions**

The application has a **CI/CD pipeline** that is defined in the following file:
```bash
.github\workflows\python-app.yml
```
The tests are automatically run after every push on the **master** branch, as written in the following file:
```bash
.github\workflows\run-tests.yml
```

# **Other features**

The application uses **pep8** to check the code style, and follows the **docstring conventions**.

And **error 404 handler** has been implemented to handle the case where the user tries to access a page that **doesn't exist** in the following file:
```bash 
services\epf-flower-data-science\src\api\app.py
```

Thank you for reading this README. I hope you enjoyed it. If you have any remarks or questions, feel free to contact me on [LinkedIn](https://www.linkedin.com/in/antoine-courbi/).

<p align="center">&mdash; ⭐️ &mdash;</p>
<p align="center"><i>This README was created during the Data Source API course</i></p>
<p align="center"><i>Created by Antoine Courbi</i></p>