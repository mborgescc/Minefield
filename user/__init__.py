from internal import Field


class Interface:

    MINE = True

    def __init__(self):
        self.size_dict = {
            0: "EXTRA_SMALL",
            1: "SMALL",
            2: "LARGE",
            3: "EXTRA_LARGE",
            4: "WORLD",
            5: "GALAXY",
        }
        self.level_dict = {
            0: "EASY",
            1: "MEDIUM",
            2: "HARD",
            3: "EXTRA_HARD",
            4: "EXTREME",
            5: "IMPOSSIBLE",
        }

    def run(self):
        print "##################################################"
        print "## WELCOME TO MAURICIO'S AND DAVID'S MINEFIELD! ##"
        print "##################################################"

        while True:
            print ""
            print "Please, choose the size of the field:"
            print " > 0 - EXTRA SMALL"
            print " > 1 - SMALL"
            print " > 2 - LARGE"
            print " > 3 - EXTRA LARGE"
            print " > 4 - WORLD"
            print " > 5 - GALAXY"

            size = input()
            if size in self.size_dict:
                size = self.size_dict[size]
                break
            print "This is not a choice. Please, try again."

        while True:
            print ""
            print "Please, choose the difficulty level:"
            print " > 0 - EASY"
            print " > 1 - MEDIUM"
            print " > 2 - HARD"
            print " > 3 - EXTRA HARD"
            print " > 4 - EXTREME"
            print " > 5 - IMPOSSIBLE"

            level = input()
            if level in self.level_dict:
                level = self.level_dict[level]
                break
            print "This is not a choice. Please, try again."

        print "Great! Please, wait a little while we prepare your game..."

        field = self.prepare_game(size, level)

        print "We are ready to start!"

        game_over = False
        while not game_over:
            self.draw(field)
            move = list
            move.append(input("Choose 'i' number: "))
            move.append(input("Choose 'j' number: "))
            win, game_over = self.check(move, field)
        self.draw(field)

        if win:
            print "You have won!"
        else:
            print "Oh no, a mine... Good luck on next time!"

    @staticmethod
    def prepare_game(size, level):
        return Field(size, level)

    @staticmethod
    def draw(field):
        print "  ",
        for j in xrange(field.size):
            print " {} ".format(j+1),
        print ""
        for i in xrange(field.size):
            print "{} ".format(i+1),
            for j in xrange(field.size):
                if field.squares[i][j] == "CLOSED":
                    print " + ",
                elif field.squares[i][j] == "OPEN":
                    print " {} ".format(field.squares[i][j].number),
                elif field.squares[i][j] == "MINE":
                    print " # ",
                else:
                    print " ? ",
            print ""
        print "\n"

    def check(self, move, field):
        return True, False
