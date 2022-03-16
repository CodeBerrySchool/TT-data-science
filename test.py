import file_handler

test_video_game_sales = file_handler.get_dicts_from_csv('vg_sales.csv')[:3]
print(test_video_game_sales)
print(file_handler.write_dicts_to_csv('test_sales.csv', test_video_game_sales))