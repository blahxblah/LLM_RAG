# 필요한 라이브러리 import하기
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from lib.etc import get_config_values

[host, user, password, database, port] = get_config_values([
                                                            ('mysql', 'host'),
                                                            ('mysql', 'user'),
                                                            ('mysql', 'password'),
                                                            ('mysql', 'database'),
                                                            ('mysql', 'port'),
                                                            ])

# SQLAlchemy 사용할 DB URL 생성하기
SQLALCHEMY_DATABASE_URL = f"mysql+mysqldb://{user}:{password}@{host}:{port}/{database}" # mysqlclient 사용
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# SQLAlchemy engine 생성하기
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"auth_plugin": "mysql_native_password"})
# 8버전의 mysql은 인증방식이 caching_sha2_password 이고, 
# mysqlclient는 이 방식을 지원하지 않기 때문에 auth_plugin을 레거시로 설정
# 또는 /etc/mysql/mysql.conf.d/mysqld.cnf 에서 default_authentication_plugin=mysql_native_password 추가하고 mysql 재시작
# 또는 ALTER USER 'yourusername'@'localhost' IDENTIFIED WITH mysql_native_password BY 'youpassword';

# connect_args={"check_same_thread": False} => SQLite 옵션
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# DB 세션 생성하기
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class 생성하기
Base = declarative_base()