def detect_anomalies(df, condition_func, message_template):
    """
    Détecte des anomalies dans un DataFrame selon une condition personnalisée.

    Args:
        df (pd.DataFrame): La base de données.
        condition_func (callable): Fonction prenant (row) et retournant True si anomalie.
        message_template (str): Modèle du message, utilisant les noms des colonnes comme variables.

    Returns:
        list: Liste des messages d'anomalies détectées.
    """
    anomalies=""
    i=0
    for _, row in df.iterrows():
        if condition_func(row):
            if i == 0 :
                anomalies =  message_template.format(**row)
                i=1
            else :
                anomalies = anomalies + "\n" + message_template.format(**row) 
            
    
    return anomalies

# - full erros check 
from datetime import datetime
anomalies = []
anomalies.append("\n🧩 **Incohérences - Pre-inclusion**\n")
condition = lambda r: r["Age_col_name"] > 47
message = "⚠️ Âge trop élevé pour ID={id_col_name} : {Age_col_name} ans"
anomalies.append(detect_anomalies(dataset1, condition, message))
