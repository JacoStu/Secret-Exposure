import os

shared_secret = os.environ.get('API_KEY')

if shared_secret == "This_is_my_api_key":
    print("Accesso verificato tramite Shared Secret.")
    
    db_path = "./production_data/database.txt"
    
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"DATABASE ELIMINATO: {db_path} è stato rimosso con successo.")
    else:
        print("Errore: Database non trovato, ma il token era valido.")
else:
    print("Token non valido per operazioni distruttive.")
