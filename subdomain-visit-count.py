class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        D = {}
        for cpstr in cpdomains:
            times, domain = cpstr.split()
            D[domain] = D.get(domain, 0) + int(times)
            for i in range(len(domain)):
                if domain[i] == '.':
                    D[domain[i+1:]] = D.get(domain[i+1:], 0) + int(times)
        return [
            "%d %s"%(times, domain) for domain, times in D.items()
        ]