class Solution(object):
    def pushDominoes(self, dominoes):
        # Fill this in.
        '''
        1. check 'R.L', keep it unChange
        2. replace '.L' to 'LL'
        3. replace 'R.' to 'RR'
        :param dominoes:
        :return:
        '''
        while True:
            new_dominoes = dominoes.replace('R.L', '|')\
                .replace('.L', 'LL').replace('R.', 'RR')\
                .replace('|', 'R.L')
            if new_dominoes == dominoes:
                break
            else:
                dominoes = new_dominoes

        return dominoes


print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR

print(Solution().pushDominoes('.L.R...LR..L..'))
# LL.RR.LLRRLL..

print(Solution().pushDominoes('RR.L'))