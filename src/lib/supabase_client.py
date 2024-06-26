from supabase import create_client, Client


class SupabaseClient:
    _instance = None

    def __new__(cls, url: str, key: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = create_client(url, key)
        return cls._instance

    @property
    def get_client(self) -> Client:
        return self.client
