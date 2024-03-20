import os

URL_CALLBACK_EXEDOC = os.environ.get("BASE_URL", "http://localhost:8000") + "/api/callbackexedoc/"
EMISOR_DOCUMENTO_EXEDOC = os.environ.get("EMISOR_DOCUMENTO_EXEDOC", "seim")

# GDMTT / Exedoc
URL_GDMTT = os.environ.get("URL_GDMTT", "http://example.com")
URL_EXECDOC = os.environ.get("URL_EXEDOC", "http://example.com")
METODO_FIRMA_EXEDOC = os.environ.get("METODO_FIRMA_EXEDOC", "")
METODO_DOCUMENTO_EXEDOC = os.environ.get("METODO_DOCUMENTO_EXEDOC", "")
URL_FIRMA_EXEDOC = f"{URL_EXECDOC}{METODO_FIRMA_EXEDOC}"
URL_DOCUMENTO_EXEDOC = f"{URL_EXECDOC}{METODO_DOCUMENTO_EXEDOC}"