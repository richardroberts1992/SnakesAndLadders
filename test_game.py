import unittest
from game import roll_die, move_player, snakes, ladders, BOARD_SIZE

# The following line might be needed if tests affect game.py's global player_positions
# For now, move_player is pure enough if we pass current_pos directly.
# import game # To potentially reset game.player_positions if needed

class TestSnakesAndLadders(unittest.TestCase):

    def test_roll_die(self):
        """Test if roll_die returns values within the 1-6 range."""
        for _ in range(100): # Run multiple times
            roll = roll_die()
            self.assertTrue(1 <= roll <= 6, f"Die roll out of range: {roll}")

    def test_player_movement(self):
        """Test various player movement scenarios."""
        # 1. Test basic movement
        # Ensure the target square for basic movement isn't a snake head or ladder bottom.
        # Square 2 is not a snake/ladder.
        self.assertEqual(move_player(1, 1), 2, "Basic movement failed (1+1->2)") 
        # Square 55 is not a snake/ladder.
        self.assertEqual(move_player(50, 5), 55, "Basic movement failed (50+5->55)")

        # 2. Test landing on a snake
        # Snake example: 16 -> 6. If player is at 10 and rolls 6 (lands on 16), should go to 6.
        self.assertEqual(move_player(10, 6), 6, "Snake movement failed (16->6)")
        # Snake example: 98 -> 78. If player is at 92 and rolls 6 (lands on 98), should go to 78.
        self.assertEqual(move_player(92, 6), 78, "Snake movement failed (98->78)")
        # Snake example: 47 -> 26. If player is at 45 and rolls 2 (lands on 47), should go to 26.
        self.assertEqual(move_player(45, 2), 26, "Snake movement failed (47->26)")


        # 3. Test landing on a ladder
        # Ladder example: 4 -> 14. If player is at 1 and rolls 3 (lands on 4), should go to 14.
        self.assertEqual(move_player(1, 3), 14, "Ladder movement failed (4->14)")
        # Ladder example: 9 -> 31. If player is at 7 and rolls 2 (lands on 9), should go to 31.
        self.assertEqual(move_player(7, 2), 31, "Ladder movement failed (9->31)")
        # Ladder example: 71 -> 91. If player is at 70 and rolls 1 (lands on 71), should go to 91.
        self.assertEqual(move_player(70, 1), 91, "Ladder movement failed (71->91)")

        # 4. Test the rule for not exceeding square BOARD_SIZE (100)
        self.assertEqual(move_player(98, 4), 98, "Exceeding BOARD_SIZE rule failed (98+4)")
        self.assertEqual(move_player(97, 6), 97, "Exceeding BOARD_SIZE rule failed (97+6)")
        self.assertEqual(move_player(99, 3), 99, "Exceeding BOARD_SIZE rule failed (99+3)")
        self.assertEqual(move_player(100, 1), 100, "Movement from BOARD_SIZE rule failed (100+1)")
        self.assertEqual(move_player(BOARD_SIZE, 5), BOARD_SIZE, "Movement from BOARD_SIZE rule failed")


    def test_win_condition(self):
        """Test that player's position becomes BOARD_SIZE (100) for a winning move."""
        # Test landing exactly on BOARD_SIZE by normal roll
        self.assertEqual(move_player(97, 3), BOARD_SIZE, "Win condition failed (97+3)")
        self.assertEqual(move_player(95, 5), BOARD_SIZE, "Win condition failed (95+5)")

        # Test landing on a ladder that leads to BOARD_SIZE
        # Ladder example: 80 -> 100. If player is at 78 and rolls 2 (lands on 80), should go to 100.
        self.assertEqual(move_player(78, 2), BOARD_SIZE, "Win via ladder failed (80->100)")
        
        # Test scenario where player is already at 100 (should remain 100, effectively a win state)
        self.assertEqual(move_player(BOARD_SIZE, 3), BOARD_SIZE, "Win condition failed (already at 100)")


if __name__ == '__main__':
    unittest.main()
