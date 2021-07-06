# Função pra pegar horario atual utc 3
def horario():
    from datetime import datetime, timezone, timedelta, timezone
    global momento

    data_e_hora_atuais = datetime.now() # Pega o horario
    data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y-horas-%H:%M") # Ajuta pra ficar mais bonito

    diferenca = timedelta(hours= -3) # Define a diferança de acordo com São Paulo
    fuso_horario = timezone(diferenca) # Ajustando o horario para o horario de São Paulo

    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    momento = data_e_hora_sao_paulo.strftime("%d-%m-%Y-horas-%H:%M") # A varivel momento fica com o horario atual fomratado
