from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = {}
        email_to_name = {}

        def find(email):
            if parent[email] != email:
                parent[email] = find(parent[email])
            return parent[email]

        def union(email1, email2):
            p1 = find(email1)
            p2 = find(email2)

            if p1 == p2:
                return

            if rank[p1] < rank[p2]:
                parent[p1] = p2
            elif rank[p1] > rank[p2]:
                parent[p2] = p1
            else:
                parent[p2] = p1
                rank[p1] += 1

        # 1. Create nodes and connect emails
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                    rank[email] = 0

                email_to_name[email] = name

                # Connect every email to the first email
                union(first_email, email)

        # 2. Group emails by their root
        groups = defaultdict(list)

        for email in parent:
            root = find(email)
            groups[root].append(email)

        # 3. Build answer
        result = []

        for root, emails in groups.items():
            name = email_to_name[root]
            result.append([name] + sorted(emails))

        return result