# Technical Exercises

This repository contains a Flask application with exercises requested by an employer.

---

## How to install the project

1. Clone the repository.

This project is available on Github. Clone with your prefered git tool or with the command:

` git clone https://github.com/WatchmakerLoL/pokemon-team-manager.git `


2. Set up a virtual environment and activate it.

Go to a folder outside the project and create the virtualenv using the following command:

` python3 -m venv /path/to/new/virtual/environment `
 
Then you should activate it by running the following command inside the virtualenv folder:

` activate `

3. Make sure you have Flask installed in the virtualenv.

` pip install Flask `

4. Run the server.

` flask run `

---


## How to use the API

This API has 3 endpoints, one for each exercise.

- check-order-status
- check-season-delivered
- detect-changes

Make either a GET or POST request to those endpoints submitting the aproppiate data.

Example Exercise 1:

```
[
    { "order_number": "ORD_1567", "item_name": "LAPTOP", "status": "SHIPPED" },
    { "order_number": "ORD_1567", "item_name": "MOUSE", "status": "SHIPPED" },
    { "order_number": "ORD_1567", "item_name": "KEYBOARD", "status": "PENDING" },
    { "order_number": "ORD_1234", "item_name": "GAME", "status": "SHIPPED" },
    { "order_number": "ORD_1234", "item_name": "BOOK", "status": "CANCELLED" },
    { "order_number": "ORD_1234", "item_name": "BOOK", "status": "CANCELLED" },
    { "order_number": "ORD_9834", "item_name": "SHIRT", "status": "SHIPPED" },
    { "order_number": "ORD_9834", "item_name": "PANTS", "status": "CANCELLED" },
    { "order_number": "ORD_7654", "item_name": "TV", "status": "CANCELLED" },
    { "order_number": "ORD_7654", "item_name": "DVD", "status": "CANCELLED" }
]
```

Example Exercise 2:

```
[
    { "ORD_ID": "113-8909896-6940269", "ORD_DT": "9/23/19", "QT_ORDD": "1"},
    { "ORD_ID": "114-0291773-7262677", "ORD_DT": "1/1/20", "QT_ORDD": "1"},
    { "ORD_ID": "114-0291773-7262697", "ORD_DT": "12/5/19", "QT_ORDD": "1"},
    { "ORD_ID": "114-9900513-77610000", "ORD_DT": "9/24/20", "QT_ORDD": "1"},
    { "ORD_ID": "112-5230502-8173028", "ORD_DT": "1/30/20", "QT_ORDD": "1"},
    { "ORD_ID": "112-7714081-3300254", "ORD_DT": "5/2/20", "QT_ORDD": "1"},
    { "ORD_ID": "114-5384551-1465853", "ORD_DT": "4/2/20", "QT_ORDD": "1"},
    { "ORD_ID": "114-7232801-4607440", "ORD_DT": "10/9/20", "QT_ORDD": "1"}
]
```

Example Exercise 3:

```
[
    { "date": "1/1/20", "was_rainy": false },
    { "date": "1/2/20", "was_rainy": true },
    { "date": "1/3/20", "was_rainy": true },
    { "date": "1/4/20", "was_rainy": false },
    { "date": "1/5/20", "was_rainy": false },
    { "date": "1/6/20", "was_rainy": true },
    { "date": "1/7/20", "was_rainy": false },
    { "date": "1/8/20", "was_rainy": true },
    { "date": "1/9/20", "was_rainy": true },
    { "date": "1/10/20", "was_rainy": true }
]
```
---

## Technical Stack.


|        | Version |
|--------|-------|
| Python | 3.9   |
| Flask  | 2.1   |
