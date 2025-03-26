import requests
import config as c
import pandas as pd


def get_schedule():
    response = requests.get(c.endpoint, params=c.shedule_params, headers=c.headers)

    if response.json()['status'] == 200:
        frame = pd.DataFrame.from_records(response.json()['getAllGroupClassesMap'])
        frame['dow'] = pd.to_datetime(frame['dia']).dt.weekday
        frame = frame[['dia', 'dow', 'hora', 'nomeAtividade', 'intensidadeAula', 'nickname', 'canPreReservateGroupClassNow', 'id_funcionariosAtividadesGrupo', 'dataRegistoReserva']]
        return frame
    
def check_my_conditions(frame:pd.DataFrame):
    if (frame is None) or (len(frame) < 1):
        return (False, dict())

    frame = frame[(frame['nomeAtividade'] == 'CYCLING') & (frame['canPreReservateGroupClassNow'] == True) & (frame['dataRegistoReserva'].isnull())]

    if frame['dow'].values[0] == 5:
        frame = frame[frame['hora'] >= '09:00:00']
    else:
        frame = frame[frame['hora'] >= '18:00:00']

    return (True, frame.to_dict('list'))

def make_appointment(data:dict):
    json_data = c.add_appointment_json_data
    json_data['idFuncionariosAtividadesGrupo'] = data['id_funcionariosAtividadesGrupo'][0]

    response = requests.post(c.endpoint, params=c.add_appointment_params, headers=c.post_req_headers, json=json_data)

    if response.json()['status'] == 200:
        return (True, data, response.json())
    
    return (False, response.json())

def construct_message(data:dict):
    message = f'''🔔 Hey Vlad!\n I've just made a Fitness appinment.\n
    Details:
    ---------------\n
    DATE: {data['dia'][0]}
    TIME: {data['hora'][0]}
    TYPE: {data['nomeAtividade'][0]}
    INTENCITY: {data['intensidadeAula'][0]}
    COACH: {data['nickname'][0]}
    ---------------
    Good luck, sweetie!
    '''
    return message

def send_message(text):
   token = c.tg_token
   chat_id = c.chat_id
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
   results = requests.get(url_req)
   return results

if __name__ == "__main__":
    possible_appointment = check_my_conditions(get_schedule())
    if possible_appointment[0]:
        result = make_appointment(possible_appointment[1])
        if result[0]:
            resp = send_message(construct_message(result[1]))