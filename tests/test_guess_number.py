import unittest
from guess_number import guess_number_game

class TestGuessNumber(unittest.TestCase):
    # 這裡可以添加更多測試，根據具體需求。
    def test_game_runs(self):
        # 這個測試主要是檢查遊戲運行邏輯，不涉及玩家輸入。
        self.assertIsNone(guess_number_game())

if __name__ == '__main__':
    unittest.main()
