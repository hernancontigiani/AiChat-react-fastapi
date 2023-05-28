import axios from 'axios'

const baseURL = `http://127.0.0.1:5000/api`;

export const api = axios.create({
    baseURL: baseURL,
});

let token = "123"

export const updateToken = (newToken) => {
  token = newToken
}

api.interceptors.request.use(function (config) {
  config.headers = {
    "Authorization": `Token ${token}`
  }
  return config
})

// defining a custom error handler for all APIs
const errorHandler = (error) => {
  if (axios.isCancel(error)) {
    console.log('successfully aborted');
    return;
  }

  return Promise.reject(error)
}
  
// registering the custom error handler to the
// "api" axios instance
api.interceptors.response.use(undefined, (error) => {
  return errorHandler(error)
})
