"""Transparent operational alert-correlation engine; not an investigation-reasoning system."""
from collections import defaultdict

def correlate(alerts):
    groups=[]
    seen=set()
    for i,a in enumerate(alerts):
        if a.get("alert_id") in seen: continue
        ids=[a.get("alert_id")]
        for j,b in enumerate(alerts):
            if i==j: continue
            same_source=a.get("source_ip") and a.get("source_ip")==b.get("source_ip")
            same_host=a.get("target_host") and a.get("target_host")==b.get("target_host")
            same_user=a.get("username") and a.get("username")==b.get("username")
            same_mitre=a.get("mitre_id") and a.get("mitre_id")==b.get("mitre_id")
            if sum(bool(x) for x in (same_source,same_host,same_user,same_mitre))>=1:
                ids.append(b.get("alert_id"))
        ids=list(dict.fromkeys(ids))
        seen.update(ids)
        groups.append({"group_id":f"ACT-{len(groups)+1:03d}","alert_ids":ids,"count":len(ids)})
    return groups
