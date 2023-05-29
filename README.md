# Renaiss fullstack challenge
# Problem
A microservice is required to be created with login functionality and user registration, with access to a chat and a language model for chat history.

The chat history must show the first message that the user sent to the chat and if he wants to access that history, show the rest of the messages.

The user can ask questions of a maximum of 2000 tokens and a maximum of 20 messages. The user must be informed as he progresses in his question the number of tokens left for that question and once the question is sent, he must inform how many questions he has left for that chat. Once the token limit is reached, it should not be allowed to continue writing and once the message limit has been reached, a new chat must be started.

# Stack
- Frontend in Next.js with Javascript.
- Frontend styles/components using flowbite.
- Backend in FastAPI
- Relational database with PostgreSQL
- Dockerized
- Authentication will be done through the use of JWT from the frontend. 

# Start the project
Launch the backend + database docker:
```sh
$ docker-compose up
```
__NOTE__: First time, launch twice to create the database in first place.

Launch nextjs dev docker server:
```sh
docker-compose -f dev_compose.yml up
```

Go to http://localhost:3000

__NOTE__: nextjs dev docker server could be replaced with a nginx server in production after building the application as static files.


# Future improvements
- Add documentation.
- Add tests.
- Remove warning "Extra attributes from the server..." from the console.
- Save JWT in cookies insted of using sessionStorage.
- Add nginx configuration.
- Demo deploy on AWS.


# How to setup a new project from scratch
## Create front app
```sh
docker run --rm -it --user "$(id -u):$(id -g)" -v $(pwd):/front -w=/front node:18.16.0 npx create-next-app@latest --js front
```

## How to intall axios and flowbite
Lanzar el docker
```sh
$ docker run --rm -it --user "$(id -u):$(id -g)" -p 3000:3000 -v $(pwd)/front:/front -w=/front node:18.16.0 bash
```

Lanzar los siguientes comandos
```sh
$ npm install axios
$ npm install flowbite flowbite-react
```

