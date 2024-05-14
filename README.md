# Juxta :thought_balloon:

Juxta is a Streamlit web application that allows users to connect their thoughts by searching for similar thoughts based on user input and add to the database.

![alt text](https://github.com/Vipi-14/juxta-search_your_thoughts/blob/master/db/img.png?raw=true)


## Overview

Juxta uses SentenceTransformer to encode text into embeddings and then calculates cosine similarity to find similar thoughts from a pre-existing database of texts.

## Features

- **Thought Search**: Users can enter their thought, and the application will search for similar thoughts from the database.
- **Add to Notes**: Users can add their thought to the database for future searches.
- **Database Persistence**: The database of texts is stored in a JSON file and is updated dynamically when new thoughts are added.

## Setup

1. Clone the repository:



## Install dependencies:

pip install -r requirements.txt

## Run the Streamlit app:

streamlit run app.py

## Usage

Enter your thought in the text input field.
Click on the "Enter" button or press "Enter" on your keyboard to start the search.
If similar thoughts are found, they will be displayed on the screen.
If no similar thoughts are found, a message will be displayed indicating so.
You can click on the "Add to Notes" button to add your thought to the database.
Database
The database of texts is stored in a JSON file named texts.json located in the db directory.

## Contributing

Contributions are welcome! If you have any ideas for improvement or would like to fix any issues, feel free to open a pull request.

License
This project is licensed under the MIT License.
