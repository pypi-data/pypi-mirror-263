from datetime import timedelta

import boto3
import pyotp
from RPA.Browser.Selenium import Selenium


class AWS:
    def __init__(self, aws_credentials, okta_credentials):
        self.session = boto3.Session()
        self.__aws_credentials = aws_credentials
        self.__okta_credentials = okta_credentials
        self.__login()

    def __login(self):
        sso_client = self.session.client(
            "sso-oidc",
            region_name="us-east-1",
        )

        register_response = sso_client.register_client(clientName="Automation-Engineer", clientType="public")

        sso_device_auth_response = sso_client.start_device_authorization(
            clientId=register_response["clientId"],
            clientSecret=register_response["clientSecret"],
            startUrl="https://thoughtfulautomation.awsapps.com/start#/",
        )

        self.__okta_login(sso_device_auth_response["verificationUriComplete"])

        token_response = sso_client.create_token(
            grantType="urn:ietf:params:oauth:grant-type:device_code",
            clientId=register_response["clientId"],
            clientSecret=register_response["clientSecret"],
            deviceCode=sso_device_auth_response["deviceCode"],
        )

        sso = self.session.client("sso", region_name="us-east-1")
        account_roles = sso.list_account_roles(
            accessToken=token_response["accessToken"], accountId=self.__aws_credentials["account_id"]
        )
        roles = account_roles["roleList"]
        role = roles[0]
        role_creds = sso.get_role_credentials(
            roleName=role["roleName"],
            accountId=role["accountId"],
            accessToken=token_response["accessToken"],
        )

        self.session = boto3.Session(
            region_name="us-east-1",
            aws_access_key_id=role_creds["roleCredentials"]["accessKeyId"],
            aws_secret_access_key=role_creds["roleCredentials"]["secretAccessKey"],
            aws_session_token=role_creds["roleCredentials"]["sessionToken"],
        )

    def __okta_login(self, verification_url):
        selenium_wait_time = 30
        browser = Selenium()
        browser.open_available_browser(url=verification_url, headless=True)
        try:
            browser.wait_until_element_is_visible(
                '//button[text() ="Confirm and continue"]', timedelta(seconds=selenium_wait_time)
            )
            browser.click_element('xpath://button[text() ="Confirm and continue"]')
            username_id = "id:okta-signin-username"
            browser.wait_until_element_is_enabled(username_id, timedelta(seconds=selenium_wait_time + 15))
            current_username = browser.get_text(username_id)
            username = str(self.__okta_credentials["username"]).split("@")[0]
            if current_username != username:
                browser.input_text(username_id, username)

            if not browser.is_checkbox_selected('//input[@name="remember"]'):
                browser.click_element_when_visible('xpath://div[@class="custom-checkbox"]')

            browser.click_button("id:okta-signin-submit")
            answer_input = "name:answer"
            browser.wait_until_element_is_enabled(answer_input, timedelta(seconds=selenium_wait_time))

            totp = pyotp.TOTP(self.__okta_credentials["totp"])
            otp_code = totp.now()
            browser.input_text(answer_input, otp_code)
            browser.click_element('xpath://input[@class="button button-primary"]')

            login_button = "id:cli_login_button"
            browser.wait_until_element_is_enabled(login_button, timedelta(seconds=selenium_wait_time))
            browser.click_element_when_visible(login_button)
            browser.wait_until_element_is_visible("xpath://b[.='Request approved']")
        except Exception as e:
            raise e
        finally:
            browser.close_all_browsers()
