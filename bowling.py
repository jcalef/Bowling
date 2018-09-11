class Game:
    def __init__(self):
        self.frames = []
        self.total_score = 0

    def add_frame(self, frame):
        self.frames.append(frame)

    def calculate_score(self):

        #calculate score ignore 10th frame already calculated
        frame_counter = 0
        while frame_counter < 9:
            
            #bonus balls
            ball_one = 0
            ball_two = 0

            #calculate strike
            if self.frames[frame_counter].isStrike:

                #if the next frame was a strike, find the score of the ball after that frame
                if self.frames[frame_counter+1].isStrike:
                    ball_one = self.frames[frame_counter+1].ball_one
                    ball_two = self.frames[frame_counter+2].ball_one if frame_counter+2 < 10 else self.frames[frame_counter+1].ball_two
                else:
                    ball_one = self.frames[frame_counter+1].ball_one 
                    ball_two = self.frames[frame_counter+1].ball_two


            #calculate spare
            elif self.frames[frame_counter].isSpare:
                ball_one =  self.frames[frame_counter+1].ball_one

            self.total_score += self.frames[frame_counter].frame_score + ball_one + ball_two

            frame_counter +=1 

        #add in final frame
        self.total_score += self.frames[9].frame_score

class Frame:
    def __init__(self, 
                ball_one = 0, 
                ball_two = 0,
                ball_three = 0, 
                frame_score = 0, 
                isSpare = False, 
                isStrike = False):
                
        self.ball_one = ball_one 
        self.ball_two = ball_two
        self.ball_three = ball_three
        self.frame_score = frame_score

        self.isSpare = isSpare
        self.isStrike = isStrike

    def roll_ball(self, remaining_pins = 10):
        valid_roll = False
        while not valid_roll:
            pins_input = input("Input 0-{}: ".format(remaining_pins))

            try:
                pins = int(pins_input)
            
                if 0 <= pins <= 10:
                    valid_roll = True
                else:
                    print("Invalid Roll!!")

            except ValueError:
                print("Invalid Roll!!!")


            
        return pins

    def calculate_frame_score(self):
        self.frame_score += self.ball_one + self.ball_two + self.ball_three
        
def play_game():
    game = Game()

    for frame_counter in range(1, 11):
        print("Frame {}".format(frame_counter))
        frame = Frame()
        print("First Ball")
        frame.ball_one = frame.roll_ball()

        #if pins remain on second ball or a strike gained on the final frame
        if frame_counter == 10 or frame.ball_one < 10:
            print("Second Ball")
            pins_remaining = 10-frame.ball_one if frame_counter < 10 or 0 < 10-frame.ball_one < 10 else 10
            frame.ball_two = frame.roll_ball(pins_remaining)
        
        #if spare or strike was gained on the 2nd ball of the final frame
        if frame_counter == 10 and ((frame.ball_two == 10) or (frame.ball_one + frame.ball_two == 10)):
            print("Third Ball")
            frame.ball_three = frame.roll_ball()
        
        if( frame.ball_one == 10):
            frame.isStrike = True
        elif( frame.ball_one + frame.ball_two == 10):
            frame.isSpare = True

        #calculate score for current frame
        frame.calculate_frame_score()

        game.add_frame(frame)
        print('\n')

    game.calculate_score()
    print("You scored a {} this game.".format(game.total_score))

if __name__ == "__main__":
    play_game()