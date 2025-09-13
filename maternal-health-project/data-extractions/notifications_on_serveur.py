from plyer import notification

# telechargements_reussis boolean, use to noticed if dataset download successfully

# Notification de fin
notification.notify(
    title="Téléchargements terminés",
    message="Tous les téléchargements ont réussi !" if telechargements_reussis else "Certains téléchargements ont échoué.",
    timeout=10
)
