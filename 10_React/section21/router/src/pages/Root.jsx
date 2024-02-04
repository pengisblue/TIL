import { Outlet } from "react-router-dom";
import MainNavigation from "../components/MAinNavigation";
import classes from "./Root.module.css";

export default function RootLayout() {
  return (
    <>
      <MainNavigation />
      <main className={classes.content}>
        <Outlet />
        {/* 자식 라우터가 표시될 곳을 의미 */}
      </main>
    </>
  );
}
