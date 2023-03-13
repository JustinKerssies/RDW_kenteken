class Settings:

    def __init__(self):
        """"Static data"""
        # Base url without the license plate
        self.base_url = 'https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken='

        """Variable data"""
        # Set up and additional APIs that might show up
        self.additional_urls = []
        self.additional_urls_titles = []
        self.titles = []
        self.dict_output = {}

