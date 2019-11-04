import Services.servicesClass as Service


def test_add_complex_number_to_list_emptylist_2_3i():
    list = []
    service = Service.Services.add_complex_number_to_list(list, 2, 3)
    assert list == ["2+3i"]


def test_add_complex_number_to_list_emptylist_14i():
    list = []
    service = Service.Services.add_complex_number_to_list(list, 0, 14)
    assert list == ["14i"]


def test_add_complex_number_to_list_emptylist_aaa_ValueError():
    list = []
    service = Service.Services.add_complex_number_to_list(list, "aaa", 2)
    assert ValueError


def test_filter_list_from_start_to_end_position_list_23456_start1_end3_345():
    list = [2, 3, 4, 5, 6]
    service = Service.Services.filter_list_from_start_to_end_position(list, 1, 3)
    assert list == [3, 4, 5]


def test_filter_list_from_start_to_end_position_list_23456_start1_end0_IndexError():
    list = [2, 3, 4, 5, 6]
    service = Service.Services.filter_list_from_start_to_end_position(list, 1, 0)
    assert IndexError


def test_all_functions():
    test_add_complex_number_to_list_emptylist_2_3i()
    test_add_complex_number_to_list_emptylist_14i()
    test_filter_list_from_start_to_end_position_list_23456_start1_end3_345()
    test_filter_list_from_start_to_end_position_list_23456_start1_end0_IndexError()
    test_add_complex_number_to_list_emptylist_aaa_ValueError()