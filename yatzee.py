
def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num 

def yahtzee_score_calc(lst):
    total = 0
    
    for i in range(len(lst)):
        turn = lst[i]
        
        if i in range(0, 6): # 1-6
            total += (i+1) * turn.count(i+1)
        
        if i == 6: # add 35
            if total >= 63:
                total += 35
        
        if i == 6 or i == 7: # Three of a kind and Four of a kind
            m = most_frequent(turn)
            m_c = turn.count(m)
            if m_c >= i-3:
                total += m * m_c
                
        if i == 8: # Full house
            m = most_frequent(turn)
            if turn.count(m) == 3:
                s = set(turn)
                s.remove(m)
                if len(s) == 1:
                    total += 25
    
        if i == 9: # Lower straight
            s = ""
            for i in set(turn):
                s += str(i)
            if "1234" in s or "2345" in s or "3456" in s:
                total += 30
        
        if i == 10:
            if sum(set(turn)) in [15, 20]:
                total += 40

        if i == 11:
            if len(set(turn)) == 1:
                total += 50
                
        if i == 12:
            total += sum(turn)
        
    
    return total




res = yahtzee_score_calc([
  [1, 3, 1, 1, 2], # Aces
  [1, 2, 4, 5, 6], # Twos
  [6, 3, 4, 3, 4], # Threes
  [3, 1, 1, 4, 4], # Fours
  [5, 5, 5, 5, 3], # Fives
  [6, 2, 6, 6, 6], # Sixes
  [1, 4, 4, 2, 1], # Three of a Kind
  [3, 3, 3, 3, 3], # Four of a Kind
  [2, 2, 1, 1, 2], # Full House
  [6, 1, 2, 3, 4], # Lower Straight
  [2, 3, 5, 4, 1], # Higher Straight
  [4, 4, 4, 4, 4], # Yahtzee
  [3, 3, 4, 5, 6], # Chance
])

print(res)
