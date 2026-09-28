export function calculateSocMetrics(alerts,incidents,feedback=[]){
 const n=alerts.length||1;
 return {
  alert_volume:alerts.length,
  critical_alerts:alerts.filter(a=>a.ai_risk_level==="Critical").length,
  high_alerts:alerts.filter(a=>a.ai_risk_level==="High").length,
  average_risk:Number((alerts.reduce((s,a)=>s+Number(a.ai_risk_score||0),0)/n).toFixed(2)),
  incident_volume:incidents.length,
  open_incidents:incidents.filter(i=>i.case_status!=="Closed").length,
  escalation_rate:incidents.length?Number((incidents.filter(i=>String(i.priority).startsWith("P1")).length/incidents.length).toFixed(4)):0,
  feedback_count:feedback.length,
  false_positive_rate:feedback.length?Number((feedback.filter(x=>x.verdict==="False Positive").length/feedback.length).toFixed(4)):0
 };
}
