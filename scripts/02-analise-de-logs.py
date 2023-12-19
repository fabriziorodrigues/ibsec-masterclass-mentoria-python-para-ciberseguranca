'''
Atenção, os códigos foram criados para fins educacionais e não devem ser utilizados para outros fins.
Esses código não são otimizados e portanto não devem ser utilizados em produção.
'''

import pandas as pd

# Carregar dados de log
log_data = pd.read_csv("logs.csv")

# Analisar logs para encontrar padrões suspeitos
# Exemplo: muitas tentativas de login fracassadas de um mesmo IP
suspicious_activity = log_data[log_data['action'] == 'login_failed'].groupby('ip_address').size()
print(suspicious_activity.sort_values(ascending=False))
