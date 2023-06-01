# MLFlow Server
No local dependencies.

---
...

# Configuration

- Clone current repository:
```
git clone https://github.com/e183b796621afbf902067460/ranepa-mlflow-server.git
```

- Get into the project folder:
```
cd ranepa-mlflow-server/
```

- Set environment variables in [.env](https://github.com/e183b796621afbf902067460/ranepa-mlflow-server/blob/master/mlruns/.env).

# Deploy

- Became super user:
```
sudo su
```

- Deploy `minio` service:
```
docker-compose up -d --build --force-recreate minio
```

- Create `csv-files`, `mlflow-compute-logs` buckets and Access Keys at the MinIO's UI.

- Set Access and Secret Keys in [docker-compose](https://github.com/e183b796621afbf902067460/ranepa-mlflow-server/blob/master/docker-compose.yml).

- Deploy `mlflow` and `mysql` services:
```
docker-compose up -d --build --force-recreate mlflow mysql
```

- Copy `diabetes_prediction_dataset.csv` from local machine to `csv-files` bucket in Minio.

- Copy `mlflow` service's ID by running:
```
docker ps -a
```

- And run experiment inside of `mlflow` service by `python3`:
```
docker exec -it <ID> python3 elastic_net/elastic_net.py
```

- Or by `mlflow run`:
```
docker exec -it <ID> mlflow run elastic_net --env-manager=local
```

- Also we can specify different params for experiment:
```
docker exec -it <ID> mlflow run elastic_net -P alpha=0.5 -P l1_ratio=0.5 --env-manager=local
```
