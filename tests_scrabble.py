"""Tests for technical interview tasks 1 & 2"""

from TECHNICAL import calculate_points, assign_seven_tiles

def test_sum_of_points_for_word():
    assert calculate_points('GUARDIAN') == 10

def test_sum_is_zero_for_empty_string():
      assert calculate_points('') == 0

def test_sum_of_points_for_long_words():
    assert calculate_points('STOCK') == 11

def test_player_rack_length_is_seven():
     letters_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
     assert len(assign_seven_tiles(letters_string)) == 7
