import database
import config

print("=== Configuration ===")
print("URL :", config.SUPABASE_URL)
print("Jours :", config.SYNC_JOURS)

print("\n=== Synchro ===")
resultat = database.sync_pannes_depuis_supabase()
print("Résultat :", resultat)

if resultat["succes"]:
    print(f"\n✅ Synchro OK : {resultat['importees']} importée(s), "
          f"{resultat['ignorees']} ignorée(s)")
else:
    print(f"\n❌ Échec : {resultat['erreur']}")

print("\n=== Pannes locales après synchro ===")
pannes = database.get_pannes_filtrees()
print(f"{len(pannes)} panne(s) :")
for p in pannes[-5:]:
    print(f"  - {p['wo']} • {p['date_panne']} {p['heure_panne'] or ''} • {p['machine']}")

print("\ntest_sync OK")