
To deploy current dir Dockerfile to cloud run / de-zoom is the service name 
# gcloud run deploy de-zoom     --region europe-west9 --source .

curl -X POST -H "Content-Type: application/json" http://localhost:5000/api/new -d '{
            "debut": "23-01-2024",
            "fin": "23-01-2024",
            "logiciel": "lalao",
            "retrocession": 34,
            "location": "la rochelle",
            "minutes_from_home": 30,
            "color": "red",
        }'



