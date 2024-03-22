from typing import Any, Dict, List, Optional

from dh_potluck.email.mandrill_email_client import (
    MandrillEmailClient,
    MandrillMergeLanguage,
    MandrillRecipient,
)


class EmailService(object):
    _email_client: Optional[MandrillEmailClient] = None

    @classmethod
    def _get_email_client(cls):
        if not cls._email_client:
            cls._email_client = MandrillEmailClient()
        return cls._email_client

    @classmethod
    def send_email_template(
        cls,
        recipients: List[MandrillRecipient],
        template_name: str,
        template_vars: List[Dict[str, str]],
        subject: Optional[str] = None,
        merge_language: Optional[MandrillMergeLanguage] = None,
        template_vars_overrides_for_recipients: Optional[List[Dict[str, Any]]] = None,
        preserve_recipients: bool = True,
    ) -> None:
        try:
            cls._get_email_client().send_email_template(
                recipients,
                template_name,
                template_vars,
                subject=subject,
                merge_language=merge_language,
                template_vars_overrides_for_recipients=template_vars_overrides_for_recipients,
                preserve_recipients=preserve_recipients,
            )
        except Exception as e:
            raise EmailServiceException(
                message=f'Error occurred while sending email template: {str(e)}'
            )

    @classmethod
    def send_email_html(
        cls,
        recipients: List[MandrillRecipient],
        subject: Optional[str] = None,
        html: Optional[str] = None,
        preserve_recipients: bool = True,
    ) -> None:
        try:
            cls._get_email_client().send_email_html(
                recipients, subject=subject, html=html, preserve_recipients=preserve_recipients
            )
        except Exception as e:
            raise EmailServiceException(
                message=f'Error occurred while sending html email: {str(e)}'
            )


class EmailServiceException(Exception):
    def __init__(self, message: str = 'Error occurred while sending email.') -> None:
        self.message = message
        super().__init__(self.message)
