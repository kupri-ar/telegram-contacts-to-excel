@echo off

cd app

rem Start the Docker Compose project in detached mode
docker-compose up -d --build

rem Wait for the container to start
:check_container_running
setlocal EnableDelayedExpansion
for /f "usebackq tokens=*" %%i in (`docker-compose ps -q app`) do (
    set container_id=%%i
)
for /f "usebackq tokens=*" %%i in (`docker inspect -f "{{.State.Running}}" !container_id!`) do (
    set container_running=%%i
)
if not "!container_running!"=="true" (
    timeout /t 1 >nul
    goto check_container_running
)

echo Press Enter to continue...

rem Attach to the container
docker attach !container_id!

rem Down the Docker Compose project in detached mode
docker-compose down
