from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from typing import List
from jose import JWTError, jwt
from passlib.context import CryptContext
from apscheduler.schedulers.background import BackgroundScheduler
from services.zabbix import ZabbixService
from services.grafana import GrafanaService
from services.wazuh import WazuhService
from services.graylog import GraylogService
from services.suricata import SuricataService
from models.report import Report
from utils.exporter import export_to_csv, export_to_powerbi
from utils.logger import log_error, log_info

app = FastAPI()

# Configuração de JWT
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Função para criar token JWT
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Função para verificar token JWT
def verify_token(token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise credentials_exception

# Dependência para proteger as rotas
def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_token(token)

@app.post("/token")
async def login_for_access_token(username: str, password: str):
    if username != "admin" or password != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/generate-report/")
async def generate_report(report: Report, token: str = Depends(get_current_user)):
    try:
        zabbix_service = ZabbixService()
        grafana_service = GrafanaService()
        wazuh_service = WazuhService()
        graylog_service = GraylogService()
        suricata_service = SuricataService()

        # Gerar dados para o relatório
        zabbix_data = zabbix_service.get_data(report)
        grafana_data = grafana_service.get_data(report)
        wazuh_data = wazuh_service.get_data(report)
        graylog_data = graylog_service.get_data(report)
        suricata_data = suricata_service.get_data(report)

        full_report_data = {
            "zabbix": zabbix_data,
            "grafana": grafana_data,
            "wazuh": wazuh_data,
            "graylog": graylog_data,
            "suricata": suricata_data
        }

        # Exportar o relatório
        if report.format == "csv":
            export_to_csv(full_report_data, report.output_dir)
        elif report.format == "powerbi":
            export_to_powerbi(full_report_data, report.output_dir)
        else:
            raise HTTPException(status_code=400, detail="Invalid format")

        return {"message": "Report generated successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating report: {str(e)}")
