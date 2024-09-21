import json
import numpy as np
import pickle


def get_estimated_price(location, sqft, bhk, bath):
    try:
        dc = load_data_columns()
        loc_index = dc.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(dc))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(load_model().predict([x])[0], 2)


def get_location_names():
    return load_data_columns()[3:]


def load_data_columns():
    print("Loading the saved artifacts....")

    with open("./model/columns.json", "r") as f:
        data_columns = json.load(f)["data_columns"]
    return data_columns


def load_model():
    with open("./model/banglore_home_prices_model.pickle", "rb") as f:
        model = pickle.load(f)
    return model


if __name__ == "__main__":
    print(get_estimated_price("1st block jayanagar", 1000, 3, 3))
