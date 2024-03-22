import bioflex
from bioturing_connector.bbrowserx_connector import BBrowserXConnector
from bioturing_connector.lens_bulk_connector import LensBulkConnector
from bioturing_connector.lens_sc_connector import LensSCConnector
from .util import empty, get_settings, get_studio_settings

class EConnector:
    """Create a connector object to submit/get data from BioColab
    """

    def __init__(self, bioflex_token: str = "", public_token: str = "", 
        private_host: str = "", private_token: str = "",
        studio_host: str = "http://127.0.0.1:11123", 
        studio_token: str = "", studio_email: str = "",
        use_token_from_api = False, studio_token_idx: int = 0,
    ):
        """
          Args:
            bioflex_token:
                The API token to access BioFlex
            public_token:
                The API token to verify authority. Generated in https://talk2data.bioturing.com
            private_host:
                The URL of the BBrowserX server, only supports HTTPS connection
                Example: https://bbrowserx.bioturing.com
            private_token:
                The API token to verify authority. Generated in-app.
            studio_host:
                The URL of the BioStudio server, only supports HTTPS connection
                Example: https://studio.bioturing.com
            studio_token:
                The API token to verify authority. Generated in-app.
            studio_email:
                The API email.
            use_token_from_api:
                Use token from API.
            studio_token_idx:
                The API token index.
        """
        self.__bioflex_token = bioflex_token
        self.__public_token = public_token
        self.__private_host = private_host
        self.__private_token = private_token
        self.__studio_host = studio_host
        self.__studio_token = studio_token
        self.__studio_email = studio_email
        self.__use_token_from_api = use_token_from_api
        self.__studio_token_idx = studio_token_idx

    def get_settings(self):
        if self.__use_token_from_api == False:
            return get_settings()

        return get_studio_settings(
            self.__studio_host,
            self.__studio_token,
            self.__studio_email,
            self.__studio_token_idx,
        )

    """
      Args:
        private_host:
          The URL of the BBrowserX private server, only supports HTTPS connection
          Example: https://bbrowserx.your_domain
          If empty, BioStudio will retrieve this information from your settings.
        private_token:
          The API token to verify authority. Generated in-app.
          If empty, BioStudio will retrieve this information from your settings.
        ssl: SSL mode
    """

    def get_bbrowserx(
        self,
        private_host: str = "",
        private_token: str = "",
        ssl: bool = True
    ):
        host = private_host
        if empty(host) == True:
            host = self.__private_host

        token = private_token
        if empty(token) == True:
            token = self.__private_token

        if (empty(host) == True) or (empty(token) == True):
            try:
                contents = self.get_settings()
                if "bio_bbx_private_domain" in contents:
                    host = contents["bio_bbx_private_domain"]
                if "bio_bbx_private_key" in contents:
                    token = contents["bio_bbx_private_key"]
            except Exception as e:
                raise e

        if (empty(host) == True) or (empty(token) == True):
            raise Exception("Empty BBrowserX setting (Host - Token)")

        return BBrowserXConnector(
            host=host,
            token=token,
            ssl=ssl
        )

    """
      Args:
        private_host:
          The URL of the BBrowserX private server, only supports HTTPS connection
          Example: https://bbrowserx.your_domain
          If empty, BioStudio will retrieve this information from your settings.
        private_token:
          The API token to verify authority. Generated in-app.
          If empty, BioStudio will retrieve this information from your settings.
        ssl: SSL mode
    """

    def get_lensbulk(
        self,
        private_host: str = "",
        private_token: str = "",
        ssl: bool = True
    ):
        host = private_host
        if empty(host) == True:
            host = self.__private_host

        token = private_token
        if empty(token) == True:
            token = self.__private_token

        if (empty(host) == True) or (empty(token) == True):
            try:
                contents = self.get_settings()
                if "bio_bbx_private_domain" in contents:
                    host = contents["bio_bbx_private_domain"]
                if "bio_bbx_private_key" in contents:
                    token = contents["bio_bbx_private_key"]
            except Exception as e:
                raise e

        if (empty(host) == True) or (empty(token) == True):
            raise Exception("Empty BBrowserX setting (Host - Token)")

        return LensBulkConnector(
            host=host,
            token=token,
            ssl=ssl
        )

    """
      Args:
        private_host:
          The URL of the BBrowserX private server, only supports HTTPS connection
          Example: https://bbrowserx.your_domain
          If empty, BioStudio will retrieve this information from your settings.
        private_token:
          The API token to verify authority. Generated in-app.
          If empty, BioStudio will retrieve this information from your settings.
        ssl: SSL mode
    """

    def get_lenssc(
        self,
        private_host: str = "",
        private_token: str = "",
        ssl: bool = True
    ):
        host = private_host
        if empty(host) == True:
            host = self.__private_host

        token = private_token
        if empty(token) == True:
            token = self.__private_token

        if (empty(host) == True) or (empty(token) == True):
            try:
                contents = self.get_settings()
                if "bio_bbx_private_domain" in contents:
                    host = contents["bio_bbx_private_domain"]
                if "bio_bbx_private_key" in contents:
                    token = contents["bio_bbx_private_key"]
            except Exception as e:
                raise e

        if (empty(host) == True) or (empty(token) == True):
            raise Exception("Empty BBrowserX setting (Host - Token)")

        return LensSCConnector(
            host=host,
            token=token,
            ssl=ssl
        )

    """
      Args:
        public_token:
          The API token to verify authority. Generated in talk2data.bioturing.com.
          If empty, BioColab will retrieve this information from your settings.
    """

    def get_talk2data(
        self,
        public_token: str = ""
    ):
        host = "https://talk2data.bioturing.com/t2d_index_tool/"
        token = public_token
        if empty(token) == True:
            token = self.__public_token

        if empty(token) == True:
            try:
                contents = self.get_settings()
                if "bio_bbx_t2d_key" in contents:
                    token = contents["bio_bbx_t2d_key"]
            except Exception as e:
                raise e

        if empty(token) == True:
            raise Exception("Empty BBrowserX setting (Public Token)")

        return BBrowserXConnector(
            host=host,
            token=token,
            ssl=True
        )

    """
      Args:
        bioflex_token:
          The API token to verify authority. Generated in https://colab.bioturing.com
          If empty, BioColab will retrieve this information from your settings.
    """

    def get_bioflex(
        self,
        bioflex_token: str = ""
    ):
        token = bioflex_token
        if empty(token) == True:
            token = self.__bioflex_token

        if (empty(token) == True):
            try:
                contents = self.get_settings()
                if "bio_bioflex_public_key" in contents:
                    token = contents["bio_bioflex_public_key"]
            except Exception as e:
                raise e

        if (empty(token) == True):
            raise Exception("Empty BioFlex setting (TOKEN)")

        return bioflex.connect(token)
