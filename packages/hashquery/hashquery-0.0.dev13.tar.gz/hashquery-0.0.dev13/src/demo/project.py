from ..hashboard_api.api import HashboardAPI
from ..hashboard_api.credentials import HashboardAccessKeyClientCredentials
from ..hashboard_api.project_manifest import ProjectManifest

demo_creds = HashboardAccessKeyClientCredentials.from_encoded_key(
    "eyJhY2Nlc3Nfa2V5X2lkIjoiNWM3YTE0ZWMtYWNkNi00YTc0LTljNzItN2FlNzRkY2IzMWZkIiwiYWNjZXNzX2tleV90b2tlbiI6IkxxMXhVZ3RPa1VmdHpyTUk5SU1xRGdBdExya1d4VFNXIiwicHJvamVjdF9pZCI6ImNzTFFXS2NUOHMzbWotdUoifQ=="
)
HashboardAPI.register_project(
    credentials=demo_creds,
    base_uri="https://hashquery.dev",
)

demo_project = ProjectManifest(demo_creds.project_id)
