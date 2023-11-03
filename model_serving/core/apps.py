from django.apps import AppConfig
from django.conf import settings
import pickle

with open(f'{settings.BASE_DIR}/model.pkl', 'rb') as file:
    pickle_model = pickle.load(file)

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    model = pickle_model
