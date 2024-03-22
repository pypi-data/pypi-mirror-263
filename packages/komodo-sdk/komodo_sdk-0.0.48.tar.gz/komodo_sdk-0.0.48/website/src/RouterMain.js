import React, { useEffect, useState } from "react";
import {
  HashRouter as Router,
  Routes,
  Route,
  Navigate,
  Outlet,
} from "react-router-dom";
import "./App.css";
import Login from "./auth/Login";
// import Chat from "./components/chat/Chat"
// import Details from "./components/chat/Details";
import ChatBot from "./pages/chatBot";
import Profile from "./pages/profile/Profile";
import Settings from "./pages/settings/Settings";
import Chat from "./pages/chat/Chat";
import Details from "./pages/chat/Details";
import Terms from "./pages/privacy/Terms";
import Privacy from "./pages/privacy/Privacy";
import Signup from "./auth/Signup";
import Pricing from "./pages/pricing/Pricing";
import Home from "./components/Home";
import Document from "./pages/Document";
import { ApiGet } from "./API/API_data";
import { API_Path } from "./API/ApiComment";
import { Helmet } from "react-helmet";

function Authorization() {
  const user = JSON.parse(localStorage.getItem("komodoUser"));
  return user?.email !== null &&
    user?.email !== undefined &&
    user?.email !== "" ? (
    <Outlet />
  ) : (
    <Navigate to={"/home"} />
  );
}

function App() {
  const [agentList, setAgentList] = useState();
  const [name, setName] = useState();
  const [company, setCompany] = useState();
  const agentDetails = async () => {
    try {
      const agent = await ApiGet(API_Path.agentDetails);
      setAgentList(agent?.data);
      setName(agent?.data?.name);
      setCompany(agent?.data?.company);
    } catch (error) {
      console.log("user details get ::error", error);
    }
  };

  useEffect(() => {
    agentDetails();
  }, []);

  return (
    <>
      <Helmet>
        <title>{name && company ? `${name} - ${company}` : ""}</title>
      </Helmet>

      <Router>
        <Routes>
          <Route path="/signup" strict element={<Signup />} />
          <Route path="/terms" element={<Terms />} />
          <Route path="/pricing" element={<Pricing />} />

          {agentList?.type === "retail" ? (
            <Route path="/" strict>
              <Route index element={<Home />} />
              <Route path="/home" strict element={<Home />} />
            </Route>
          ) : (
            <Route path="/" strict>
              <Route index element={<Login />} />
              <Route path="/login" strict element={<Login />} />
            </Route>
          )}
          <Route path="/login" strict element={<Login />} />
          <Route path="/home" strict element={<Home />} />

          {/* </Route> */}

          <Route element={<Authorization />}>
            <Route path="/chat" element={<Chat />} />

            <Route path="/chatbot" element={<ChatBot />} />
            <Route path="/document" element={<Document />} />
            {/* <Route path="/document" element={<ChatBot />} /> */}
            <Route path="/details/:id" element={<Details />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/settings" element={<Settings />} />

            <Route path="/privacy" element={<Privacy />} />
          </Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
