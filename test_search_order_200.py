#Мирослав Кольцов 10 когорта дипломный проект инженер по тестированию плюс
import Create_and_Search_Order

def test_search_order_status_code_200():
    assert Create_and_Search_Order.search_order().status_code == 200