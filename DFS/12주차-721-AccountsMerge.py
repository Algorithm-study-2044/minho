from typing import List

## 개느림
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        answer = []
        invalid = set()
        for i in range(len(accounts)):
            if i in invalid:
                continue
            emails = set(accounts[i][1:])
            j = i+1
            while j < len(accounts):
                if j in invalid:
                    j += 1
                    continue
                if accounts[j][0] == accounts[i][0]:
                    flag = 0
                    for e in accounts[j][1:]:
                        if e in emails:
                            flag = 1
                            break
                    if flag:
                        for e in accounts[j][1:]:
                            emails.add(e)
                        invalid.add(j)
                        j = i+1
                        continue
                j += 1
            answer.append([accounts[i][0]] + sorted(list(emails)))
        
        return answer
    

## Solution - using id <Union Find>
import collections

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_id = collections.defaultdict(list)
        visited = [False] * len(accounts)
        answer = []

        # Create a graph
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email_to_id[account[j]].append(i)
        
        # DFS
        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True
            for email in accounts[i][1:]:
                emails.add(email)
                for neighbor in email_to_id[email]:
                    dfs(neighbor, emails)
        
        # Implement DFS
        for i in range(len(accounts)):
            if visited[i]:
                continue
            name, emails = accounts[i][0], set()
            dfs(i, emails)
            answer.append([name] + sorted(emails))
        
        return answer
