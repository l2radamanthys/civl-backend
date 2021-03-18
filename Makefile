DB_NOMBRE_DEL_DUMP= ~/Dropbox/Trabajo/CIVcivlackups/civl_backup_`date +'%Y%m%d_%Hhs%Mmin'`.dump
CARPETA_BACKUPS = "-1"
DB_DUMP_MAS_RECIENTE=`ls -Art ~/Dropbox/Trabajo/CIVL/backups/civl_*.dump | tail -n 1`
NOMBRE_RELEASE = `date +"%Y%m%d%H%M"`
SERVIDOR = "webapp@167.172.236.158"

N=[0m
R=[00;31m
G=[01;32m
Y=[01;33m
B=[01;34m
L=[01;30m

compandos:
	@clear
	@echo ""
	@echo "${Y}CIVL Backend"
	@echo "${B}COMANDOS DISPONIBLES"
	@echo ""
	@echo "	${G}iniciar${N}: Instalar dependencias"
	@echo "	${G}ejecutar${N}: Correr servidor de pruebas"
	@echo "	${G}ejecutar_worker${N}: Ejecuta Servicios"
	@echo "	${G}crear_migraciones${N}"
	@echo "	${G}migrar${N}"
	@echo "	${G}test${N}"
	@echo "	${G}test_live${N}: Ejecutar los test automaticamente"
	@echo "	${G}reset${N}: Resetear la base de datos"
	@echo "	${G}build_requirements${N}"
	@echo "	${G}collectstatic${N}"
	@echo "	${G}realizar_backup${N}"
	@echo "	${G}cargar_ultimo_dump${N}"
	@echo ""
	@echo "	${G}docker_build${N}"
	@echo "	${G}docker_run${N}"
	@echo "	${G}generar_build${N}"
	@echo ""

iniciar:
	@pipenv install

ejecutar:
	@pipenv run python manage.py runserver

ejecutar_alt:
	@pipenv run python manage.py runserver 8080

ejecutar_worker:
	@pipenv run python manage.py rqworker

crear_migraciones:
	@pipenv run python manage.py makemigrations

migrar:
	@pipenv run python manage.py migrate --noinput

test:
	@echo "${G}Ejecutando tests ...${N}"
ifeq ($(filtro),)
	pipenv run pytest
else
	pipenv run pytest -k $(filtro)
endif

test_live:
ifeq ($(filtro),)
	pipenv run ptw
else
	pipenv run ptw -- -k $(filtro)
endif

reset:
	dropdb --if-exists civl -e; createdb civl
	pipenv run python manage.py migrate --noinput

build_requirements:
	@pipenv lock -r > requirements.txt
	cat requirements.txt

collectstatic:
	pipenv run python manage.py collectstatic

realizar_backup:
	@echo "Creando el archivo ${DB_NOMBRE_DEL_DUMP}"
	@pg_dump -F c tca > ${DB_NOMBRE_DEL_DUMP}

realizar_backup_produccion:
	@echo $(ssh $SERVIDOR 'ls -t backups | head -1')

cargar_ultimo_dump:
	@echo "Se cargará el dump mas reciente: ${DB_DUMP_MAS_RECIENTE}"
	dropdb --if-exists tca_gt -e; createdb tca_gt
	pg_restore --no-acl --no-owner -d tca_gt ${DB_DUMP_MAS_RECIENTE}

diagrama:
	@pienv run python manage.py graph_models tca -a -g -o tca.png

generar_build:
	./generar_build.sh ${NOMBRE_RELEASE}

