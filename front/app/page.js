import ChatList from "@/components/ChatList"
import NavBar from "@/components/NavBar"
import Chat from "@/components/Chat"


export default function Home() {
    return (
    <div className="flex flex-col h-screen">
        <NavBar />
        <ChatList />
        <Chat />
    </div>

    )
}