export function priorityForRisk(risk,correlated=false){
 const score=Math.min(100,Number(risk||0)+(correlated?5:0));
 return score>=85?"P1 - Critical":score>=65?"P2 - High":score>=35?"P3 - Medium":"P4 - Low";
}
