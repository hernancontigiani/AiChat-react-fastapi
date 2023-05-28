# Renaiss fullstack challenge



# How to setup a new project
## Create front app
```sh
docker run --rm -it --user "$(id -u):$(id -g)" -v $(pwd):/front -w=/front node:18.16.0 npx create-next-app@latest --js front
```

## Instalar librerias del proyecto
Lanzar el docker
```sh
$ docker run --rm -it --user "$(id -u):$(id -g)" -p 3000:3000 -v $(pwd)/front:/front -w=/front node:18.16.0 bash
```

Lanzar los siguientes comandos
```sh
$ npm install axios
$ npm install @mui/material @mui/icons-material @emotion/react @emotion/styled
$ npm install classnames
```
```sh
$ npm install axios
$ npm install flowbite flowbite-react
```

