"use client"
import { Sidebar } from "flowbite-react";

export default function Home() {


  return (
    <Sidebar aria-label="Default sidebar example">
      <Sidebar.Items>
        <Sidebar.ItemGroup>
          <Sidebar.Item
            href="#"
            // icon={u}
          >
            Sign In
          </Sidebar.Item>
          <Sidebar.Item
            href="#"
            // icon={b}
          >
            Sign Up
          </Sidebar.Item>
        </Sidebar.ItemGroup>
      </Sidebar.Items>
    </Sidebar>
  )
}
