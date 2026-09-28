export function sigmoid(z){const x=Math.max(-30,Math.min(30,z));return 1/(1+Math.exp(-x));}
export function normalizeAlert(alert, allAlerts=[]){
 const sev={critical:1,high:.8,medium:.55,low:.25}[String(alert.severity||"low").toLowerCase()]??.25;
 const failed=Math.min(1,Number(alert.failed_attempts||0)/100);
 const ip=alert.source_ip||"";
 const repetition=Math.min(1,allAlerts.filter(a=>(a.source_ip||"")===ip).length/3);
 const tacticRisk=["credential access","privilege escalation","persistence","defense evasion","exfiltration","command and control"].includes(String(alert.mitre_tactic||"").toLowerCase())?1:
   ["discovery","reconnaissance","initial access","execution"].includes(String(alert.mitre_tactic||"").toLowerCase())?.55:.2;
 const eventRisk={privilege_escalation:1,authentication_failure:.65,network_scan:.55}[String(alert.event_type||"").toLowerCase()]??.2;
 return [
  Math.min(1,Number(alert.rule_level||0)/12),sev,alert.successful_login_after_failures===true?1:0,
  failed,tacticRisk,repetition,eventRisk,Number(alert.anomaly_signal??0)
 ];
}
export function mlRisk(alert,model,allAlerts=[]){
 const x=normalizeAlert(alert,allAlerts);
 const z=model.intercept+model.coefficients.reduce((s,c,i)=>s+c*x[i],0);
 const probability=sigmoid(z);
 const risk=Math.round(probability*100);
 const confidence=Math.abs(probability-.5)*2;
 return {ml_probability:Number(probability.toFixed(4)),ai_risk_score:risk,confidence:Number(confidence.toFixed(4)),model_version:model.model_version,model_name:model.model_name,features:x};
}
export function hybridRisk(deterministic,ml){
 const finalRisk=Math.round(.55*deterministic+.45*ml.ai_risk_score);
 const level=finalRisk>=85?"Critical":finalRisk>=65?"High":finalRisk>=35?"Medium":"Low";
 return {final_risk:finalRisk,final_level:level,deterministic_risk:deterministic,ml_probability:ml.ml_probability,confidence:ml.confidence};
}
