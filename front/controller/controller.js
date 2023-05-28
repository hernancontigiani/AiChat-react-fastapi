import { ChatAPI } from "../api/ChatAPI";


export const AppController = (state, dispatch) => {

    const getChats = () => {
        ChatAPI.getAll().then((response) => {
          if (response) {
            dispatch({type: "setChats", payload: response})
          }
        });
    }
    const setMessages = (messages) => {
        dispatch({type: "setMessages", payload: messages})
      };

    return {
        getChats,
        setMessages,
    }
}