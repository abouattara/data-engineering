

# Notification de fin
notification.notify(
    title="Téléchargements terminés",
    message="Tous les téléchargements ont réussi !" if telechargements_reussis else "Certains téléchargements ont échoué.",
    timeout=10
)
