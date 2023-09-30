#- Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.#
class Bowler:
    def __init__(self):
        self.wickets_taken = 0
        self.economy = 0.0
        self.hattricks = 0
        self.bowling_rank = 0
    def get_bowl(self,wt,ec,ht,bor):
        self.wickets_taken = wt
        self.economy = wc
        self.hattricks = ht
        self.bowling_rank = bor
    def disp_bowl(self):
        print "Wickets Taken:",self.wickets_taken
        print "Economy:",self.economy
        print "Hattricks:",self.hattricks
        print "Bowling Rank:",self.bowling_rank
      class Batsman:
    def __init__(self):
        self.strike_rate = 0.0
        self.total_runs = 0
        self.highest_score = 0
        self.batting_rank = 0
    def get_bat(self,sr,tr,hs,br):
        self.strike_rate = sr
        self.total_runs = tr
        self.highest_score = hs
        self.batting_rank = br
    def disp_bat(self):
        print "Strike Rate:",self.strike_rate
        print "Total Runs:",self.total_runs
        print "Highest Score:",self.highest_score
        print "Batting Rank:",self.batting_rank
class AllRounder(Batsman,Bowler):
    def __init__(self):
        Batsman.__init__(self)
        Bowler.__init__(self)
        self.allrounder_rank = 0
    def get_all(self,sr,tr,hs,br,wt,ec,ht,bor,ar):
        Batsman.get_bat(self,sr,tr,hs,br)
        Bowler.get_bowl(self,wt,ec,ht,bor)
        self.allrounder_rank = 
    def disp_all(self):
        self.disp_bat()
        self.disp_bowl()
        print "All Rounder Rank:",self.allrounder_rank