import mne
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, FastICA
import scipy.stats

# Caminho do arquivo EDF
caminho_arquivo = "/home/paulo/Downloads/scientisst-move-annotated-wearable-multimodal-biosignals-recorded-during-everyday-life-activities-in-naturalistic-environments-1.0.0/K2Q2/scientisst_chest.edf"

# Carregar o arquivo EDF
raw = mne.io.read_raw_edf(caminho_arquivo, preload=True)

# Definir o intervalo de tempo (0 a 10 segundos)
start_time, end_time = 0, 10
raw.crop(tmin=start_time, tmax=end_time)

# Obter os dados
data = raw.get_data()

# Normalizar os sinais para terem amplitudes iguais
normalized_data = data / np.max(np.abs(data), axis=1, keepdims=True)

# Calcular características (média, variância, mediana, curtose)
mean_signal = np.mean(normalized_data, axis=1)
variance_signal = np.var(normalized_data, axis=1)
median_signal = np.median(normalized_data, axis=1)
kurtosis_signal = scipy.stats.kurtosis(normalized_data, axis=1)

# Aplicar o PCA
n_components_pca = 4  # Ajustar o número de componentes conforme necessário
pca = PCA(n_components=n_components_pca)
pca_data = pca.fit_transform(normalized_data.T).T

# Aplicar o ICA
n_components_ica = 4  # Ajustar o número de componentes conforme necessário
ica = FastICA(n_components=n_components_ica, random_state=97)
ica_data = ica.fit_transform(normalized_data.T).T

# Plotar os quatro gráficos
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

# Gráfico do sinal original ECG
ax1.plot(raw.times, normalized_data[0], label='Sinal Original - ECG', color='blue')
ax1.set_title('Sinal Original - ECG')
ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Amplitude Normalizada')
ax1.legend()

# Gráfico do sinal com PCA como ECG
ax2.plot(raw.times, pca_data[0], label='PCA', color='red')
ax2.set_title('PCA')
ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel('Amplitude Normalizada')
ax2.legend()

# Gráfico do sinal com ICA como ECG
ax3.plot(raw.times, ica_data[0], label='ICA', color='green')
ax3.set_title('ICA')
ax3.set_xlabel('Tempo (s)')
ax3.set_ylabel('Amplitude Normalizada')
ax3.legend()

# Gráfico comparativo dos três sinais de ECG
ax4.plot(raw.times, normalized_data[0], label='Sinal Original - ECG', color='blue')
ax4.plot(raw.times, pca_data[0], label='PCA', color='red')
ax4.plot(raw.times, ica_data[0], label='ICA', color='green')
ax4.set_title('Comparação dos Sinais de ECG')
ax4.set_xlabel('Tempo (s)')
ax4.set_ylabel('Amplitude Normalizada')
ax4.legend()

plt.tight_layout()
plt.show()