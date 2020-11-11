class math:
       def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
        
    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)
