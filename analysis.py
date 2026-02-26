import pyshark
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка дампа
cap = pyshark.FileCapture('dhcp.pcapng')

# Извлечение DNS-запросов
dns</i>requests = []
for packet in cap:
    try:
        if 'DNS' in packet:
            dns<i>requests.append(packet)
    except AttributeError:
        pass  # Игнорируем пакеты без нужных атрибутов

# Создание списка IP-адресов и доменов
ip</i>addresses = set()
for request in dns<i>requests:
    if hasattr(request.dns, 'qry</i>name'):
        ip<i>addresses.add(request.dns.qry</i>name)

# Визуализация количества DNS-запросов
dns<i>count = len(dns</i>requests)
plt.figure(figsize=(10, 6))
sns.countplot(x=[1] * dns<i>count)
plt.title('Количество DNS-запросов')
plt.xlabel('DNS Запросы')
plt.ylabel('Число запросов')
plt.xticks(ticks=[], labels=[])
plt.savefig('dns</i>requests<i>count.png')
plt.show()
