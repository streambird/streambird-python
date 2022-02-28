from typing import Dict, Optional


class MagicLinks:
    """MagicLinks class, containing magic links information."""

    def __init__(self, client):
        self._client = client
        self.email = Email(client)
        

class Email:
    def __init__(self, client):
        self._client = client

    def login_or_create(
        self,
        email: str,
        login_redirect_url: Optional[str] = None,
        registration_redirect_url: Optional[str] = None,
        login_expires_in: Optional[int] = None,
        registration_expires_in: Optional[int] = None,
        device_fingerprint: Optional[Dict] = None,
        requires_verification: Optional[bool] = False,
    ):

        req = {
           'email': email,
           'requires_verification': requires_verification,
        }
        if login_redirect_url:
            req['login_redirect_url'] = login_redirect_url
        if registration_expires_in:
            req['registration_expires_in'] = registration_expires_in
        if login_expires_in:
            req['login_expires_in'] = login_expires_in
        if registration_expires_in:
            req['registration_expires_in'] = registration_expires_in
        if device_fingerprint:
            req['device_fingerprint'] = device_fingerprint

        return self._client.api.post_request('auth/magic_links/email/login_or_create', body=req)