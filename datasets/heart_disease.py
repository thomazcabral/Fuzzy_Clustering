# This database contains 76 attributes. The "goal" field refers to the presence of heart disease in the patient. It is integer valued from 0 (no presence) to 4. 
dataset = fetch_ucirepo(id=45)

# Converter os dados em DataFrame
df = pd.DataFrame(dataset.data.features)

# Se quiser adicionar os rótulos (se existirem)
if dataset.data.targets is not None:
    # targets pode ser Series ou DataFrame dependendo do conjunto
    targets = pd.DataFrame(dataset.data.targets)
    df = pd.concat([df, targets], axis=1)
