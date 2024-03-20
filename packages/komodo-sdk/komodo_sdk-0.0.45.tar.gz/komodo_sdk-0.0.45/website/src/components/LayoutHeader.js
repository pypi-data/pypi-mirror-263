import React from "react";
import { Link, useLocation } from "react-router-dom";

const LayoutHeader = () => {
  const komodoUser = JSON.parse(localStorage.getItem("komodoUser"));
  const location = useLocation();

  return (
    <div className="flex items-center sm:flex-col w-full justify-between">
      <h1 className="text-3xl font-cerebrisemibold ">Komodo AI</h1>
      <div className="flex gap-14">
        <Link to="/home">
          <p
            className={`text-[20px] font-cerebriregular leading-[24px] ${
              location?.pathname === "/home"
                ? "text-[#316FF6]"
                : "text-[#333333]"
            }`}
          >
            Home
          </p>
        </Link>
        <Link to="/pricing">
          <p
            className={`text-[20px] font-cerebriregular leading-[24px] ${
              location?.pathname === "/pricing"
                ? "text-[#316FF6]"
                : "text-[#333333]"
            }`}
          >
            Pricing
          </p>
        </Link>
      </div>
      <div className="flex gap-6 sm:justify-end sm:gap-3">
        <div className="flex gap-3">
          {komodoUser?.email !== null &&
          komodoUser?.email !== undefined &&
          komodoUser?.email !== "" ? null : (
            <>
              <Link to="/login">
                <button className="bg-[#F3F7FF] text-[18px] font-cerebri border text-customBlue border-[#C7D8FD] py-2 px-4 rounded-[10px] min-w-[107px]">
                  Login
                </button>
              </Link>
              <Link to="/signup">
                <button className="bg-customBlue text-[18px]  font-cerebri py-2 px-5 text-white rounded-[10px] min-w-[113px]">
                  Sign up
                </button>
              </Link>
            </>
          )}

          <Link to="/chat">
            <button className="bg-customBlue text-[18px] font-cerebri py-2 px-5 text-white rounded-[10px] min-w-[113px]">
              Try Now
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default LayoutHeader;
