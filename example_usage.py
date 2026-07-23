from client import AutomatedSeoSiteHealthAuditorClient

def main():
    client = AutomatedSeoSiteHealthAuditorClient()
    res = client.audit_domain("example.com", crawl_depth=3)
    print(f"Health Score: {res['health_score']}/100")
    print(res["audit_summary"])
    print("Critical Issues:")
    for issue in res["critical_issues"]:
        print(f"  [{issue['severity']}] {issue['issue']}")

if __name__ == "__main__":
    main()
