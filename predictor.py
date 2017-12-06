import sqlalchemy
from sqlalchemy import create_engine
from mbti_no_pos import map_strings

class Predictor:
    db_string = 'postgres://secretuser:secretpassword@localhost:5432/mbti'
    
    # Here are probabilities of people in each of 4 different categories
    p_probs = {'I': 0.769567, 'E': 0.230433, 'N': 0.862017, 'S': 0.137983, 'F': 0.541095, 'T': 0.458905, 'P': 0.60415, 'J': 0.39585}
    
    # Probabilities of values in each of 4 categories
    v_probs = {'I': 0.771512, 'E': 0.228488, 'N': 0.895135, 'S': 0.104865, 'F': 0.542246, 'T': 0.457754, 'P': 0.601053, 'J': 0.398947}
    
    def __init__(self):
        self.db = create_engine(self.db_string)
    
    def run(self, text):
        words, length = map_strings(text)
        
        # no valid words were found
        if length == 0:
            return None
        
        sql_template = 'SELECT SUM("I") AS I, SUM("E") AS E, SUM("N") AS N, SUM("S") AS S, SUM("T") AS T, SUM("F") AS F, SUM("J") AS J, SUM("P") AS P FROM vocabulary WHERE word = ANY( :user_vocab )'
        
        result = self.db.execute(sqlalchemy.text(sql_template), {'user_vocab': words})
        
        # lets get and format data from DB
        row = result.first()
        i, e, n, s, f, t, p, j = row
        result.close()

        # if completely trash text was provided
        if i == None:
            return None        
        i, e, n, s, f, t, p, j = int(i), int(e), int(n), int(s), int(f), int(t), int(p), int(j)
        
        # probabilities calculated based on provided text. +1 was added to denominator to avoid division by zero
        Pi = i/(i+e+1)
        Pn = n/(n+s+1)
        Pf = f/(f+t+1)
        Pp = p/(p+j+1)
        
        # In training set we have mixed group of people with both E and I. 
        # Since person we are testing belongs to one group only then our testing set is more focused
        # on specific words and probability of these words usage should be higher than in mixed group.
        # So we have to compare values of word usage probability for testing person
        # with same probability for group and to choose group that have smaller values of probability 
        # for same words
        
        # mask creation based on calculated probabilities
        result = "I" if Pi >= self.v_probs['I'] else "E"
        result += "N" if Pn >= self.v_probs['N'] else "S"
        result += "F" if Pf >= self.v_probs['F'] else "T"
        result += "P" if Pp >= self.v_probs['P'] else "J"
        
        return result
