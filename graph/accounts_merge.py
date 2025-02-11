import collections
from typing import List


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    email_account_map = collections.defaultdict(list)
    for i, account in enumerate(accounts):
        for email in account[1:]:
            email_account_map[email].append(i)

    merged_accounts = []
    visited_accounts = set()

    def dfs(i, emails):
        if i in visited_accounts:
            return
        visited_accounts.add(i)
        for email in accounts[i][1:]:
            emails.add(email)
            for account_index in email_account_map[email]:
                dfs(account_index, emails)

    for i, account in enumerate(accounts):
        emails = set()
        if i not in visited_accounts:
            dfs(i, emails)
            name = account[0]
            merged_accounts.append([name] + sorted(emails))

    return merged_accounts


print(
    accountsMerge(
        [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
         ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])
)
