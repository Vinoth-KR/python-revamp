from name_function import get_formatted_name


def test_first_last_name():
    """Do names like James Anderson work?"""
    formatted_name = get_formatted_name('james', 'anderson')
    assert formatted_name == 'James Anderson'


def test_first_last_middle_name():
    """Do names like James Robert Anderson work?"""
    formatted_name = get_formatted_name('james', 'anderson', 'robert')
    assert formatted_name == 'James Robert Anderson'