"use client"

import { ChatAPI } from "@/api/ChatAPI";
import { AuthAPI } from "@/api/AuthAPI";
import { updateToken, removeToken } from "@/api/client";

export const initializeAuthentication = () => {
  const token = typeof window !== "undefined" ?
     window.sessionStorage.getItem('token') 
     : 
     "";
  // const token = sessionStorage.getItem('token');
  console.log(`token: ${token}`)
  return token? token : ""
}

export const AppController = (state, dispatch) => {
    const login = (username, password) => {
      AuthAPI.login(username, password).then((response) => {
        updateToken(response.token);
        dispatch({type: "setToken", payload: response.token})
      }).catch( error => {
        alert(error.response.data.detail);
      });
    }
    const logout = () => {
      removeToken();
      dispatch({type: "setToken", payload: ""})
    }
    const getChats = () => {
        ChatAPI.getAll(state.token).then((response) => {
            dispatch({type: "setChats", payload: response})
        });
    }
    const setMessages = (messages) => {
        dispatch({type: "setMessages", payload: messages})
      };

    return {
        login,
        logout,
        getChats,
        setMessages,
    }
}