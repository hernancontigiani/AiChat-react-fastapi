import { data } from "browserslist";
import { api } from "./client"

const controller = new AbortController();

export const AuthAPI = {
  login: async function () {
    
    const response = await api.request({
      url: `/auth/login`,
      method: "POST",
      signal: controller.signal,
      data: {
        username: 'hernan',
        password: '1234'
      }
    })
    if(response) {
      return response.data
    }
  },
  abort: function(){
    controller.abort()
  },
}