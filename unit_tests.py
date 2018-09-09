import unittest
import bowling

class GameClassMethods(unittest.TestCase):
    def test_calculate_score_with_all_strikes(self):

        game = bowling.Game()

        frame_1 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
        game.add_frame(frame_1)

        frame_2 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
        game.add_frame(frame_2)

        frame_3 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
        game.add_frame(frame_3)

        frame_4 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
        game.add_frame(frame_4)

        frame_5 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
        game.add_frame(frame_5)

        frame_6 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
        game.add_frame(frame_6)

        frame_7 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
        game.add_frame(frame_7)

        frame_8 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
        game.add_frame(frame_8)

        frame_9 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
        game.add_frame(frame_9)

        frame_10 = bowling.Frame(ball_one = 10, ball_two = 10, ball_three = 10, frame_score = 30)
        game.add_frame(frame_10)

        game.calculate_score()

        self.assertEqual(game.total_score, 300)

    def test_calculate_score_with_gutter_on_third_ball_tenth_frame(self):

            game = bowling.Game()

            frame_1 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_1)

            frame_2 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_2)

            frame_3 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_3)

            frame_4 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_4)

            frame_5 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_5)

            frame_6 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_6)

            frame_7 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_7)

            frame_8 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_8)

            frame_9 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_9)

            frame_10 = bowling.Frame(ball_one = 10, ball_two = 10, ball_three = 0, frame_score = 20)
            game.add_frame(frame_10)

            game.calculate_score()

            self.assertEqual(game.total_score, 290)

    def test_calculate_score_with_gutter_on_second_ball_tenth_frame(self):

            game = bowling.Game()

            frame_1 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_1)

            frame_2 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_2)

            frame_3 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_3)

            frame_4 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_4)

            frame_5 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_5)

            frame_6 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_6)

            frame_7 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_7)

            frame_8 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_8)

            frame_9 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_9)

            frame_10 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 10, frame_score = 20)
            game.add_frame(frame_10)

            game.calculate_score()

            self.assertEqual(game.total_score, 280)

    def test_calculate_score_with_spare_on_tenth_frame(self):

            game = bowling.Game()

            frame_1 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_1)

            frame_2 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_2)

            frame_3 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_3)

            frame_4 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_4)

            frame_5 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_5)

            frame_6 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_6)

            frame_7 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_7)

            frame_8 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_8)

            frame_9 = bowling.Frame(ball_one = 10, ball_two = 0, ball_three = 0, frame_score = 10, isStrike = True)
            game.add_frame(frame_9)

            frame_10 = bowling.Frame(ball_one = 0, ball_two = 10, ball_three = 10, frame_score = 20)
            game.add_frame(frame_10)

            game.calculate_score()

            self.assertEqual(game.total_score, 270)

    def test_calculate_score_with_all_gutters(self):

            game = bowling.Game()

            frame_1 = bowling.Frame(ball_one = 0, ball_two = 0, ball_three = 0, frame_score = 0)
            game.add_frame(frame_1)

            frame_2 = bowling.Frame(ball_one = 0, ball_two = 0, ball_three = 0, frame_score = 0)
            game.add_frame(frame_2)

            frame_3 = bowling.Frame(ball_one = 0, ball_two = 0, ball_three = 0, frame_score = 0)
            game.add_frame(frame_3)

            frame_4 = bowling.Frame(ball_one = 0, ball_two = 0, ball_three = 0, frame_score = 0)
            game.add_frame(frame_4)

            frame_5 = bowling.Frame(ball_one = 0, ball_two = 0, ball_three = 0, frame_score = 0)
            game.add_frame(frame_5)

            frame_6 = bowling.Frame(ball_one = 0, ball_two = 0, ball_three = 0, frame_score = 0)
            game.add_frame(frame_6)

            frame_7 = bowling.Frame(ball_one = 0, ball_two = 0, ball_three = 0, frame_score = 0)
            game.add_frame(frame_7)

            frame_8 = bowling.Frame(ball_one = 0, ball_two = 0, ball_three = 0, frame_score = 0)
            game.add_frame(frame_8)

            frame_9 = bowling.Frame(ball_one = 0, ball_two = 0, ball_three = 0, frame_score = 0)
            game.add_frame(frame_9)

            frame_10 = bowling.Frame(ball_one = 0, ball_two = 0, ball_three = 0, frame_score = 0)
            game.add_frame(frame_10)

            game.calculate_score()

            self.assertEqual(game.total_score, 0)


if __name__ == '__main__':
    unittest.main()