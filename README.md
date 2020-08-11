# Deployment  
## Local deployment

### Create environment
```bash
$ cp -R .envs.example .envs
```
`.envs` folder structure
```bash
.envs
├── app.env
└── db.env
```
### Build and start Docker containers
Build containers
```bash
$ docker-compose -f local.yml build
````
Start containers in detached mode (go to localhost:8000 when all containers up)  
```bash
$ docker-compose -f local.yml up -d
```
Create superuser
```bash
$ docker-compose -f local.yml run --rm app ./manage.py createsuperuser
```

### Daily basis usage
Start containers in detached mode
```bash
$ docker-compose -f local.yml up -d
```
Stop and destroy containers and network
```bash
$ docker-compose -f local.yml down
```
Show containers logs in realtime:

All logs  from all containers  
```bash
$ docker-compose -f local.yml logs -f
```
Or you can watch logs from one service(container) - set service name  
```bash
$ docker-compose -f local.yml logs -f app
$ docker-compose -f local.yml logs -f db
```  

Run Django management commands
```bash
$ docker-compose -f local.yml run --rm app ./manage.py management_command
```
### Useful Docker commands
Show containers status
```bash
$ docker-compose -f local.yml ps
```
Manually restart container
```bash
$ docker-compose -f local.yml restart service_name
```
Manually rebuild container and restart service
```bash
$ docker-compose -f local.yml up -d --build --no-deps service_name
```
Show containers performance
```bash
$ docker stats
```
Show volumes list
```bash
$ docker volume ls
```
Manually remove volume
```bash
$ docker volume rm volume_name
```

```
