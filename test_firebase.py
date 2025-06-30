import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Prueba: escribe y lee
doc_ref = db.collection("test").document("prueba")
doc_ref.set({"mensaje": "Hola Firebase desde FastAPI!"})

doc = doc_ref.get()
print(doc.to_dict())
