import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6033727590:AAFPRMrOxi0o3oZ-onoBaMywMu2NlU073Wk)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BJWap1sBu0UbkmK_A-JFYrAefXaMiJrk4G1RDHHDUr2w1n4IZl4rIKOFBc2cCeovlgjRNhzyPqeCkYWz_6o4OO_79S5hZZO7taryPfNeu-ZEaLlLhFzlFv21GsOqXTWMI37pHWg0vrZIIL6VaNYeKUCl5W9eqEvBWNcDbIEZcP4ganzgq3RUGw8L4EOSV8t23UlSelfbPxdFDdTjdsbVi7A-j5M8TrFmUn8SbjyC9Ld3Khd4tHKpGY4hu-skAdcbUz3y4Yzs3oDpE1YtnLehJUaK9gRkJgyVaSGWZEaJFWralyiCTXBZ64qI_TGm-s9RkIGvVItp6anOm1gmvPaRKuJo6xGbxzE=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
