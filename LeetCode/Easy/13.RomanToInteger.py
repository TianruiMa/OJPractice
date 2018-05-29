class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        A = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        B = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        C = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        D = ['','M','MM','MMM']
        return D[data/1000]+C[data%1000/100]+B[data%100/10]+A[data%10]