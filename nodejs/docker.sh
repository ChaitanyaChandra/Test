docker build -t ChaituChowdary/spec-app .
docker run -itd -p 8080:3000 --name=ServerOne -h ServerOne ChaituChowdary/spec-app
docker exec -it ServerOne /bin/bash