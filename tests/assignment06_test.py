import data_conversion
import file_handler
import platform_sales
from testfixtures import compare

def test_sum():
    test_video_game_sales = file_handler.get_dicts_from_csv('vg_sales.csv')[:3]
    test_sum = platform_sales.sum_gamesales_by_territory(
        test_video_game_sales, 'Global_Sales')
    assert test_sum == 158.8

def test_sum_by_platform():
    test_video_game_sales = file_handler.get_dicts_from_csv('vg_sales.csv')[:3]
    test_sum_by_platform = platform_sales.sum_platform_sales(platform_sales.get_gamesales_by_platforms(
        test_video_game_sales)[0].items(), data_conversion.get_sales_keys(test_video_game_sales))
    compare(test_sum_by_platform, result)

result = {
    'Platform': 'NES',
    'NA_Sales': 29.08,
    'EU_Sales': 3.58,
    'JP_Sales': 6.81,
    'Other_Sales': 0.77,
    'Global_Sales': 40.24
}
