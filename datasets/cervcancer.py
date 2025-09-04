# The dataset contains 19 attributes regarding ca cervix behavior risk with class label is ca_cervix with 1 and 0 as values which means the respondent with and without ca cervix, respectively.

# pip3 install ucimlrepo

from ucimlrepo import fetch_ucirepo
dataset = fetch_ucirepo(id=537)

df = pd.DataFrame(dataset.data.features)

if dataset.data.targets is not None:
    targets = pd.DataFrame(dataset.data.targets)
    df = pd.concat([df, targets], axis=1)
