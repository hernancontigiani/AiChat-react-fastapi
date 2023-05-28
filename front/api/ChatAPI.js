import { api } from "./client"

const controller = new AbortController();

export const ChatAPI = {
  getAll: async function (token) {
    console.log(token)
    const response = await api.request({
      url: `/chats/`,
      headers: {
        "Authorization": `Bearer ${token}`
      },
      method: "GET",
      signal: controller.signal
    })
    if(response) {
      return response.data
    }
  },
  abort: function(){
    controller.abort()
  },
}