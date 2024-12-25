import torch

# Verificar se a GPU está disponível
gpu_available = torch.cuda.is_available()

# Imprimir o status da GPU
print(f"GPU disponível: {gpu_available}")

# Se a GPU estiver disponível, imprimir o nome da GPU
if gpu_available:
    print(f"Nome da GPU: {torch.cuda.get_device_name(0)}")