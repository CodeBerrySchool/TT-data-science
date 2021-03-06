import file_handler
import data_conversion
from testfixtures import compare

def test_has_method():
    assert hasattr(file_handler, 'get_dicts_from_csv')

def test_converter_has_get_method():
    assert hasattr(data_conversion, 'get_sales_keys')

def test_converter_has_modify_method():
    assert hasattr(data_conversion, 'modify_sales_numbers')

def test_get_dict_keys():
    test_video_game_sales = file_handler.get_dicts_from_csv('vg_sales.csv')[:3]
    test_keys = data_conversion.get_sales_keys(test_video_game_sales)
    compare(test_keys, result1)

def test_modify_sales_numbers():
    test_video_game_sales = file_handler.get_dicts_from_csv('vg_sales.csv')[:3]
    test_modified = data_conversion.modify_sales_numbers(test_video_game_sales)
    compare(test_modified, result2)

result1 = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
result2 = [{
    "Rank": "1",
    "Name": "Wii Sports",
    "Platform": "Wii",
    "Year": "2006",
    "Genre": "Sports",
    "Publisher": "Nintendo",
    "NA_Sales": 41.49,
    "EU_Sales": 29.02,
    "JP_Sales": 3.77,
    "Other_Sales": 8.46,
    "Global_Sales": 82.74
},
    {
    "Rank": "2",
    "Name": "Super Mario Bros.",
    "Platform": "NES",
    "Year": "1985",
    "Genre": "Platform",
    "Publisher": "Nintendo",
    "NA_Sales": 29.08,
    "EU_Sales": 3.58,
    "JP_Sales": 6.81,
    "Other_Sales": 0.77,
    "Global_Sales": 40.24
},
    {
    "Rank": "3",
    "Name": "Mario Kart Wii",
    "Platform": "Wii",
    "Year": "2008",
    "Genre": "Racing",
    "Publisher": "Nintendo",
    "NA_Sales": 15.85,
    "EU_Sales": 12.88,
    "JP_Sales": 3.79,
    "Other_Sales": 3.31,
    "Global_Sales": 35.82
}]
