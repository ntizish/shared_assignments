"""Tests for formula_one.py."""

import pytest
from formula_one import Driver, Race, FormulaOne
import csv

filename = 'ex08_example_data.txt'


def test_race():
    """Test Race class and its methods."""
    r = Race('ex08_example_data.txt')
    assert len(r.raw_data) == 28
    assert r.get_num_of_races() == 4
    """
    WRITE A FUNC THAT CHECKS FOR RIGHT ERROR.
    """
    data_for_extractor = {'Name': 'Mika Hakkinen', 'Team': 'Mclaren-Mercedes', 'Time': 79694, 'Diff': '', 'Race': 1}
    assert r.extract_info(r.raw_data[0]) == data_for_extractor
    data_for_filter21 = {'Name': 'David Coulthard', 'Team': 'Mclaren-Mercedes', 'Time': 77522, 'Diff': '', 'Race': 2}
    data_for_filter40 = {'Name': 'Mika Hakkinen', 'Team': 'Mclaren-Mercedes', 'Time': 77831, 'Diff': '', 'Race': 4}
    assert r.filter_data_by_race(2)[1] == data_for_filter21
    assert r.filter_data_by_race(4)[0] == data_for_filter40
    assert r.format_time('123456') == '2:03.456'
    assert r.format_time('0') == '0:00.000'
    assert Race.calculate_time_difference(4201, 57411) == f"+{r.format_time(f'{57411 - 4201}')}"
    data_to_sort_by_time = r.filter_data_by_race(1)
    assert r.sort_data_by_time(data_to_sort_by_time)[0]['Name'] == 'Jenson Button'
    assert r.get_results_by_race(1)[0]['Team'] == 'Williams-BMW'


def test_formula_one():
    """Test for writing files in FormulaOne class."""
    fo = FormulaOne(filename)
    fo.write_race_results_to_file(2)
    with open('results_for_race_2.txt', 'r') as f:
        read_race_lines = f.readlines()
        assert read_race_lines[2].replace(' ', '') == '1DavidCoulthardMclaren-Mercedes1:17.52225\n'
        first_line = f'PLACE{5 * " "}NAME{21 * " "}TEAM{21 * " "}TIME{11 * " "}DIFF{11 * " "}POINTS\n'
        assert read_race_lines[0] == first_line

    fo.write_race_results_to_csv(1)
    with open('race_1_results.csv', 'r') as f:
        reader = csv.reader(f)
        rows = [r for r in reader]
        assert rows[1] == ['1', 'Jenson Button', 'Williams-BMW', '1:17.606', '', '25', '1']

    fo.write_championship_to_file()
    with open('championship_results.txt', 'r') as f:
        read_champ_lines = f.readlines()
        assert read_champ_lines[8].replace(' ', '') == '7PedrodelaRosaArrows-Supertec36\n'
        first_line_champ = f'PLACE{5 * " "}NAME{21 * " "}TEAM{21 * " "}POINTS\n'
        assert read_champ_lines[0] == first_line_champ


def test_driver():
    """Test Driver class."""
    d = Driver('Huevos Rancheros', 'Garnish-Auto')
    d.add_result(1, 15)
    d.add_result(2, 0)
    d.add_result(3, 25)

    assert d.get_results() == {1: 15, 2: 0, 3: 25}
    assert d.get_points() == 40
    assert d.__dict__() == {'Name': 'Huevos Rancheros', 'Team': 'Garnish-Auto', 'Points': 40}
