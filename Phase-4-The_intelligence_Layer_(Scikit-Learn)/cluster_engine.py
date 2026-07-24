import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Customer Data: Annual_Income (k$), Spending_Score (1-100)
data = {
    'Income': [15, 16, 17, 18, 19, 70, 71, 72, 73, 74, 130, 135, 140, 145, 150],
    'Score':  [10, 12, 11, 14, 15, 55, 50, 52, 58, 59, 90,  95,  92,  98,  99]
}

df = pd.DataFrame(data)
print("--- Unsupervised Clustering Engine Online ---")

X = df

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

model = KMeans(n_clusters=3,random_state=42,n_init=10)

clusters = model.fit_predict(X_scaled)

print(clusters,"\n")
print(model.cluster_centers_)