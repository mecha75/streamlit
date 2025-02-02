from pathlib import Path

basedir = Path(__file__).parent.parent
user1 = "superpower"
pw1 = "mecha75"
# ip1 = "na-moung.iptime.org:63306"
ip1 = "138.2.44.37:3306"

db1 = "7habbits"
mysql_url = f"mysql+pymysql://{user1}:{pw1}@{ip1}/{db1}?charset=utf8"

# Base config클래스 작성하기
class BaseConfig:
    SECRET_KEY = "k"
    WTF_CSRF_SECRET_KEY="k"
    # 이미지 업로드 경로에 apps/images를 지정한다.
    UPLOAD_FOLDER = str(Path(basedir,"apps","uploadfiles"))
    # UPLOAD_FOLDER_fx = str(Path(basedir,"apps","uploadfiles/fx"))
    # UPLOAD_FOLDER_sales = str(Path(basedir,"apps","uploadfiles/salesfigure"))

# BaseConfig 클래스를 상속하여 LocalConfig를 작성한다.
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = mysql_url
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLAlCHEMY_ECHO=True

# BaseConfig 클래스를 상속하여 TestingConfig를 작성한다.
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = mysql_url
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLAlCHEMY_ECHO=False

# config 사전에 매핑한다.
config = {
    "testing":TestingConfig,
    "local":LocalConfig,
}
