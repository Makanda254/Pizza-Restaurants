# Pizza-Restaurants
A Pizza Restaurant application with a react frontend and a flask backend

# Table of Contents
* Introduction
* Deliverables
* Installation
* Known Bugs
* Technologies used
* License
* Support


## Introduction
You are required to come up with a fully built React frontend application, so you can test if your API is working. 

## Deliverables
## Models

The file `server/models.py` defines the model classes and its relationships**.
Use the following commands to create the initial database `db.sqlite`:

```console
flask db upgrade 
```

The following relationships are implemented:

- A `Restaurant` has many `Pizza`s through `RestaurantPizza`
- A `Pizza` has many `Restaurant`s through `RestaurantPizza`
- A `RestaurantPizza` belongs to a `Restaurant` and belongs to a `Pizza`

Update `server/models.py` to establish the model relationships. Since a
`RestaurantPizza` belongs to a `Restaurant` and a `Pizza`, configure the model
to cascade deletes.



You can seed the database:

```console
python server/seed.py
```

> If you aren't able to get the provided seed file working, you are welcome to
> generate your own seed data to test the application.

## Validations

Add validations to the `RestaurantPizza` model:

- must have a `price` between 1 and 30

## Routes

Set up the following routes. Make sure to return JSON data in the format
specified along with the appropriate HTTP verb.

Recall you can specify fields to include or exclude when serializing a model
instance to a dictionary using to_dict() (don't forget the comma if specifying a
single field).

NOTE: If you choose to implement a Flask-RESTful app, you need to add code to
instantiate the `Api` class in server/app.py.

### GET /restaurants

Return JSON data in the format below:

```json
[
  {
    "address": "address1",
    "id": 1,
    "name": "Karen's Pizza Shack"
  },
  {
    "address": "address2",
    "id": 2,
    "name": "Sanjay's Pizza"
  },
  {
    "address": "address3",
    "id": 3,
    "name": "Kiki's Pizza"
  }
]
```

Recall you can specify fields to include or exclude when serializing a model
instance to a dictionary using `to_dict()` (don't forget the comma if specifying
a single field).

### GET /restaurants/<int:id>

If the `Restaurant` exists, return JSON data in the format below:

```json
{
  "address": "address1",
  "id": 1,
  "name": "Karen's Pizza Shack",
  "restaurant_pizzas": [
    {
      "id": 1,
      "pizza": {
        "id": 1,
        "ingredients": "Dough, Tomato Sauce, Cheese",
        "name": "Emma"
      },
      "pizza_id": 1,
      "price": 1,
      "restaurant_id": 1
    }
  ]
}
```

If the `Restaurant` does not exist, return the following JSON data, along with
the appropriate HTTP status code:

```json
{
  "error": "Restaurant not found"
}
```

### DELETE /restaurants/<int:id>

If the `Restaurant` exists, it should be removed from the database, along with
any `RestaurantPizza`s that are associated with it (a `RestaurantPizza` belongs
to a `Restaurant`). If you did not set up your models to cascade deletes, you
need to delete associated `RestaurantPizza`s before the `Restaurant` can be
deleted.

After deleting the `Restaurant`, return an _empty_ response body, along with the
appropriate HTTP status code.

If the `Restaurant` does not exist, return the following JSON data, along with
the appropriate HTTP status code:

```json
{
  "error": "Restaurant not found"
}
```

### GET /pizzas

Return JSON data in the format below:

```json
[
  {
    "id": 1,
    "ingredients": "Dough, Tomato Sauce, Cheese",
    "name": "Emma"
  },
  {
    "id": 2,
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni",
    "name": "Geri"
  },
  {
    "id": 3,
    "ingredients": "Dough, Sauce, Ricotta, Red peppers, Mustard",
    "name": "Melanie"
  }
]
```

### POST /restaurant_pizzas

This route should create a new `RestaurantPizza` that is associated with an
existing `Pizza` and `Restaurant`. It should accept an object with the following
properties in the body of the request:

```json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```

If the `RestaurantPizza` is created successfully, send back a response with the
data related to the `RestaurantPizza`:

```json
{
  "id": 4,
  "pizza": {
    "id": 1,
    "ingredients": "Dough, Tomato Sauce, Cheese",
    "name": "Emma"
  },
  "pizza_id": 1,
  "price": 5,
  "restaurant": {
    "address": "address3",
    "id": 3,
    "name": "Kiki's Pizza"
  },
  "restaurant_id": 3
}
```

If the `RestaurantPizza` is **not** created successfully due to a validation
error, return the following JSON data, along with the appropriate HTTP status
code:

```json
{
  "errors": ["validation errors"]
}
```


## Set Up/ Installation 
- Clone the repository or download the source code.
- Make sure you have python or python3 installed on your system.
- Open the cloned folder with vscode.
To download the dependencies for the frontend and backend, run:

```console
pipenv install
pipenv shell
npm install --prefix client
```

You can run your Flask API on [`localhost:5555`](http://localhost:5555) by
running:

```console
python server/app.py
```

You can run your React app on [`localhost:4000`](http://localhost:4000) by
running:

```sh
npm start --prefix client
```

**Ensure your internet connection is stable to facilitate the download of the source code**


## Known Bugs
The application works well.

## Technologies used
- Terminal
- Python
- Flask
- JavaScript
- React

# License
This project is licensed under the MIT License.

## Support and contact details
- email :: victormakanda254@gmail.com
- phone :: +254768918629
