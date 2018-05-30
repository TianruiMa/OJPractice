class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # move_dict = {'U':0,'D':0,'L':0,'R':0}
        # # move_dict = {'U':1,'D':-1,'L':3,'R':-3}
        # # res = 0
        # for m in moves:
        #     move_dict[m]+=1
        # return move_dict['U'] == move_dict['D'] and move_dict['L'] == move_dict['R']
        return (moves.count('U')==moves.count('D')) and (moves.count('L')==moves.count('R'))