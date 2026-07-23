class AutomatedSeoSiteHealthAuditorClient:
    def audit_domain(self, target_domain: str, crawl_depth: int = 2) -> dict:
        issues = [
            {"issue": "Missing meta description on /blog/ai-agent", "severity": "HIGH"},
            {"issue": "3 pages missing H1 tag", "severity": "MEDIUM"},
            {"issue": "Unoptimized PNG images > 2MB", "severity": "LOW"}
        ]
        return {
            "health_score": 88.5,
            "critical_issues": issues,
            "audit_summary": f"Audited {target_domain} (Depth: {crawl_depth}). Found {len(issues)} issues across 200 checks."
        }
