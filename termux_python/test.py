import numpy as np
import torch

n_buckets=32
x=np.array([[1,2,3,4,5,6,7,8,9,10],[1,2,3,5,6,8,0,11,22,34],[12,3,44,56,23,6,8,7,9,11]]) # 6*3
y=np.random.randn(10,6)
vectors_rota=np.dot(x,y)
vectors_rota=np.hstack([vectors_rota,-vectors_rota])
print(vectors_rota)
vec_bucket=np.argmax(vectors_rota,axis=1)
print(vec_bucket)
vec_bucket=torch.tensor(vec_bucket)
print(vec_bucket.sort(dim=-1))