class Solution(object):
    def dot3(self,ip):
        if len(ip.split("."))==4:
            return True
        return False
    def invalidIP(self,ip):

        v4=ip.split(".")
        octate=0
        if v4[-1]=="":
            octate=v4[-2]
        else:
            octate=v4[-1]
        #print v4,"octate:%r"%octate
        try:
            o=int(octate)
            #print "octate=%d"%o
        except:
            return True
        if o>255:
            return True
        return False

    def validIp(self,ip):

        if '.' in ip:
            v4=ip.split(".")
            if len(v4)!=4: return False

            for octate in v4:
                found=0
                i=0
                if not octate or len(octate)>3:
                    return False
                if octate[0]=="0" and len(octate)>1:
                    return False
                try:
                    o=int(octate)
                except:
                    return False
                if o<0 or o>255:
                    return False
            return True
        else:
            return False

    def helper(self,s,ip,out):

        if self.validIp(ip) and len(s)==0:
            out.append(ip)
            return

        #Found 3 dots and still invalid
        if ((len(ip)>0) and self.invalidIP(ip)) or len(s)==0:
            #print self.invalidIP(ip)
            return

        self.helper(s[1:],ip+s[0]+".",out)
        self.helper(s[1:],ip+s[0],out)

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        out=[]
        ip=""
        if len(s)>12:
            return []
        self.helper(s,ip,out)
        return out
