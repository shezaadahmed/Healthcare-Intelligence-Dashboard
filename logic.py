def analyze(row):
    alerts = []
    recommendations = []

    bed_ratio = row["beds_available"] / row["total_beds"]

    # Alerts
    if bed_ratio < 0.1:
        alerts.append("🚨 Critical bed shortage")
    elif bed_ratio < 0.2:
        alerts.append("⚠️ Low bed capacity")

    if row["critical_patients"] > 20:
        alerts.append("🚨 High critical patient load")

    if row["incoming_patients"] > row["beds_available"]:
        alerts.append("⚠️ Incoming patients exceed capacity")

    # Recommendations
    if bed_ratio < 0.2:
        recommendations.append("Transfer stable patients to nearby hospitals")

    if row["critical_patients"] > 20:
        recommendations.append("Allocate additional ICU staff")

    if row["incoming_patients"] > row["beds_available"]:
        recommendations.append("Set up temporary triage / emergency beds")

    # Confidence score (simple but impressive)
    score = 100 - (len(alerts) * 15)

    return alerts, recommendations, max(score, 50)