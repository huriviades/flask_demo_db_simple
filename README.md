
# Demo Flask con Docker Compose

Este proyecto levanta un entorno con **Flask + PostgreSQL** usando
Docker Compose, incluyendo carga de base de datos y despliegue de la
aplicación.

------------------------------------------------------------------------

## 📁 1. Crear directorio de trabajo

``` bash
mkdir -p /home/$USER/dockers/demo
cd /home/$USER/dockers/demo
apt install git -y
```

------------------------------------------------------------------------

## 📦 2. Cargar imagen Docker
(Usa la imagen generada en clases llamada Ubuntu_web_dev-2.tar.gz)

``` bash
docker load --input ubuntu_web_dev-2.tar.gz
```

------------------------------------------------------------------------

## ⚙️ 3. Crear archivo docker-compose.yml

``` bash
cat > docker-compose.yml << "EOF"
version: "3.4"

services:
  demo_flask_compose:
    restart: "no"
    image: ubuntu/web:2
    ports:
      - "80:80"
    environment:
      - TZ=UTC
    networks:
      ADSL:
        ipv4_address: 172.30.0.10
    volumes:
      - 'demo_flask_compose_data:/var/www/html'

  demo_flask_db:
    image: 'bitnamilegacy/postgresql:14.9.0'
    ports:
      - '5432:5432'
    environment:
      - TZ=UTC
      - POSTGRESQL_DATABASE=demo_db
      - POSTGRESQL_USERNAME=usuario_prueba
      - POSTGRESQL_PASSWORD=PWD123
    networks:
      ADSL:
        ipv4_address: 172.30.1.10
    volumes:
      - 'demo_db_compose_data:/bitnami/postgresql'

networks:
  ADSL:
    external: true

volumes:
  demo_flask_compose_data:
    driver: local
  demo_db_compose_data:
    driver: local
EOF
```

------------------------------------------------------------------------

## ▶️ 4. Levantar servicios

``` bash
docker-compose up -d
```

------------------------------------------------------------------------

## 🗄️ 5. Cargar base de datos
(Ver en el repo, la subcarpeta llamada instrucciones)

``` bash
docker cp D_TimeZone_data.sql demo-demo_flask_db-1:/tmp/D_TimeZone_data.sql
docker-compose exec demo_flask_db bash -c "export PGPASSWORD='PWD123'; psql -U usuario_prueba -d demo_db -f /tmp/D_TimeZone_data.sql"
```

------------------------------------------------------------------------

## 🐳 6. Acceder al contenedor web

``` bash
docker-compose exec demo_flask_compose bash
```

------------------------------------------------------------------------

## 📥 7. Preparar el proyecto Flask

``` bash
cd /var/www/html
git clone --no-checkout https://github.com/huriviades/flask_demo_db_simple.git
cd flask_demo_db_simple
git sparse-checkout init --cone
git sparse-checkout set demo_web
git checkout main
rm -rf ../demo_web
mv demo_web/ ../
cd .. && rm -rf flask_demo_db_simple
cd demo_web/
supervisorctl restart demo_web
```

------------------------------------------------------------------------

## ✅ Resultado

-   Aplicación Flask en http://localhost
-   Base de datos PostgreSQL configurada
-   Servicios corriendo con Docker Compose

------------------------------------------------------------------------

## ⚠️ Notas

-   Asegúrate de que la red ADSL exista.
-   El comando rm -rf elimina contenido previo.
