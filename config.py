from datetime import datetime, timedelta

bearer_token = 'your_bearer_token'

next_date = (datetime.now() + timedelta(hours=12)).strftime('%Y-%m-%d')
# now = (datetime.now() - timedelta(hours=1)).strftime('%Y-%m-%d %H')
now = datetime.now().strftime('%Y-%m-%d %H')
my_id = "your_gym_id"

tg_token = 'your_token'
chat_id = 'your_user_id'

## GET
headers = {
    'User-Agent': 'OnVirtualGym/2 CFNetwork/3826.400.120 Darwin/24.3.0',
    'Content-Type': 'Content-Type',
    'Connection': 'keep-alive',
    'Accept-Language': 'en_GB',
    'Accept': '*/*',
    'Authorization': f'Bearer {bearer_token}',
}

endpoint = 'https://gofitness.onvirtualgym.com/apiGroupClasses.php'

shedule_params = {
    'method': 'getAllGroupClassesMap',
    'numSocio': my_id,
    'idGinasio': '8',
    'selectedDate': next_date,
}

## POST
post_req_headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {bearer_token}',
}

add_appointment_params = {
    'method': 'addPreReservationOfClientToActivityGroupClasses',
}

add_appointment_json_data = {
    'fk_numSocio': my_id,
    'clientDateTime': now,
    'data_atividade': next_date,
    'idFuncionariosAtividadesGrupo': '1260',
}


remove_appointment_params = {
    'method': 'uncheckPreReservationOfClientToActivityGroupClasses',
}

remove_appointment_json_data = {
  "data_atividade" : next_date,
  "idFuncionariosAtividadesGrupo" : "1260",
  "fk_numSocio" : my_id
}