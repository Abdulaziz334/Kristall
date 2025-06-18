# security/auth.py

AUTHORIZED_KEYS = {
    "admin": "KRISTALL_ADMIN_TOKEN_2025",
    "metalifex": "METALIFEX_INTEGRATION_TOKEN",
    "base_manager_1": "BASE_MANAGER_TKN_001",
    "ai_module": "AI_ROUTER_ACCESS_KEY"
}

def is_authorized(provided_key):
    return provided_key in AUTHORIZED_KEYS.values()